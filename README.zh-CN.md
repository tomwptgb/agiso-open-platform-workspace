# agiso-open-platform-workspace

[English](./README.md) | [简体中文](./README.zh-CN.md)

这是一个面向 Agiso Open Platform 集成 skill 及其本地证据库的开源工作区。

安装入口：

- [Install in AI clients](./INSTALL_SKILLS.md)
- [安装到 AI 客户端](./INSTALL_SKILLS.zh-CN.md)

本仓库围绕两个边界组织：

- `knowledge-base/`：提取后的源材料、派生索引，以及用于再生成它们的流水线
- `skill/agiso-open-platform/`：面向 Codex 的 skill、参考材料和读取本地知识库的辅助脚本

## 仓库用途

当你需要一个本地可检查、可复用的工作区来完成以下工作时，可以使用本仓库：

- 探索 Agiso Open Platform 的服务覆盖范围
- 阅读提取后的 Agiso API 和回调文档
- 生成签名请求示例和回调处理器
- 将整个工作流打包为可复用的 Codex skill

## 仓库结构

```text
.
├── knowledge-base/
│   ├── docs/
│   ├── extracted/
│   ├── raw_js/
│   └── extract_docs.py
├── skill/
│   ├── README.md
│   └── agiso-open-platform/
│       ├── SKILL.md
│       ├── agents/
│       ├── references/
│       └── scripts/
└── README.md
```

## 快速开始

1. 查看 skill 入口文件 `skill/agiso-open-platform/SKILL.md`。
2. 如果你需要把业务流程映射到正确的 Agiso 服务，先读 `skill/agiso-open-platform/references/service-map.md`。
3. 对于签名、文档搜索、服务定位等确定性任务，优先使用 `skill/agiso-open-platform/scripts/` 下的辅助脚本。
4. 将 `knowledge-base/` 视为 skill 读取的本地证据层。
5. 如果你想把这个 skill 安装到 Codex、Claude Code 或 Claude，请先阅读 `INSTALL_SKILLS.md`。

## Skill 与路径约定

仓库名为 `agiso-open-platform-workspace`。  
skill 标识和目录名保持为 `agiso-open-platform`。

skill 脚本会通过以下任一来源解析知识库路径：

1. `AGISO_KNOWLEDGE_BASE_ROOT`
2. `<repo>/knowledge-base`

这样可以去掉之前隐式的相对路径耦合，并提高 skill 在不同克隆环境中的可移植性。

## 开源范围

本仓库中的原创代码、仓库级文档和 skill 材料采用 MIT License 发布，见 `LICENSE`。

需要特别注意的边界：

- `knowledge-base/docs/`、`knowledge-base/extracted/` 和 `knowledge-base/raw_js/` 包含来自 Agiso 公共属性的第三方材料或派生材料。
- 除非上游权利方明确允许，否则这些材料并不会自动落入本仓库的 MIT 许可范围。
- 如果你计划公开再分发本仓库，请先审查这些材料的来源和权利边界。

更具体的说明见 `THIRD_PARTY_NOTICES.md`。

## 贡献

提交 Pull Request 前，请先阅读 `CONTRIBUTING.md`。  
仓库提供了适用于公开协作的社区健康文件：

- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `SUPPORT.md`

## 维护者发布前检查

在公开发布变更前，请确认：

1. 工作区和提交历史中不存在密钥、令牌或私有凭据。
2. 已重新检查第三方 Agiso 材料是否允许再分发。
3. skill 指令与打包脚本、参考材料保持一致。
4. 打标签或推送前 `git status` 为干净状态。
