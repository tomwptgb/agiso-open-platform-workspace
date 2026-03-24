# Service Matrix

This file maps each service to its document coverage and likely task type.

## Shared Document Pattern

Most services expose:

- `guide.md`
- `api.md`
- `push.md`
- `errorCode.md`
- `feeStandrd.md`
- `signDemo.md`
- `faq.md`

Only some services also expose `model.md`.

## Coverage By Service

| Service | Business area | Push docs | Model docs | Notes |
|---|---|---:|---:|---|
| `open` | 平台公共接口与托管服务 | No | No | Start here for auth, hosted app lifecycle, tokens |
| `alds` | 淘宝自动发货 | Yes | Yes | Canonical auto-delivery reference set |
| `acs` | 淘宝采购 | Yes | Yes | Procurement-specific workflows and models |
| `acpr` | 卡券自动充值 | Yes | No | Card recharge and 91kami-related flows |
| `print` | 云打印/代发 | Yes | No | Printing and dispatch callbacks |
| `supplier` | 供应商接口 | N/A | N/A | Uses guide, demo, and signing docs instead |
| `aldsDoudian` | 抖店自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsIdle` | 闲鱼自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsJd` | 京东自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsKwai` | 快手自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsPdd` | 拼多多自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsWeidian` | 微店自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsWxVideoShop` | 微信小店自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsXhs` | 小红书自动发货 | Yes | No | Marketplace variant of auto-delivery |
| `aldsYouzan` | 有赞自动发货 | Yes | No | Marketplace variant of auto-delivery |

## Gateway Hints

Derived from `../knowledge-base/extracted/crawl_summary.json`:

- `alds` gateway: `https://gw-api.agiso.com/alds`
- `acs` gateway: `https://gw-api.agiso.com/acs`
- `print` gateway: `https://ebprint.agiso.com`
- `acpr` gateway: `https://mai.91kami.com`
- other services often follow `https://gw-api.agiso.com/{service_name}`

## Selection Hints

- If the user says "开放平台" or asks about merchant auth, start with `open`
- If the user says "自动发货" plus a marketplace name, choose the matching `alds*` service
- If the user asks for supplier-side server code or OAuth-like code exchange, choose `supplier`
- If the user asks for card recharge or stock-in, consider `acpr`
- If the user asks for procurement or purchase orders, consider `acs`

## Structural Inference

The repeated file layout suggests Agiso is organized around a stable documentation schema:

- onboarding
- endpoint catalog
- callback catalog
- failure reference
- pricing reference
- signing reference
- operator FAQ

That schema should shape generated outputs and tool design.
