# Contributing

[English](./CONTRIBUTING.md) | [简体中文](./CONTRIBUTING.zh-CN.md)

感谢你的贡献。

## 开始之前

- 先阅读 `README.md`，了解仓库结构和许可边界。
- 将 `knowledge-base/` 视为带有来源约束的证据层。
- 让每次改动都保持明确范围，并解释其必要性。

## 贡献规则

- 优先提交聚焦的小型 Pull Request，而不是大范围重写。
- 不要提交密钥、令牌或私有客户数据。
- 如果不能确认第三方材料可再分发，就不要提交。
- 保持 skill 指令、参考材料和脚本之间的一致性。
- 当工作流或边界发生变化时，同步更新仓库文档。

## Skill 相关改动

编辑 `skill/agiso-open-platform/` 时：

- 保持 `SKILL.md` 简洁、以过程为导向
- 详细材料尽量下沉到 `references/`，避免把 `SKILL.md` 写得过重
- 只有在确定性复用明显优于纯文字说明时，才新增脚本
- 保持 `agents/openai.yaml` 与 skill 实际用途一致

## Pull Request 检查清单

- 这次改动有清晰的原因和范围。
- 仓库文档仍然与实际情况一致。
- 没有新增任何密钥。
- 已考虑许可和来源影响。
- 提交完成后 `git status` 为干净状态。
