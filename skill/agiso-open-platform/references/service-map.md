# Service Map

Use this file to decide which Agiso document set to open first.

## Core Services

| Service | Meaning | Main docs |
|---|---|---|
| `open` | 开放平台公共接口 | `../../../knowledge-base/docs/open/guide.md`, `../../../knowledge-base/docs/open/api.md`, `../../../knowledge-base/docs/open/signDemo.md`, `../../../knowledge-base/docs/open/errorCode.md` |
| `alds` | 淘宝自动发货 | `../../../knowledge-base/docs/alds/api.md`, `../../../knowledge-base/docs/alds/push.md`, `../../../knowledge-base/docs/alds/model.md`, `../../../knowledge-base/docs/alds/signDemo.md` |
| `acs` | 淘宝采购 | `../../../knowledge-base/docs/acs/api.md`, `../../../knowledge-base/docs/acs/push.md`, `../../../knowledge-base/docs/acs/model.md`, `../../../knowledge-base/docs/acs/signDemo.md` |
| `acpr` | 卡券自动充值 | `../../../knowledge-base/docs/acpr/api.md`, `../../../knowledge-base/docs/acpr/push.md`, `../../../knowledge-base/docs/acpr/signDemo.md` |
| `print` | 云打印/代发 | `../../../knowledge-base/docs/print/api.md`, `../../../knowledge-base/docs/print/push.md`, `../../../knowledge-base/docs/print/signDemo.md` |
| `supplier` | 供应商接口 | `../../../knowledge-base/docs/supplier/guide.md`, `../../../knowledge-base/docs/supplier/demo.md`, `../../../knowledge-base/docs/supplier/signDemo.md` |

## Marketplace Variants

These mostly follow the same document shape: `guide`, `api`, `push`, `errorCode`, `feeStandrd`, `signDemo`, `faq`.

| Service | Marketplace |
|---|---|
| `aldsDoudian` | 抖店 |
| `aldsIdle` | 闲鱼 |
| `aldsJd` | 京东 |
| `aldsKwai` | 快手 |
| `aldsPdd` | 拼多多 |
| `aldsWeidian` | 微店 |
| `aldsWxVideoShop` | 微信小店 |
| `aldsXhs` | 小红书 |
| `aldsYouzan` | 有赞 |

Open the matching files under `../../../knowledge-base/docs/<service>/`.

## Reverse-Engineered Navigation Aids

- `../../../knowledge-base/docs/README.md`: human-readable table of contents across all services
- `../../../knowledge-base/extracted/crawl_summary.json`: service list, gateway URLs, platform summary
- `../../../knowledge-base/extracted/route_map.json`: route-to-title map for each service
- `../../../knowledge-base/extracted/api_docs_index.json`: extracted endpoint and push topic index

## Selection Heuristics

- If the task mentions merchant authorization, token exchange, or hosted app lifecycle, start with `open`
- If the task mentions auto-delivery on a named marketplace, start with the corresponding `alds*` service
- If the task mentions procurement, start with `acs`
- If the task mentions card recharge or 91kami, start with `acpr`
- If the task mentions printer integration or printing callbacks, start with `print`
- If the task is supplier-side code or sample integration, start with `supplier`
