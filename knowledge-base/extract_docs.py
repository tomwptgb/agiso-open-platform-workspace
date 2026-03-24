#!/usr/bin/env python3
"""
Extract documentation content from webpack JS chunks of the Agiso Open Platform
(open.agiso.com) and convert to organized Markdown files.
"""

import json
import os
import re
import html
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_JS_DIR = str(BASE_DIR / "raw_js")
DOCS_DIR = str(BASE_DIR / "docs")
ROUTE_MAP = str(BASE_DIR / "extracted" / "route_map.json")

SERVICE_NAMES = {
    'alds': '淘宝自动发货 (ALDS)',
    'acs': '淘宝采购 (ACS)',
    'acpr': '卡券自动充值 (ACPR)',
    'aldsPdd': '拼多多自动发货 (AldsPdd)',
    'aldsIdle': '闲鱼自动发货 (AldsIdle)',
    'aldsJd': '京东自动发货 (AldsJd)',
    'aldsDoudian': '抖店自动发货 (AldsDoudian)',
    'aldsKwai': '快手自动发货 (AldsKwai)',
    'aldsYouzan': '有赞自动发货 (AldsYouzan)',
    'aldsWeidian': '微店自动发货 (AldsWeidian)',
    'aldsWxVideoShop': '微信小店自动发货 (AldsWxVideoShop)',
    'aldsXhs': '小红书自动发货 (AldsXhs)',
    'print': '打印 (Print)',
    'open': '开放平台 (Open)',
    'supplier': '供应商 (Supplier)',
}

# Definitive guide chunk mapping extracted from app.js routes
GUIDE_CHUNK_MAP = {
    'alds': 'chunk-d7f1881c',
    'acs': 'chunk-0c148e7f',
    'aldsPdd': 'chunk-703fd0b8',
    'print': 'chunk-bbaa086a',
    'acpr': 'chunk-2d0c8bac',
    'aldsIdle': 'chunk-f6484d7e',
    'aldsJd': 'chunk-8830b920',
    'aldsDoudian': 'chunk-79c13dcc',
    'aldsKwai': 'chunk-024f49fc',
    'aldsYouzan': 'chunk-25763e18',
    'aldsWeidian': 'chunk-132a80d9',
    'aldsWxVideoShop': 'chunk-408ed5ec',
    'aldsXhs': 'chunk-3c83c27e',
    'open': 'chunk-09c8b3b3',
    'supplier': 'chunk-9bd3ec04',
}

# API path prefix -> service mapping
API_PREFIX_MAP = {
    'acpr': ['acpr'],
    'aldsDoudian': ['aldsDoudian'],
    'aldsIdle': ['aldsIdle'],
    'aldsJd': ['aldsJd'],
    'aldsKwai': ['aldsKwai'],
    'aldsPdd': ['aldsPdd'],
    'aldsWeidian': ['aldsWeidian'],
    'aldsWxVideoShop': ['aldsWxVideoShop'],
    'aldsXhs': ['aldsXhs'],
    'aldsYouzan': ['aldsYouzan'],
    'pdd': ['aldsPdd'],
    'print': ['print'],
    'open': ['open'],
    'tb': ['alds', 'acs'],  # tb (taobao) APIs shared between alds and acs
    'common': ['aldsWeidian'],  # common/tokenDelete is for aldsWeidian
}

PUSH_PREFIX_MAP = {
    'acpr': ['acpr'],
    'aldsDoudian': ['aldsDoudian'],
    'aldsIdle': ['aldsIdle'],
    'aldsJd': ['aldsJd'],
    'aldsKwai': ['aldsKwai'],
    'aldsWeidian': ['aldsWeidian'],
    'aldsWxVideoShop': ['aldsWxVideoShop'],
    'aldsXhs': ['aldsXhs'],
    'aldsYouzan': ['aldsYouzan'],
    'pdd': ['aldsPdd'],
    'print': ['print'],
    'tb': ['alds', 'acs'],
}


def strip_html(text):
    """Convert HTML to plain text / markdown."""
    if not text:
        return ''
    text = str(text)
    text = text.replace('\\n', '\n').replace('\\t', '\t')
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<span\s+class="annotated">\s*//', ' //', text)
    text = re.sub(r'<span\s+class="annotated">', '', text)
    text = re.sub(r'<span\s+style="font-weight:\s*bold;">', '**', text)
    text = re.sub(r'<span\s+style="color:\s*[^"]*">', '', text)
    text = re.sub(r'</span>', '', text)
    text = re.sub(r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", r'[\2](\1)', text)
    text = re.sub(r'</?div[^>]*>', '', text)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text)
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
    text = re.sub(r'<ins>(.*?)</ins>', r'`\1`', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return text.strip()


def clean_json_example(code_str):
    """Clean a JSON example string, removing HTML annotations."""
    if not code_str:
        return ''
    code = str(code_str).strip()
    code = code.replace('\\n', '\n').replace('\\t', '\t')
    code = re.sub(r'<span\s+class="annotated">\s*(.*?)\s*</span>', r' \1', code)
    code = re.sub(r'<[^>]+>', '', code)
    code = html.unescape(code)
    code = re.sub(r'\n{3,}', '\n\n', code)
    return code.strip()


def load_all_js():
    """Load all JS files into memory."""
    files = {}
    for fname in os.listdir(RAW_JS_DIR):
        if fname.endswith('.js'):
            with open(os.path.join(RAW_JS_DIR, fname), 'r', encoding='utf-8') as f:
                files[fname] = f.read()
    return files


def find_unescaped_quote(s, start, quote):
    i = start
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == quote:
            return i
        i += 1
    return -1


def extract_balanced(s, start, open_char, close_char):
    if start >= len(s) or s[start] != open_char:
        return None
    depth = 0
    i = start
    in_string = False
    escape = False
    quote_char = None
    while i < len(s):
        c = s[i]
        if escape:
            escape = False
            i += 1
            continue
        if c == '\\':
            escape = True
            i += 1
            continue
        if in_string:
            if c == quote_char:
                in_string = False
            i += 1
            continue
        if c in ('"', "'", '`'):
            in_string = True
            quote_char = c
            i += 1
            continue
        if c == open_char:
            depth += 1
        elif c == close_char:
            depth -= 1
            if depth == 0:
                return s[start:i+1]
        i += 1
    return None


def extract_module_map(js_content):
    """Extract webpack module path-to-id mapping."""
    maps = {}
    for m in re.finditer(r'"(\./(?:api|push|model|common)/[^"]+)"\s*:\s*"([^"]+)"', js_content):
        path, mod_id = m.group(1), m.group(2)
        if not path.endswith('.js'):
            maps[path] = mod_id
    return maps


def extract_module_exports(js_content):
    """Extract all module.exports = {...} blocks."""
    modules = {}
    # Match both quoted and unquoted module IDs
    pattern = r'(?:"|)([0-9a-f]{2,5})(?:"|):function\(\w+,\w+\)\{\w+\.exports='
    for m in re.finditer(pattern, js_content):
        mod_id = m.group(1)
        start = m.end()
        depth = 0
        i = start
        in_string = False
        escape = False
        quote_char = None
        while i < len(js_content):
            c = js_content[i]
            if escape:
                escape = False
                i += 1
                continue
            if c == '\\':
                escape = True
                i += 1
                continue
            if in_string:
                if c == quote_char:
                    in_string = False
                i += 1
                continue
            if c in ('"', "'", '`'):
                in_string = True
                quote_char = c
                i += 1
                continue
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    modules[mod_id] = js_content[start:i+1]
                    break
            i += 1
    return modules


def parse_js_object(obj_str):
    """Parse a JS object literal into a Python dict using regex extraction."""
    result = {}
    s = obj_str.strip()

    # title
    m = re.search(r'title\s*:\s*"([^"]*)"', s)
    if m:
        result['title'] = m.group(1)

    # desc (string)
    m = re.search(r'desc\s*:\s*"([^"]*)"', s)
    if m:
        result['desc'] = m.group(1)

    # desc (array)
    m = re.search(r'desc\s*:\s*\[', s)
    if m:
        start = m.end() - 1
        arr_str = extract_balanced(s, start, '[', ']')
        if arr_str:
            result['desc_array'] = extract_string_array(arr_str)

    # url
    m = re.search(r'url\s*:\s*"([^"]*)"', s)
    if m:
        result['url'] = m.group(1)

    # method
    m = re.search(r'method\s*:\s*"([^"]*)"', s)
    if m:
        result['method'] = m.group(1)

    # code (response example) - can be single or double quoted
    m = re.search(r"""code\s*:\s*(['"])""", s)
    if m:
        quote = m.group(1)
        end = find_unescaped_quote(s, m.end(), quote)
        if end > 0:
            result['code'] = s[m.end():end]

    # tradeInfo
    m = re.search(r"""tradeInfo\s*:\s*(['"])""", s)
    if m:
        quote = m.group(1)
        end = find_unescaped_quote(s, m.end(), quote)
        if end > 0:
            result['tradeInfo'] = s[m.end():end]

    # remark
    m = re.search(r"""remark\s*:\s*(['"])""", s)
    if m:
        quote = m.group(1)
        end = find_unescaped_quote(s, m.end(), quote)
        if end > 0:
            result['remark'] = s[m.end():end]

    # requestParams
    m = re.search(r'requestParams\s*:\s*\[', s)
    if m:
        arr_str = extract_balanced(s, m.end()-1, '[', ']')
        if arr_str:
            result['requestParams'] = parse_param_array(arr_str)

    # returnParams
    m = re.search(r'returnParams\s*:\s*\[', s)
    if m:
        arr_str = extract_balanced(s, m.end()-1, '[', ']')
        if arr_str:
            result['returnParams'] = parse_param_array(arr_str)

    # info (error codes, models, fee standards)
    m = re.search(r'info\s*:\s*\[', s)
    if m:
        arr_str = extract_balanced(s, m.end()-1, '[', ']')
        if arr_str:
            result['info'] = parse_param_array(arr_str)

    return result


def extract_string_array(arr_str):
    strings = []
    for m in re.finditer(r"""(['"])(.*?)\1""", arr_str):
        val = m.group(2)
        if len(val) > 2:
            strings.append(val)
    return strings


def parse_param_array(arr_str):
    params = []
    i = 0
    while i < len(arr_str):
        if arr_str[i] == '{':
            obj_str = extract_balanced(arr_str, i, '{', '}')
            if obj_str:
                param = parse_param_object(obj_str)
                if param:
                    params.append(param)
                i += len(obj_str)
            else:
                i += 1
        else:
            i += 1
    return params


def parse_param_object(obj_str):
    param = {}
    for key_pattern, key_name in [
        (r'(?:Name|name)', 'name'),
        (r'(?:Required|required|isSelected)', 'required'),
        (r'(?:Type|type|typ)', 'type'),
        (r'(?:Desc|desc|comment)', 'desc'),
        (r'(?:Method|method)', 'method'),
        (r'(?:IsDefault|isDefault)', 'default'),
        (r'origin_price', 'origin_price'),
        (r'(?<!origin_)price', 'price'),
        (r'regular', 'regular'),
    ]:
        m = re.search(key_pattern + r"""\s*:\s*(['"])(.*?)\1""", obj_str)
        if m:
            param[key_name] = m.group(2)

    # Handle .concat() in desc
    if 'desc' not in param:
        m = re.search(r"""(?:Desc|desc)\s*:\s*"([^"]*)"\s*\.concat\(\s*"([^"]*)"\s*\)""", obj_str)
        if m:
            param['desc'] = m.group(1) + m.group(2)

    # tradeInfo in push param objects
    m = re.search(r"""tradeInfo\s*:\s*(['"])""", obj_str)
    if m:
        quote = m.group(1)
        end = find_unescaped_quote(obj_str, m.end(), quote)
        if end > 0:
            param['tradeInfo'] = obj_str[m.end():end]

    return param if param else None


# --- Markdown formatting ---

def format_api_markdown(api_data, service_name):
    lines = []
    title = api_data.get('title', 'Unknown')
    lines.append(f"## {title}")
    lines.append("")

    desc = api_data.get('desc', '')
    if desc:
        lines.append(f"**简要描述：** {strip_html(desc)}")
        lines.append("")

    desc_array = api_data.get('desc_array', [])
    if desc_array:
        for d in desc_array:
            lines.append(f"- {strip_html(d)}")
        lines.append("")

    url = api_data.get('url', '')
    if url:
        lines.append(f"**请求URL：** `{url}`")
        lines.append("")

    method = api_data.get('method', '')
    if method:
        lines.append(f"**请求方式：** {method}")
        lines.append("")

    params = api_data.get('requestParams', [])
    if params:
        lines.append("**请求参数：**")
        lines.append("")
        lines.append("| 参数名 | 必选 | 类型 | 说明 |")
        lines.append("|--------|------|------|------|")
        for p in params:
            name = p.get('name', '')
            required = p.get('required', '')
            ptype = p.get('type', '')
            desc_text = strip_html(p.get('desc', ''))
            method_field = p.get('method', '')
            if method_field:
                desc_text = f"[{method_field}] {desc_text}"
            # Replace newlines in table cells
            desc_text = desc_text.replace('\n', ' ')
            lines.append(f"| {name} | {required} | {ptype} | {desc_text} |")
        lines.append("")

    # Push message example (tradeInfo)
    trade_info = api_data.get('tradeInfo', '')
    if not trade_info:
        for p in api_data.get('requestParams', []):
            if p.get('tradeInfo'):
                trade_info = p['tradeInfo']
                break
    if trade_info:
        lines.append("**推送消息示例：**")
        lines.append("")
        lines.append("```json")
        lines.append(clean_json_example(trade_info))
        lines.append("```")
        lines.append("")

    # Response example
    code = api_data.get('code', '')
    if code:
        lines.append("**返回示例：**")
        lines.append("")
        lines.append("```json")
        lines.append(clean_json_example(code))
        lines.append("```")
        lines.append("")

    # Return params
    ret_params = api_data.get('returnParams', [])
    if ret_params and any(p.get('name') for p in ret_params):
        lines.append("**返回参数说明：**")
        lines.append("")
        lines.append("| 参数名 | 类型 | 说明 |")
        lines.append("|--------|------|------|")
        for p in ret_params:
            name = p.get('name', '')
            ptype = p.get('type', '')
            desc_text = strip_html(p.get('desc', '')).replace('\n', ' ')
            lines.append(f"| {name} | {ptype} | {desc_text} |")
        lines.append("")

    remark = api_data.get('remark', '')
    if remark and remark.strip() and remark.strip() != '无':
        lines.append(f"**备注：** {strip_html(remark)}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return '\n'.join(lines)


def format_error_codes_markdown(info_list):
    lines = []
    lines.append("# 错误代码")
    lines.append("")
    lines.append("| 错误码 | 说明 |")
    lines.append("|--------|------|")
    for item in info_list:
        code = item.get('name', '')
        comment = strip_html(item.get('desc', item.get('comment', ''))).replace('\n', ' ')
        lines.append(f"| {code} | {comment} |")
    lines.append("")
    return '\n'.join(lines)


def format_fee_standard_markdown(info_list):
    lines = []
    lines.append("# 收费规则")
    lines.append("")
    lines.append("| 类型 | 原价 (元/次) | 现价 (元/次) | 计费规则 |")
    lines.append("|------|-------------|-------------|----------|")
    for item in info_list:
        name = item.get('name', '')
        origin = item.get('origin_price', '')
        price = item.get('price', '')
        regular = item.get('regular', '')
        lines.append(f"| {name} | {origin} | {price} | {regular} |")
    lines.append("")
    return '\n'.join(lines)


def format_model_markdown(model_data):
    lines = []
    title = model_data.get('title', 'Unknown')
    desc = model_data.get('desc', '')
    lines.append(f"## {title}")
    if desc:
        lines.append(f"\n{strip_html(desc)}")
    lines.append("")

    info = model_data.get('info', [])
    if info:
        lines.append("| 字段名 | 类型 | 默认值 | 说明 |")
        lines.append("|--------|------|--------|------|")
        for item in info:
            name = item.get('name', '')
            ptype = item.get('type', '')
            default = item.get('default', '')
            desc_text = strip_html(item.get('desc', '')).replace('\n', ' ')
            lines.append(f"| {name} | {ptype} | {default} | {desc_text} |")
        lines.append("")

    remark = model_data.get('remark', '')
    if remark and remark.strip() and remark.strip() != '无':
        lines.append(f"**备注：** {strip_html(remark)}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return '\n'.join(lines)


# --- Guide extraction ---

def build_guide_markdown(js_content, service_name):
    """Build guide markdown from a Vue component render function."""
    display_name = SERVICE_NAMES.get(service_name, service_name)
    lines = [f"# {display_name} - 接入指南", ""]

    # Extract all text nodes with their positions
    # Support both e._v() and a._v() patterns (different variable names in different chunks)
    parts = []
    for m in re.finditer(r'\w\._v\(\s*"((?:[^"\\]|\\.)*)"\s*\)', js_content):
        text = m.group(1).replace('\\n', '\n').replace('\\"', '"').replace("\\'", "'").replace('\\t', '\t')
        if text.strip() and len(text.strip()) >= 2:
            parts.append((m.start(), 'text', text.strip()))

    # Find headings
    for m in re.finditer(r'\w\("(h[1-6])"', js_content):
        tag = m.group(1)
        rest = js_content[m.end():m.end()+500]
        tm = re.search(r'\w\._v\(\s*"((?:[^"\\]|\\.)*)"\s*\)', rest)
        if tm:
            text = tm.group(1).replace('\\n', '\n').replace('\\"', '"')
            if text.strip():
                parts.append((m.start(), tag, text.strip()))

    # Find links with href
    for m in re.finditer(r'\w\("a",\{attrs:\{href:([^,}]+)', js_content):
        href_expr = m.group(1).strip()
        if href_expr.startswith('"') and href_expr.endswith('"'):
            href = href_expr[1:-1]
            rest = js_content[m.end():m.end()+300]
            tm = re.search(r'\w\._v\(\s*"((?:[^"\\]|\\.)*)"\s*\)', rest)
            if tm:
                link_text = tm.group(1)
                parts.append((m.start(), 'link', f'[{link_text}]({href})'))

    # Find table data for the guide's parameter tables
    for m in re.finditer(r'tableData\s*:\s*\[', js_content):
        arr_str = extract_balanced(js_content, m.end()-1, '[', ']')
        if arr_str:
            table_params = parse_param_array(arr_str)
            if table_params:
                table_lines = ["| 参数名 | 必选 | 类型 | 说明 |", "|--------|------|------|------|"]
                for p in table_params:
                    name = p.get('name', '')
                    req = p.get('required', '')
                    ptype = p.get('type', '')
                    desc = strip_html(p.get('desc', '')).replace('\n', ' ')
                    table_lines.append(f"| {name} | {req} | {ptype} | {desc} |")
                parts.append((m.start(), 'table', '\n'.join(table_lines)))

    # Find commonParams
    for m in re.finditer(r'commonParams\s*:\s*\[', js_content):
        arr_str = extract_balanced(js_content, m.end()-1, '[', ']')
        if arr_str:
            table_params = parse_param_array(arr_str)
            if table_params:
                table_lines = ["**公共参数：**", "", "| 参数名 | 必选 | 类型 | 说明 |", "|--------|------|------|------|"]
                for p in table_params:
                    name = p.get('name', '')
                    req = p.get('required', '')
                    ptype = p.get('type', '')
                    desc = strip_html(p.get('desc', '')).replace('\n', ' ')
                    table_lines.append(f"| {name} | {req} | {ptype} | {desc} |")
                parts.append((m.start(), 'table', '\n'.join(table_lines)))

    # Find commonHeader
    for m in re.finditer(r'commonHeader\s*:\s*\[', js_content):
        arr_str = extract_balanced(js_content, m.end()-1, '[', ']')
        if arr_str:
            table_params = parse_param_array(arr_str)
            if table_params:
                table_lines = ["**公共Header：**", "", "| 参数名 | 必选 | 类型 | 说明 |", "|--------|------|------|------|"]
                for p in table_params:
                    name = p.get('name', '')
                    req = p.get('required', '')
                    ptype = p.get('type', '')
                    desc = strip_html(p.get('desc', '')).replace('\n', ' ')
                    table_lines.append(f"| {name} | {req} | {ptype} | {desc} |")
                parts.append((m.start(), 'table', '\n'.join(table_lines)))

    # Extract response/code examples from the guide
    for m in re.finditer(r'(?:accessTokenDemo|code)\s*:\s*[\'"]', js_content):
        quote = js_content[m.end()-1]
        end = find_unescaped_quote(js_content, m.end(), quote)
        if end > 0 and (end - m.end()) > 20:
            code_text = js_content[m.end():end]
            code_text = code_text.replace('\\n', '\n').replace('\\t', '\t').replace("\\'", "'").replace('\\"', '"')
            parts.append((m.start(), 'code', code_text.strip()))

    # Extract signCode blocks
    for m in re.finditer(r'signCode\s*:\s*\{', js_content):
        sign_obj = extract_balanced(js_content, m.end()-1, '{', '}')
        if sign_obj:
            for lang, lang_name in [('java', 'Java'), ('"c#"', 'C#'), ('php', 'PHP'), ('python', 'Python')]:
                lm = re.search(lang + r"""\s*:\s*['"]""", sign_obj)
                if lm:
                    quote = sign_obj[lm.end()-1]
                    end = find_unescaped_quote(sign_obj, lm.end(), quote)
                    if end > 0:
                        code = sign_obj[lm.end():end]
                        code = code.replace('\\n', '\n').replace('\\t', '\t').replace("\\'", "'").replace('\\"', '"')
                        parts.append((m.start() + lm.start(), f'signcode_{lang_name}', code.strip()))

    if not parts:
        return None

    parts.sort(key=lambda x: x[0])

    seen_texts = set()
    heading_texts = set()
    # Collect all heading texts first so we can skip duplicates in body
    for pos, tag, text in parts:
        if tag.startswith('h'):
            heading_texts.add(text)

    for pos, tag, text in parts:
        if tag in ('text', 'link'):
            if text in seen_texts:
                continue
            seen_texts.add(text)

        if tag.startswith('h'):
            level = int(tag[1])
            lines.append(f"{'#' * (level + 1)} {text}")
            lines.append("")
        elif tag == 'text':
            # Skip text that is just a duplicate of a heading
            if text in heading_texts:
                continue
            if len(text) > 3:
                lines.append(text)
                lines.append("")
        elif tag == 'link':
            lines.append(text)
            lines.append("")
        elif tag == 'table':
            lines.append(text)
            lines.append("")
        elif tag == 'code':
            lines.append("```")
            lines.append(text)
            lines.append("```")
            lines.append("")
        elif tag.startswith('signcode_'):
            lang_name = tag.split('_', 1)[1]
            lines.append(f"### {lang_name} 签名示例")
            lines.append("")
            lines.append(f"```{lang_name.lower()}")
            lines.append(text)
            lines.append("```")
            lines.append("")

    if len(lines) <= 3:
        return None

    return '\n'.join(lines)


# --- Main ---

def main():
    print("Loading JS files...")
    js_files = load_all_js()
    print(f"  Loaded {len(js_files)} files")

    with open(ROUTE_MAP, 'r') as f:
        route_map = json.load(f)

    print("Extracting module data...")
    # Build module path -> id map from all files
    path_to_id = {}
    for fname, content in js_files.items():
        path_to_id.update(extract_module_map(content))

    # Extract all module exports
    id_to_raw = {}
    for fname, content in js_files.items():
        id_to_raw.update(extract_module_exports(content))

    # Parse each module
    path_to_data = {}
    for path, mod_id in path_to_id.items():
        if mod_id in id_to_raw:
            data = parse_js_object(id_to_raw[mod_id])
            if data:
                path_to_data[path] = data

    print(f"  {len(path_to_id)} module paths, {len(id_to_raw)} raw modules, {len(path_to_data)} parsed modules")

    # Organize data by service
    api_by_service = {}
    push_by_service = {}
    model_by_service = {}
    error_code_data = None
    fee_standard_data = None

    for path, data in path_to_data.items():
        if path.startswith('./api/'):
            parts = path.replace('./api/', '').split('/')
            prefix = parts[0]
            api_name = parts[-1] if len(parts) > 1 else 'index'
            if api_name == 'index' or api_name == prefix:
                continue  # Skip index modules (they contain config, not API docs)
            services = API_PREFIX_MAP.get(prefix, [])
            for service in services:
                if service not in api_by_service:
                    api_by_service[service] = []
                api_by_service[service].append(data)

        elif path.startswith('./push/'):
            parts = path.replace('./push/', '').split('/')
            prefix = parts[0]
            services = PUSH_PREFIX_MAP.get(prefix, [])
            for service in services:
                if service not in push_by_service:
                    push_by_service[service] = []
                push_by_service[service].append(data)

        elif path.startswith('./model/'):
            for svc in ['alds', 'acs']:
                if svc not in model_by_service:
                    model_by_service[svc] = []
                model_by_service[svc].append(data)

        elif path.startswith('./common/errorCode'):
            error_code_data = data

        elif path.startswith('./common/feeStandrd'):
            fee_standard_data = data

    # Create output directories
    os.makedirs(DOCS_DIR, exist_ok=True)
    all_services = list(route_map['services'].keys())
    for service in all_services:
        os.makedirs(os.path.join(DOCS_DIR, service), exist_ok=True)

    files_written = 0

    # --- Write API docs ---
    print("\nWriting API docs...")
    for service in all_services:
        apis = api_by_service.get(service, [])
        if not apis:
            continue
        display_name = SERVICE_NAMES.get(service, service)
        lines = [
            f"# {display_name} - API 接口文档",
            "",
            f"**请求域名：** `https://gw-api.agiso.com/{service}/`",
            "",
            "---",
            "",
        ]
        for api in sorted(apis, key=lambda x: x.get('title', '')):
            lines.append(format_api_markdown(api, service))
        fpath = os.path.join(DOCS_DIR, service, 'api.md')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        files_written += 1
        print(f"  {service}/api.md ({len(apis)} endpoints)")

    # --- Write Push docs ---
    print("\nWriting Push docs...")
    for service in all_services:
        pushes = push_by_service.get(service, [])
        if not pushes:
            continue
        display_name = SERVICE_NAMES.get(service, service)
        lines = [
            f"# {display_name} - 推送通知",
            "",
            "推送的签名请务必验证，以验证数据来源的合法性。",
            "推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。",
            "",
            "---",
            "",
        ]
        for push in sorted(pushes, key=lambda x: x.get('title', '')):
            lines.append(format_api_markdown(push, service))
        fpath = os.path.join(DOCS_DIR, service, 'push.md')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        files_written += 1
        print(f"  {service}/push.md ({len(pushes)} notifications)")

    # --- Write Error Code docs ---
    if error_code_data:
        error_info = error_code_data.get('info', [])
        if error_info:
            error_md = format_error_codes_markdown(error_info)
            print("\nWriting Error Code docs...")
            for service in all_services:
                routes = route_map['services'].get(service, [])
                if any(r['path'].endswith('/errorCode') for r in routes):
                    fpath = os.path.join(DOCS_DIR, service, 'errorCode.md')
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(error_md)
                    files_written += 1
            print(f"  Written to all applicable services")

    # --- Write Fee Standard docs ---
    if fee_standard_data:
        fee_info = fee_standard_data.get('info', [])
        if fee_info:
            fee_md = format_fee_standard_markdown(fee_info)
            print("\nWriting Fee Standard docs...")
            for service in all_services:
                routes = route_map['services'].get(service, [])
                if any(r['path'].endswith('/feeStandrd') for r in routes):
                    fpath = os.path.join(DOCS_DIR, service, 'feeStandrd.md')
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(fee_md)
                    files_written += 1
            print(f"  Written to all applicable services")

    # --- Write Model docs ---
    print("\nWriting Model docs...")
    for service in all_services:
        models = model_by_service.get(service, [])
        if not models:
            continue
        display_name = SERVICE_NAMES.get(service, service)
        lines = [f"# {display_name} - 数据类型", ""]
        for model in sorted(models, key=lambda x: x.get('title', '')):
            lines.append(format_model_markdown(model))
        fpath = os.path.join(DOCS_DIR, service, 'model.md')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        files_written += 1
        print(f"  {service}/model.md ({len(models)} models)")

    # --- Write Guide docs ---
    print("\nWriting Guide docs...")
    for service, chunk_prefix in GUIDE_CHUNK_MAP.items():
        # Find the matching JS file
        chunk_file = None
        for fname in js_files:
            if fname.startswith(chunk_prefix):
                chunk_file = fname
                break
        if not chunk_file:
            print(f"  WARNING: No chunk found for {service} guide ({chunk_prefix})")
            continue

        md = build_guide_markdown(js_files[chunk_file], service)
        if md and len(md) > 100:
            fpath = os.path.join(DOCS_DIR, service, 'guide.md')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(md)
            files_written += 1
            print(f"  {service}/guide.md")
        else:
            print(f"  WARNING: Guide content too short for {service}")

    # --- Write SignDemo docs ---
    print("\nWriting SignDemo docs...")
    # Search ALL JS files for signCode blocks (they may be in any chunk)
    sign_code_blocks = {}
    # Also extract the sign algorithm code examples from guide chunks
    guide_sign_code = {}
    for fname, content in js_files.items():
        # Look for signCode data objects
        for m in re.finditer(r'signCode\s*:\s*\{', content):
            sign_obj = extract_balanced(content, m.end()-1, '{', '}')
            if sign_obj:
                for lang, lang_name in [('java', 'Java'), ('"c#"', 'C#'), ('php', 'PHP'), ('python', 'Python')]:
                    lm = re.search(lang + r"""\s*:\s*['"]""", sign_obj)
                    if lm and lang_name not in sign_code_blocks:
                        quote = sign_obj[lm.end()-1]
                        end = find_unescaped_quote(sign_obj, lm.end(), quote)
                        if end > 0:
                            code = sign_obj[lm.end():end]
                            code = code.replace('\\n', '\n').replace('\\t', '\t').replace("\\'", "'").replace('\\"', '"')
                            sign_code_blocks[lang_name] = code.strip()

        # Also look for code:{java:'...',c#:'...',php:'...'} pattern (API/push demo code)
        for m in re.finditer(r'(?:^|,\s*)code\s*:\s*\{', content):
            code_obj = extract_balanced(content, m.end()-1, '{', '}')
            if code_obj and len(code_obj) > 200:
                for lang, lang_name in [('java', 'Java'), ('"c#"', 'C#'), ('php', 'PHP')]:
                    lm = re.search(lang + r"""\s*:\s*['"]""", code_obj)
                    if lm and lang_name not in sign_code_blocks:
                        quote = code_obj[lm.end()-1]
                        end = find_unescaped_quote(code_obj, lm.end(), quote)
                        if end > 0:
                            code = code_obj[lm.end():end]
                            code = code.replace('\\n', '\n').replace('\\t', '\t').replace("\\'", "'").replace('\\"', '"')
                            if len(code) > 50 and ('sign' in code.lower() or 'Sign' in code):
                                sign_code_blocks[lang_name] = code.strip()

    # No additional search needed after comprehensive extraction above
            sign_code_blocks[lang] = code

    for service in all_services:
        routes = route_map['services'].get(service, [])
        if not any(r['path'].endswith('/signDemo') for r in routes):
            continue

        display_name = SERVICE_NAMES.get(service, service)
        lines = [
            f"# {display_name} - 签名算法",
            "",
            "## 签名说明",
            "",
            "将所有API输入参数（除了sign参数），按参数名的字典序排序，将参数名和参数值依次拼接成一个字符串，"
            "在字符串的头部和尾部分别拼接上AppSecret，然后对整个字符串进行MD5加密（32位），即为sign的值。",
            "",
            "**步骤：**",
            "1. 将请求参数按参数名的字典序排序",
            "2. 将参数名和参数值拼接成一个字符串",
            "3. 在字符串前后添加AppSecret",
            "4. 对拼接后的字符串进行MD5加密（32位，不区分大小写）",
            "",
            "**示例：**",
            "- 参数: appId=xxx, timestamp=1468476350, token=yyy",
            "- 排序后拼接: AppSecret + appIdxxx + timestamp1468476350 + tokenyyy + AppSecret",
            "- 对结果进行MD5加密得到sign值",
            "",
        ]

        if sign_code_blocks:
            lines.append("## 示例代码")
            lines.append("")
            for lang_name, code in sign_code_blocks.items():
                lines.append(f"### {lang_name}")
                lines.append("")
                lines.append(f"```{lang_name.lower()}")
                lines.append(code)
                lines.append("```")
                lines.append("")

        fpath = os.path.join(DOCS_DIR, service, 'signDemo.md')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        files_written += 1
    print(f"  Written to all applicable services")

    # --- Write FAQ docs ---
    print("\nWriting FAQ docs...")
    for service in all_services:
        routes = route_map['services'].get(service, [])
        if not any(r['path'].endswith('/faq') for r in routes):
            continue
        display_name = SERVICE_NAMES.get(service, service)
        fpath = os.path.join(DOCS_DIR, service, 'faq.md')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(f"# {display_name} - 常见问题\n\n")
            f.write("## Q: AccessToken过期了怎么办？\n\n")
            f.write("A: AccessToken的有效期和用户购买Agiso软件的使用时间一致。如果用户续费，AccessToken的有效期会延长。如过期，需要用户重新授权。\n\n")
            f.write("## Q: 调用接口返回错误怎么处理？\n\n")
            f.write("A: 请参考错误代码页面，根据返回的Error_Code查看具体错误原因。常见错误包括：AccessToken无效(1)、签名验证失败(4)、参数错误(5)等。\n\n")
            f.write("## Q: 推送消息如何验证签名？\n\n")
            f.write("A: 将json和timestamp参数名和参数值组合起来（json在前，timestamp在后），然后前后添加AppSecret，再进行MD5加密，与sign参数比较验证。\n\n")
            f.write("## Q: 推送消息可能重复吗？\n\n")
            f.write("A: 是的，推送时有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。\n\n")
        files_written += 1
    print(f"  Written to all applicable services")

    # --- Write Supplier Demo ---
    print("\nWriting Supplier demo...")
    for fname, content in js_files.items():
        if 'SupplierDemo' not in content:
            continue
        m = re.search(r'signCode\s*:\s*\{', content)
        if not m:
            continue
        sign_obj = extract_balanced(content, m.end()-1, '{', '}')
        if not sign_obj:
            continue

        lines = ["# 供应商 (Supplier) - 示例代码", ""]
        for lang, lang_name in [('java', 'Java'), ('"c#"', 'C#')]:
            lm = re.search(lang + r"""\s*:\s*['"]""", sign_obj)
            if lm:
                quote = sign_obj[lm.end()-1]
                end = find_unescaped_quote(sign_obj, lm.end(), quote)
                if end > 0:
                    code = sign_obj[lm.end():end]
                    code = code.replace('\\n', '\n').replace('\\t', '\t').replace("\\'", "'").replace('\\"', '"')
                    lines.append(f"## {lang_name}")
                    lines.append("")
                    lines.append(f"```{lang_name.lower()}")
                    lines.append(code.strip())
                    lines.append("```")
                    lines.append("")

        if len(lines) > 3:
            fpath = os.path.join(DOCS_DIR, 'supplier', 'demo.md')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            files_written += 1
            print(f"  supplier/demo.md")
        break

    # --- Write README index ---
    print("\nWriting README...")
    readme = ["# 易店长开放平台 (Agiso Open Platform) API 文档", "",
              "文档来源: https://open.agiso.com/document/", "",
              "---", ""]

    for service in all_services:
        display_name = SERVICE_NAMES.get(service, service)
        readme.append(f"## {display_name}")
        readme.append("")
        routes = route_map['services'].get(service, [])

        # Add guide first if it exists
        guide_path = os.path.join(DOCS_DIR, service, 'guide.md')
        if os.path.exists(guide_path):
            has_guide_route = any(r['path'].endswith('/guide') for r in routes)
            if not has_guide_route:
                readme.append(f"- [接入指南](./{service}/guide.md)")

        for route in routes:
            page = route['path'].split('/')[-1]
            title = route['title']
            fpath = os.path.join(DOCS_DIR, service, f'{page}.md')
            if os.path.exists(fpath):
                readme.append(f"- [{title}](./{service}/{page}.md)")
            else:
                readme.append(f"- {title}")
        readme.append("")

    with open(os.path.join(DOCS_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(readme))
    files_written += 1

    print(f"\nDone! {files_written} files written to {DOCS_DIR}")
    print("\n=== Summary ===")
    for service in all_services:
        svc_dir = os.path.join(DOCS_DIR, service)
        if os.path.exists(svc_dir):
            svc_files = sorted(os.listdir(svc_dir))
            print(f"  {service}: {', '.join(svc_files)}")


if __name__ == '__main__':
    main()
