# 打印 (Print) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/print/`

---

## 关闭打印订单

**简要描述：** 关闭打印订单

**请求URL：** `/PrintTrade/Close`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |
| recycleWaybillCode | 否 | boolen | 是否回收电子面单，默认false |

**返回示例：**

```json
{
    "IsSuccess":true,
    "Data":{
        "Tids":[
            "test002"
        ]
    },
    "Error_Code":0,
    "Error_Msg":"",
    "AllowRetry":null,
    "RequestId":"20201027142251106"
  }
```

---

## 分配订单给代发供应商

**简要描述：** 分配订单给代发供应商

**请求URL：** `/PrintTrade/AssignedToSupplier`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |
| supplierId | 是 | String | 代发供应商Id |
| goodsJson | 否 | String | 商品列表 (要修改商品列表才传,json序列化成字符串后再传)   [{       "GoodsId":"a135465", // 商品id (非必须)       "Name":"风衣",       // 商品名称       "SkuName":"XXL",     // 商品SKU名称 (非必须)       "OutIid":"fy",       // 商品编码 (非必须)       "SkuOutIid":"fy-xxl",// 商品SKU编码 (非必须)       "Num":2,             // 数量       "Weigth":1.2         // 重量   }] |
| senderInfoJson | 否 | String | 指定打印电子单时使用的发件人信息 (json序列化成字符串后再传)   {       "Name":"黄小姐",       "Mobile":"13912346789"   } |
| waybillCodeChangeNeedToPush | 否 | boolen | 当运单号变动时是否推送，默认false |
| payTime | 否 | string | 付款时间，如: 2012-12-17 18:54:00 |

**返回示例：**

```json
{
        "IsSuccess":true,
        "Error_Code":0,
        "Error_Msg":"",
    }
```

---

## 创建线下订单

**简要描述：** 创建线下订单

**请求URL：** `/PrintTrade/CreateOfflineTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 否 | String | 订单编号 |
| receiverJson | 是 | String | 收件人信息 (json序列化成字符串后再传) {   "Name":"陈先生",     "Mobile":"18259563258",     "Phone":"0595-86598963",     "Province":"福建省",     "City":"泉州市",     "District":"南安市",     "Town":"",     "Detail":"xx小区x楼xxx" } |
| senderInfoJson | 否 | String | 指定打印电子单时使用的发件人信息 (json序列化成字符串后再传) {     "Name":"黄小姐",     "Mobile":"13912346789" } |
| goodsJson | 否 | String | 商品列表 (json序列化成字符串后再传) [{     "GoodsId":"a135465", // 商品id (非必须)     "Name":"风衣",       // 商品名称     "SkuName":"XXL",     // 商品SKU名称 (非必须)     "OutIid":"fy",       // 商品编码 (非必须)     "SkuOutIid":"fy-xxl",// 商品SKU编码 (非必须)     "Num":2,             // 数量     "Weigth":1.2         // 重量 }] |
| buyerMsg | 否 | String | 买家留言 |
| sellerMsg | 否 | String | 卖家备注 |
| payment | 是 | Number | 订单金额 |
| formPlatform | 否 | Number | 订单来源平台，淘宝：100，天猫：110，拼多多：200，京东：300 |
| waybillCodeChangeNeedToPush | 否 | boolen | 当运单号变动时是否推送，默认false |
| payTime | 否 | string | 付款时间，如: 2012-12-17 18:54:00 |

**返回示例：**

```json
{
      "IsSuccess":true,
      "Error_Code":0,
      "Error_Msg":"",
      "Data":{
        "Tid": "123456789"
      }
  }
```

---

## 将订单退回给分销商

**简要描述：** 将订单退回给分销商

**请求URL：** `/PrintTrade/BackToAgency`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |

**返回示例：**

```json
{
    "IsSuccess":true,
    "Error_Code":0,
    "Error_Msg":"",
    "AllowRetry":null,
    "RequestId":"20201027142251106"
  }
```

---

## 智能解析地址

**简要描述：** 提取文本中的，姓名、电话、省市区、地址、邮编。提取结果的准确度较高，但对于极特殊的文本可能存在提取错误

**请求URL：** `/Utils/ParseAddress`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| text | 是 | String | 地址信息，如：陈先生18112345678江苏省苏州市昆山市花桥镇蓬青东路9000号一单元，000000 |

**返回示例：**

```json
{
    "IsSuccess":true,
    "Data":{
        "Province":"江苏省",
        "City":"苏州市",
        "Area":"昆山市",
        "Detail":"花桥镇蓬青东路9000号一单元",
        "Mobile":"18112345678",
        "Name":"陈先生",
        "PostalCode":"000000"
    },
    "Error_Code":0,
    "Error_Msg":"",
    "AllowRetry":null,
    "RequestId":"20201119143328108"
  }
```

---

## 查询打印订单状态

**简要描述：** 查询打印订单状态

**请求URL：** `/PrintTrade/QueryPrintTradeStatus`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |

**返回示例：**

```json
{
    "IsSuccess":true,
    "Data":{
        "Status": 100, // 订单状态：100：待审核；200：待打单；300：待发货；400：已发货；500：已取消；600：已关闭；
        "IsLock": false, // 是否锁定订单
        "IsMerge": false, // 是否合并订单
        "IsTear": false, // 是否拆分订单
        "HasPrinted": false, // 是否有打印过（有打印过，不管成功失败该值都为true）
        "IsPrintSuccess": false, // 是否打印成功（只有HasPrinted是true时，该值才有意义）
        "HasGetWaybillCode": false, // 是否获取了运单号
    },
    "Error_Code":0,
    "Error_Msg":"",
    "AllowRetry":null,
    "RequestId":"20201027142251106"
  }
```

---

## 查询订单的运单号

**简要描述：** 查询订单通过打单软件获取到的电子面单运单号

**请求URL：** `/PrintTrade/QueryWaybillCode`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |

**返回示例：**

```json
{
      "IsSuccess":true,
      "Data":{
          "ExpressCompanyName":"百世快递",
          "WaybillCode":"YTO123456789",
          "WaybillCodeList":[
            "YTO123456789",
            "YTO123456780"
          ]
      },
      "Error_Code":0,
      "Error_Msg":"",
      "AllowRetry":null,
      "RequestId":"20201014150108088"
  }
```

---

## 检测是否快递停发地区

**简要描述：** 检测该订单的收件地址是否在停发地区

**请求URL：** `/PrintTrade/CheckIsStopDeliveryArea`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |
| waybillAccountId | 是 | String | 电子面单帐号Id |

**返回示例：**

```json
{
        "IsSuccess":true,
        "Error_Code":0,
        "Data":{
          "IsStopDeliveryArea":true, // 是否停发
          "HasSetting":true // 是否设置停发地区
      },
        "Error_Msg":"",
    }
```

---

## 获取供应商身份信息

**简要描述：** 获取当前用户作为供应商的名称和Id

**请求URL：** `/DropShippingSupplier/GetSupplierInfo`

**请求方式：** POST

**返回示例：**

```json
{
    "IsSuccess":true,
    "Error_Code":0,
    "Error_Msg":"",
    "Data":{
        "Id":"c73960ecb355452c8e64c230bd418830",
        "Name":"大橙子一件代发"
    }
}
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Id | string | 供应商id |
| Name | string | 供应商名称 |

---

## 获取用户的代发供应商

**简要描述：** 获取用户账号下的代发供应商信息

**请求URL：** `/DropShippingSupplier/GetMyDropShippingSupplier`

**请求方式：** POST

**返回示例：**

```json
{
        "IsSuccess":true,
        "Error_Code":0,
        "Error_Msg":"",
        "Data":{
            "Suppliers":[
                {
                    "RelationIdNo":3,
                    "SupplierId":"4ce7fad38bdc46e89236d1a5b1af8887",
                    "Name":"Agiso代发",
                    "Status":100,
                    "CreateTime":"2020-09-16T10:45:47"
                }
            ]
        }
    }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| SupplierId | string | 代发供应商id |
| Name | string | 代发供应商名称 |

---

## 获取用户的代销商

**简要描述：** 获取用户的代销商

**请求URL：** `/DropShippingSupplier/GetMyAgencySeller`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| pageNo | 是 | Number |  |
| pageSize | 是 | Number | 最大值不能超过100 |

**返回示例：**

```json
{
        "IsSuccess":true,
        "Error_Code":0,
        "Error_Msg":"",
        "Data":{
            "List":[
                {
                    "RelationIdNo":2,
                    "SellerId":"4ce7fad38bdc46e89236d1a5b1af8887",
                    "Nick":"Agiso",
                    "Status":200,
                    "CreateTime":"2020-09-16T10:21:29"
                }
            ],
            "TotalCount":1
        }
    }
```

---

## 获取订单的运单号

**简要描述：** 获取订单的运单号

**请求URL：** `/PrintTrade/GetWaybillCode`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |
| waybillAccountId | 是 | String | 电子面单帐号Id，在飞流里获取:http://ebprint.agiso.com/#/setting/accounts |
| setSent | 否 | Boolean | 获取面单成功后，是否将该笔订单设置为已发货状态 |
| logisticsSend | 否 | Boolean | 获取面单成功后，是否调用电商平台接口发货 |
| audit | 否 | Boolean | 当为true时，如果订单状态为待审核时，通过审核 |
| payTime | 否 | String | 当有传payTime时，订单的付款时间会被以参数的值覆盖，如: 2012-12-17 18:54:00 |

**返回示例：**

```json
{
      "IsSuccess":true,
      "Data":{
          "Waybills":[
            {
              "ParentWaybillCode":"xxxx",
              "WaybillCode":"xxxx"
            }
          ],
          "SendResult":{
            "IsSuccess":true,
            "ErrorMsg":""
          }
      },
      "Error_Code":0,
      "Error_Msg":"",
      "AllowRetry":null,
      "RequestId":"20201014150108088"
  }
```

---
