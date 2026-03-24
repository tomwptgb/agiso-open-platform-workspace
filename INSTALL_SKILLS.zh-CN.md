# Install In AI Clients

[English](./INSTALL_SKILLS.md) | [简体中文](./INSTALL_SKILLS.zh-CN.md)

本仓库包含一个可安装的 skill：

- skill 名称：`agiso-open-platform`
- 仓库路径：`skill/agiso-open-platform/`
- 主入口文件：`skill/agiso-open-platform/SKILL.md`

## 第一性原理规则

本仓库只应记录与本项目直接相关且相对稳定的事实：

- 预期支持哪些客户端
- skill 在本仓库中的位置
- 每个客户端的最短安装路径
- 当平台细节变化时，应该阅读哪份官方指南

本仓库不应该复制冗长且变化频繁的平台说明书。

## 兼容性

当前记录的目标客户端：

- `Codex`：可安装，且已在本仓库工作流中验证
- `Claude Code`：由 Claude Code 官方的 Skills 文件系统发现模型支持
- `Claude`：可通过自定义 skill 上传使用，但受账号能力和设置限制

## 安装到 Codex

推荐方式：

```bash
python3 /home/ubuntu/snap/codex/35/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo tomwptgb/agiso-open-platform-workspace \
  --path skill/agiso-open-platform
```

安装完成后，重启 Codex。

本地安装的替代方式：

```bash
mkdir -p "$HOME/skills"
cp -R /path/to/agiso-open-platform-workspace/skill/agiso-open-platform "$HOME/skills/"
```

官方参考：

- OpenAI skills catalog：<https://github.com/openai/skills>

## 安装到 Claude Code

Claude Code 会从文件系统自动发现 skills。常见位置有两个：

- 个人级：`~/.claude/skills/agiso-open-platform/`
- 项目级：`.claude/skills/agiso-open-platform/`

个人级安装示例：

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/agiso-open-platform-workspace/skill/agiso-open-platform ~/.claude/skills/
```

项目级安装示例：

```bash
mkdir -p .claude/skills
cp -R /path/to/agiso-open-platform-workspace/skill/agiso-open-platform .claude/skills/
```

复制完成后，重启 Claude Code。

官方参考：

- Claude Code Skills 文档：<https://docs.claude.com/en/docs/claude-code/skills>

## 安装到 Claude

Claude 使用“上传自定义 skill”，而不是文件系统自动发现。

最小流程：

1. 将 `skill/agiso-open-platform/` 打包成 ZIP 文件。
2. 在 Claude 中进入 `Customize > Skills`。
3. 上传这个 ZIP 文件。
4. 如有需要，启用该 skill。

重要前提：

- 你的 Claude 计划需要支持 Skills
- 必须启用 code execution
- 对于 Team 或 Enterprise，组织设置可能会控制访问权限

官方参考：

- Use Skills in Claude：<https://support.claude.com/en/articles/12512180-use-skills-in-claude>
- What are Skills?：<https://support.claude.com/en/articles/12512176-what-are-skills>

## 应该先读什么

如果你只想走最短路径：

- Codex 用户：直接使用上面的 GitHub 安装命令
- Claude Code 用户：直接把 skill 目录复制到 `~/.claude/skills/`
- Claude 用户：先阅读官方上传指南

## 维护规则

当客户端安装方式变化时，优先只更新：

- 本文中的兼容性说明
- 与本项目相关的最短安装路径
- 官方参考链接

不要把本仓库变成供应商文档的镜像副本。
