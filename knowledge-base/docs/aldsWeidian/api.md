# 微店自动发货 (AldsWeidian) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsWeidian/`

---

## 删除商家授权

**简要描述：** 开发者自行删除对商家的授权

**请求URL：** `/Sys/TokenDelete`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
|  |  |  | 在公共Header处，上传相应Authorization参数，就能删除相应的商家 |

**返回示例：**

```json
{
    "IsSuccess": false,
    "Error_Msg": "删除失败",
  }
```

---
