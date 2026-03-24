# 淘宝自动发货 (ALDS) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/alds/`

---

## 修改宝贝附言

**简要描述：** 修改宝贝在自动发货系统中，设置的要发送的附言。

**请求URL：** `/Item/UpdateAdditional`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| numIid | 是 | Long | 宝贝ID |
| additional | 是 | String | 附言内容 |
| skuId | 否 | Long | Sku Id（不传时更新宝贝设置，传对应SkuId时可以更新具体的SKU的设置） |
| aldsType | 否 | Int | 自动发货类型（1:付款时发【默认】; 2:确认收货时发; 4:好评时发） |

**返回示例：**

```json
{
    "IsSuccess":false,
    "Data":
    {
      "ErrorInfos":
      {
        "NumIid":3435436546,
        "SkuId":0,
        "ErrorMsg":"受影响数据0行，请检查该宝贝ID是否已添加到自动发货系统中。"
      }
    },
    "Error_Code":15,
    "Error_Msg":"更新附言失败"
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| ErrorInfos | ItemUpdateAdditionalErrorInfo | 修改宝贝附言失败的错误信息 |

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 修改库存数量

**简要描述：** 修改库存数量

**请求URL：** `/Item/QuantityUpdate`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| numIid | 是 | Long | 宝贝ID |
| quantity | 是 | Long | 宝贝数量 |
| skuId | 否 | Long | SKU ID |
| outerId | 否 | String | 商家编码 |
| type | 否 | Long | 类型,传2为增量修改,传1或者不传为全量修改 |

**返回示例：**

```json
{
    "IsSuccess":false,
    "Data":
    {
      "ErrorInfos":
      {
        "NumIid":3435436546,
        "SkuId":0,
        "OuterId":null,
        "Quantity":30,
        "type":1,
        "ErrorMsg":"ISV失败，错误代码：15；错误原因：Remote service error；错误描述：isv.item-not-exist:invalid-numIid-or-iid-商品id对应的商品不存在"
      }
    },
    "Error_Code":10,
    "Error_Msg":"更新库存数量失败",
    "AllowRetry":null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| ErrorInfos | ItemUpdateQuantityErrorInfo | 修改库存数量失败的错误信息 |

**备注：** 更多返回错误代码请看首页的错误代码描述,以及淘宝API文档的对应接口的返回信息

---

## 修改采购单备注

**简要描述：** 修改采购单备注

**请求URL：** `/Trade/MemoUpdate`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tids | 是 | String | 订单编号,多个订单编号间用,分隔开 |
| memo | 否 | String | 备注,替换掉原备注,如果不传则将备注修改为空 |
| flag | 否 | Long | 旗帜,为0-10的数字,如果不传则表示保留原旗帜,如果传入大于10则会识别为10 |

**返回示例：**

```json
{
    "IsSuccess":false,
    "Data":{
            "ErrorInfos":
                [
                    {
                        "Tid":324234345,
                        "ErrorMsg":"ISV失败，错误代码：520；错误原因：Remote service error；错误描述：isv.trade-not-exist-订单不存在：324234345"
                    },
                    {
                        "Tid":234235342,
                        "ErrorMsg":"ISV失败，错误代码：520；错误原因：Remote service error；错误描述：isv.trade-not-exist-订单不存在：234235342"
                    }
                ]
            },
    "Error_Code":7,
    "Error_Msg":"全部失败",
    "AllowRetry":null
}
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| ErrorInfos | tradesUpdateMemoErrorInfo[] | 修改备注失败的错误信息 |

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 修改采购单备注v1

**简要描述：** 修改采购单备注v1

**请求URL：** `/v1/Trade/MemoUpdate`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单编号 |
| memo | 否 | String | 备注,替换掉原备注,如果不传则将备注修改为空 |
| flag | 否 | Long | 旗帜,为0-10的数字,如果不传则表示保留原旗帜,如果传入大于10则会识别为10 |
| operator | 否 | Long | 可填操作员的淘宝账号UserID |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": ""
}
```

---

## 关闭采购单

**简要描述：** 关闭采购单

**请求URL：** `/Trade/Close`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tids | 是 | String | 订单编号,多个订单编号间用,分隔开 |
| closeReason | 是 | String | 交易关闭原因。可以选择的理由有：1.未及时付款 2、买家不想买了 3、买家信息填写错误，重新拍 4、恶意买家/同行捣乱 5、缺货 6、买家拍错了 7、同城见面交易 |

**返回示例：**

```json
{
    "IsSuccess": false,
    "Data": {
      "ErrorInfos": [{
        "Tid": 16450834718671238,
        "ErrorMsg": "未知错误，参考ISV失败，错误代码：520；错误原因：Remote service error；错误描述：isv.trade-not-exist-订单不存在：16450834718671238"
      }, {
        "Tid": 654927041195110504,
        "ErrorMsg": "参数：tid无效，格式不对、非法值、越界等，传入正确的订单ID"
      }]
    },
    "Error_Code": 7,
    "Error_Msg": "全部失败",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| ErrorInfos | TradesCloseErrorInfo[] | 关闭订单失败的错误信息 |

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 创建发货结果

**简要描述：** 调用该接口用于创建订单发货结果，该结果可在「自动发货软件」「订单日志」里查到。多次调用会生成多个发货结果，买家提取时只会提取到最后一个发货结果。

**请求URL：** `/Trade/CreateOrderResult`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单编号 |
| aldsType | 是 | Number | 1 付款后发货结果； 2、确认收货赠送结果；4、好评后赠送结果 |
| content | 是 | String | 发货结果内容，JSON字符串:[{"Oid":3130073692357778,"Additional":"附言（使用说明）","CardPwdContent":[{"CardNoShowType":1,"PwdShowType":0,"Title":"卡密标题","PrefixCardNo":"卡号前缀(非必填)","PrefixPwd":"卡密前缀(非必填)","CardPwdArr":[{"c":"0000030016","p":"","d":""}]}]}] |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": "",
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**备注：** 请求参数content说明，Oid：子订单编号【必填】，Additional：附言（使用说明）非必填，
  CardPwdContent：卡密信息非必填（长度不能超过5000字符），CardNoShowType、PwdShowType：卡号卡密展示类型（ 0：文本；1：条形码；2：二维码码；3：相册网址；4：条形码+二维码），
  PrefixCardNo：卡号前缀(非必填)，PrefixPwd：卡密前缀(非必填)，
  c：卡号，p：卡密，d：到期时间格式yyyy-MM-dd HH:mm:ss 非必填

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

## 卡券回库

**简要描述：** 卡券回库

**请求URL：** `/CardPwd/StockBack`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpcId | 是 | Number | 卡种ID |
| cardNo | 是 | String | 卡号 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "StockBackSuccCount": 1,
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| StockBackSuccCount | Number | 回库成功个数 |

---

## 发送手淘卡片

**简要描述：** 调用该接口发送手淘卡片。注意：由于平台规则限制，一笔订单24小时内只能发送一次手淘卡片，调用前需使用“创建发货结果”接口生成卡片内容。

**请求URL：** `/Trade/SendTbAppCard`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单编号 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": "发卡接口调用成功",
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

---

## 发送旺旺消息

**简要描述：** 发送旺旺消息，一笔订单10天内（从订单付款时间开始计算）可发送3次旺旺消息。注意：调用超过3次后会导致消息发不了，但仍会扣除接口费用。

**请求URL：** `/WwMsg/Send`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单编号 |
| msg | 是 | String | 要发给买家的旺旺消息，最大长度5000字 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": null,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

---

## 取消电子面单号

**简要描述：** 取消电子面单号

**请求URL：** `/Waybill/CainiaoWaybillCancel`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpCode | 是 | String | 物流公司code |
| waybillCode | 是 | String | 运单号 |

**返回示例：**

```json
{
       "IsSuccess": true,
       "Error_Code": 0,
       "Error_Msg": "",
       "AllowRetry": null
    }
```

**备注：** 参考：[商家取消获取的电子面单号](https://open.taobao.com/api.htm?docId=26766&docType=2&qq-pf-to=pcqq.c2c)

---

## 取消直充订单（退款）

**简要描述：** 取消直充订单（退款），该接口只适用天猫直充订单的订单状态更新，不支持其它类型的订单。

**请求URL：** `/Trade/CancelCeTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Number | 订单编号 |
| reason | 是 | String | 取消原因 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

---

## 完成直充订单（发货）

**简要描述：** 完成直充订单（发货），该接口只适用天猫直充订单的订单状态更新，不支持其它类型的订单。

**请求URL：** `/Trade/FinishCeTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Number | 订单编号 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

---

## 执行自动发货

**简要描述：** 调用该接口将根据您在自动发货后台设定的发货规则，进行一次发货逻辑的处理。该操作等同于在[手动发货页面](https://alds.agiso.com/aldstb/#/Autologistics/AldsManual)的操作。注意：该页面执行后，也会自动发送旺旺，可以通过参数中的选项控制发货中的一些限制。

**请求URL：** `/Trade/AldsProcessTrades`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tids | 是 | String | 订单编号,多个订单编号间用,分隔开 |
| ignoreAldsLog | 否 | String | 忽略发货记录            默认值:'false',可选值'true'、'false' |
| ignoreBlackList | 否 | String | 忽略黑名单            默认值:'false',可选值'true'、'false' |
| ignoreOnOff | 否 | String | 忽略发货开关            默认值:'false',可选值'true'、'false' |
| ignoreRefundCheck | 否 | String | 退款中也发            默认值:'false',可选值'true'、'false' |
| ignoreRestricted | 否 | String | 忽略限拍限购            默认值:'false',可选值'true'、'false' |
| ignoreTradeStatusCheck | 否 | String | 忽略订单状态验证            默认值:'false',可选值'true'、'false' |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "ResultsInfo": [{
        "Tid": 1645083471867778,
        "ResultCode": 100,
        "ResultMsg": "发送完成，从历史记录发货，一般是备用方案发过货了，因此无需再生成旺旺消息！"
      }]
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| ResultsInfo | AldsTradesResult[] | 执行自动发货返回的信息 |

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 提卡

**简要描述：** 手动提卡。

**请求URL：** `/CardPwd/PickupStockOut`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpcId | 是 | Long | 卡种ID |
| usedTid | 是 | Long | 订单编号，保证唯一，并且大于11位 |
| num | 是 | Int | 提卡数量 |
| usedNick | 是 | String | 买家昵称 |
| buildCpd | 否 | Boolean | 是否生成提取链接 |

**返回示例：**

```json
{
    "IsSuccess":true,
    "Data":
    {
      "SuccCount": 1,  // 成功数量
      "CpdUrl": "https://alds.agiso.com/ocb0c6f74c8a95355c3f6c7d9d42.aspx",  // 提取链接
      "CardPwdList": [{  // 提取的卡券列表
        "c": "123",  // 卡号
        "p": "123"  // 密码
      }]
    },
    "Error_Code":0,
    "Error_Msg":""
  }
```

**备注：** 更多返回错误代码请看首页的错误代码描述

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

## 更新发货状态（线下自己联系物流发货）

**简要描述：** 更新发货状态（线下自己联系物流发货）

**请求URL：** `/Trade/LogisticsOfflineSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Number | 淘宝交易的订单编号 |
| subTid | 否 | Number[] | 需要拆单发货的子订单集合，针对的是一笔交易下有多个子订单需要分开发货的场景；1次可传人多个子订单号，子订单间用逗号隔开；为空表示不做拆单发货。最大列表长度：50 |
| outSid | 是 | String | 运单号。具体一个物流公司的真实运单号码。淘宝官方物流会校验，请谨慎传入！ |
| companyCode | 是 | String | 物流公司代码。如"POST"就代表中国邮政，“ZJS”就代表宅急送。可调用淘宝接口 taobao.logistics.companies.get 获取。 |

**返回示例：**

```json
{
    "IsSuccess": false,
    "Data": {
      "ErrCode": "isv.logistics-online-service-error:B04"
      "IsSuccess": false
    },
    "Error_Code": 10,
    "Error_Msg": "调用淘宝接口失败"
  }
```

**备注：** 参考：[淘宝接口文档](http://open.taobao.com/docs/api.htm?spm=a219a.7629065.0.0.2NLtBh&apiId=10690)

---

## 更新发货状态（采购成功发货）

**简要描述：** 更新发货状态（采购成功发货），一般虚拟商品使用

**请求URL：** `/Trade/LogisticsDummySend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tids | 是 | String | 订单编号,多个订单编号间用,分隔开 |

**返回示例：**

```json
{
    "IsSuccess": false,
    "Data": {
      "ErrorInfos": [
        {
          "Tid": 16450834718671238,
          "ErrorCode": -81,
          "AllowRetry": false
        },
        { 
          "Tid": 16434660155127778,
          "ErrorCode": -81,
          "AllowRetry": false
        }
      ]
    },
    "Error_Code": 7,
    "Error_Msg": "全部失败",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| ErrorInfos | DummySendErrorInfo[] | 交易更新发货状态失败的错误信息 |

**备注：** 参考：[淘宝文档](https://open.taobao.com/api.htm?docId=121&docType=2)

---

## 查询商家被授权品牌列表和类目列表

**简要描述：** 查询商家被授权品牌列表和类目列表

**请求URL：** `/ItemCategory/ItemcatsAuthorizeGet`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fields | 是 | String | 需要返回的字段。目前支持有： brand.vid, brand.name, item_cat.cid, item_cat.name, item_cat.status, item_cat.sort_order, item_cat.parent_cid, item_cat.is_parent, xinpin_item_cat.cid, xinpin_item_cat.name, xinpin_item_cat.status, xinpin_item_cat.sort_order, xinpin_item_cat.parent_cid, xinpin_item_cat.is_parent |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "Brands": [],
      "ItemCats": [],
      "XinpinItemCats": [{
        "Cid": 50011740,   // 商品所属类目ID
        "Features": [],  // Feature对象列表
                              目前已有的属性：
                              若Attr_key为 udsaleprop，attr_value为1 则允许卖家在改类目新增自定义销售属性,不然为不允许
        "IsParent": true,   // 该类目是否为父类目(即：该类目是否还有子类目)
        "Name": "流行男鞋",   // 类目名称
        "ParentCid": 0,   // 父类目ID=0时，代表的是一级的类目
        "SortOrder": 168,   // 排列序号，表示同级类目的展现次序，如数值相等则按名称次序排列。取值范围:大于零的整数
        "Status": "normal",   // 状态。可选值:normal(正常),deleted(删除)
        "TaosirCat": false   // 是否度量衡类目
      }]
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**备注：** 返回参数说明请参考：[淘宝文档（点击查看）](https://open.taobao.com/api.htm?docId=161&docType=2)

---

## 查询面单服务订购及面单使用情况 

**简要描述：** 查询面单服务订购及面单使用情况

**请求URL：** `/Waybill/CainiaoWaybillIiSearch`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpCode | 否 | String | 物流公司code |

**返回示例：**

```json
{
       "IsSuccess": true,
       "Data": [{
            "BranchAccountCols":[
                {
                    "AllocatedQuantity":0,
                    "BranchCode":null,
                    "BranchName":null,
                    "BranchStatus":0,
                    "CancelQuantity":0,
                    "PrintQuantity":0,
                    "Quantity":0,
                    "SegmentCode":null,
                    "ServiceInfoCols":[
                        {
                            "Required":false,
                            "ServiceAttributes":[
                                {
                                    "AttributeCode":null,
                                    "AttributeName":null,
                                    "AttributeType":null,
                                    "TypeDesc":null
                                }
                            ],
                            "ServiceCode":null,
                            "ServiceDesc":null,
                            "ServiceName":null
                        }
                    ],
                    "ShippAddressCols":[
                        {
                            "City":null,
                            "Detail":null,
                            "District":null,
                            "Province":null,
                            "Town":null
                        }
                    ]
                }
            ],
            "CpCode":null,
            "CpType":0
       }],
       "Error_Code": 0,
       "Error_Msg": "",
       "AllowRetry": null
    }
```

**备注：** 参考：[查询面单服务订购及面单使用情况](https://open.taobao.com/api.htm?docId=27125&docType=2&qq-pf-to=pcqq.c2c)

---

## 根据淘宝账号获取openuid

**简要描述：** 根据淘宝账号获取openuid，单次最多30个

**请求URL：** `/User/UserOpenuidGetbynick`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| buyerNicks | 是 | String | 淘宝账号列表，示例：tesapo,kimvb2000            更多字段参考[文档](https://open.taobao.com/api.htm?docId=63724&docType=2) |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": {
        "OpenUids":[{
            "BuyerNick": "Test",
            "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa"
        }]
      },
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null
    }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| BuyerNick | String | 淘宝账号昵称 |
| BuyerOpenUid | String | 淘宝OpenUid |

**备注：** 返回参数说明请参考：[淘宝文档（点击查看）](https://open.taobao.com/api.htm?docId=63724&docType=2)

---

## 添加卡券

**简要描述：** 可添加卡券种类：禁止重复卡号、允许重复卡号、套卡、无限循环使用卡券。不可添加卡券种类：图片卡种

**请求URL：** `/CardPwd/Add`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpcId | 是 | Number | 卡种ID |
| data | 是 | String | 卡券数据，卡号与密码之间的分隔符用英文逗号，一行一个卡券数据，最多1000行卡券 |
| isUseFirst | 否 | bool | 是否优先出库。0表示否，1表示是 |
| allowReplace | 否 | bool | 是否覆盖已存在卡券，0表示不覆盖，1表示覆盖 |
| summary | 否 | String | 描述，比如：该批次卡种的供应商等相关信息 |
| price | 否 | Decimal | 成本单价 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "AddSuccessCount": 1,
      "AddFailCount": 0,
      "ReplaceUnSoldSuccessCount": 0,
      "ReplaceSoldSuccessCount": 0,
      "ReplaceFailCount": 0
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| AddSuccessCount | Number | 卡券添加成功数量 |
| AddFailCount | Number | 卡券添加失败数量 |
| ReplaceUnSoldSuccessCount | Number | 未出售卡券覆盖成功数量 |
| ReplaceSoldSuccessCount | Number | 已出售卡券覆盖成功数量 |
| ReplaceFailCount | Number | 卡券密覆盖失败数量 |
| ResultMsg | String | 返回结果信息 |

---

## 物流流转信息查询

**简要描述：** 物流流转信息查询

**请求URL：** `/Trade/LogisticsTraceSearch`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Number | 订单编号 |
| sellerNick | 是 | String | 卖家昵称 |
| subTid | 否 | Number[]\t | 拆单子订单列表，比如：1,2,3 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "OutSid": "1324657987",
      "CompanyName": "中通速递",
      "Tid": "1324657987",
      "Status": "",
      "TraceList": [{
        "StatusTime": "2000-01-01 00:00:00",
        "StatusDesc": "达到杭州物流集中地",
        "Action": "ARRIVE"
      }],
    },
    "Error_Code": 0,
    "Error_Msg": ""
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| OutSid | String | 运单号 |
| CompanyName | String | 物流公司名称 |
| Tid | Number | 交易号 |
| Status | String | 订单的物流状态（仅支持线上发货online订单，线下发货offline发出后直接变为已签收） * 等候发送给物流公司 *已提交给物流公司,等待物流公司接单 *已经确认消息接收，等待物流公司接单 *物流公司已接单 *物流公司不接单 *物流公司揽收失败 *物流公司揽收成功 *签收失败 *对方已签收 *对方拒绝签收 |
| TraceList | Trace[] | 流转信息列表 |

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 电子面单云打印接口 

**简要描述：** 菜鸟电子面单的云打印申请电子面单号的方法

**请求URL：** `/Waybill/PrintApply`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| sellerToken | 否 | String | 订单所属卖家的AccessToken，如果有传该参数并且Recipient为空时，会自动获取TradeOrderList的头一笔订单的收件人信息填充到Recipient |
| paramJson | 是 | String | {     "CpCode":"YTO",     "DmsSorting":null,     "ProductCode":null,     "ResourceCode":null,     "Sender":{         "Address":{             "City":"杭州市",             "Detail":"********",             "District":"上城区",             "Province":"浙江省",             "Town":null         },         "Mobile":"159***99",         "Name":"小明",         "Phone":null     },     "StoreCode":null,     "ThreePlTiming":null,     "TradeOrderInfoDtos":[         {             "LogisticsServices":null,             "ObjectId":"1",             "OrderInfo":{                 "OrderChannelsType":"TB",                 "TradeOrderList":[                     "660372***7364701"                 ]             },             "PackageInfo":{                 "GoodsDescription":null,                 "Id":"123a",                 "Items":[                     {                         "Count":1,                         "Name":"衣服"                     }                 ],                 "PackagingDescription":null,                 "TotalPackagesCount":null,                 "Volume":null,                 "Weight":null             },             "Recipient":{                 "Address":{                     "City":"张家口市",                     "Detail":"********",                     "District":"万全区",                     "Province":"河北省",                     "Town":null                 },                 "Mobile":"139****93",                 "Name":"小红",                 "Phone":null             },             "TemplateUrl":"http://cloudprint.cainiao.com/template/standard/101/632",             "UserId":null         }     ] } |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": {
        "Modules": "[
            {
                "ObjectId":"1",
                "ParentWaybillCode":null,
                "PrintData":"{
                    "encryptedData":"********",
                    "signature":"MD:PijS7175cLjAj+erewrew==",
                    "templateURL":"http://cloudprint.cainiao.com/template/standard/301",
                    "ver":"waybill_print_secret_version_1"
                }",
                "WaybillCode":"YT45435431234777"
            }
        ]"
      },
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null
    }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Modules |  | 面单信息 |

**备注：** 参考：[电子面单云打印接口](https://open.taobao.com/api.htm?docId=26869&docType=2)

---

## 获取出售中的商品列表

**简要描述：** 获取出售中的商品列表

**请求URL：** `/Item/OnSaleGet`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fields | 是 | String | 需返回的字段列表。可选值：Item商品结构体中的以下字段： approve_status,num_iid,title,nick,type,cid,pic_url,num,props,valid_thru,list_time,price, has_discount,has_invoice,has_warranty,has_showcase,modified,delist_time,postage_id, seller_cids,outer_id,sold_quantity ；字段之间用“,”分隔。不支持其他字段，如果需要获取其他字段数据，调用taobao.item.seller.get 获取。 |
| q | 否 | String | 搜索字段。搜索商品的title |
| cid | 否 | Number | 商品类目ID。ItemCat中的cid字段。可以通过taobao.itemcats.get取到 |
| sellerCids | 否 | String | 卖家店铺内自定义类目ID。多个之间用“,”分隔。可以根据taobao.sellercats.list.get获得.(注：目前最多支持32个ID号传入) |
| pageNo | 否 | Number | 页码。取值范围:大于零的整数。默认值为1,即默认返回第一页数据。用此接口获取数据时，当翻页获取的条数（page_no*page_size）超过10万,为了保护后台搜索引擎，接口将报错。所以请大家尽可能的细化自己的搜索条件，例如根据修改时间分段获取商品 |
| hasDiscount | 否 | Boolean | 是否参与会员折扣。可选值：true，false。默认不过滤该条件 |
| hasShowcase | 否 | Boolean | 是否橱窗推荐。 可选值：true，false。默认不过滤该条件 |
| orderBy | 否 | String | 排序方式。格式为column:asc/desc ，column可选值:list_time(上架时间),delist_time(下架时间),num(商品数量)，modified(最近修改时间)，sold_quantity（商品销量）,;默认上架时间降序(即最新上架排在前面)。如按照上架时间降序排序方式为list_time:desc |
| isTaobao | 否 | Boolean | 商品是否在淘宝显示 |
| isEx | 否 | Boolean | 商品是否在外部网店显示 |
| pageSize | 否 | Number | 每页条数。取值范围:大于零的整数;最大值：200；默认值：200。用此接口获取数据时，当翻页获取的条数（page_no*page_size）超过2万,为了保护后台搜索引擎，接口将报错。所以请大家尽可能的细化自己的搜索条件，例如根据修改时间分段获取商品 |
| startModified | 否 | Date | 起始的修改时间，比如：2000-01-01 00:00:00 |
| endModified | 否 | Date | 结束的修改时间，比如：2000-01-01 00:00:00 |
| isCspu | 否 | Boolean | 是否挂接了达尔文标准产品体系 |
| isCombine | 否 | Boolean | 组合商品 |
| auctionType | 否 | String | 商品类型：a-拍卖,b-一口价 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": [{
      "AfterSaleId": 0,
      "ApproveStatus": "onsale",
      "AuctionPoint": 0,
      "AutoFill": null,
      "AutoRepost": false,
      "Barcode": null,
      "ChangeProp": null,
      "ChaoshiExtendsInfo": null,
      "ChargeFreeList": null,
      "Cid": 50158004,
      "CodPostageId": 0,
      "CpvMemo": null,
      "Created": null,
      "CuntaoItemSpecific": null,
      "CustomMadeTypeId": null,
      "DelistTime": "2019-05-21 14:14:29",
      "DeliveryTime": null,
      "Desc": null,
      "DescModuleInfo": null,
      "DescModules": null,
      "DetailUrl": null,
      "EmsFee": null,
      "ExpressFee": null,
      "Features": null,
      "FoodSecurity": null,
      "FreightPayer": null,
      "GlobalStockCountry": null,
      "GlobalStockDeliveryPlace": null,
      "GlobalStockTaxFreePromise": false,
      "GlobalStockType": null,
      "HasDiscount": false,
      "HasInvoice": false,
      "HasShowcase": false,
      "HasWarranty": false,
      "Iid": null,
      "Increment": null,
      "InnerShopAuctionTemplateId": 0,
      "InputCustomCpv": null,
      "InputPids": null,
      "InputStr": null,
      "Is3D": false,
      "IsAreaSale": false,
      "IsCspu": false,
      "IsEx": false,
      "IsFenxiao": 0,
      "IsLightningConsignment": false,
      "IsPrepay": false,
      "IsTaobao": false,
      "IsTiming": false,
      "IsVirtual": false,
      "IsXinpin": false,
      "ItemImgs": [],
      "ItemRectangleImgs": [],
      "ItemSize": null,
      "ItemWeight": null,
      "ItemWirelessImgs": [],
      "LargeScreenImageUrl": null,
      "ListTime": "2019-05-14 14:14:29",
      "LocalityLife": null,
      "Location": null,
      "Modified": "2019-05-15 11:46:42",
      "MpicVideo": null,
      "MsPayment": null,
      "Newprepay": null,
      "Nick": "168商务休闲馆",
      "Num": 27,
      "NumIid": 556850391855,
      "O2oBindService": false,
      "OneStation": false,
      "OuterId": "",
      "OuterShopAuctionTemplateId": 0,
      "PaimaiInfo": null,
      "PeriodSoldQuantity": 0,
      "PicUrl": "https://img.alicdn.com/bao/uploaded/i3/584056073/O1CN01mVMNjk1ujTodGb6kQ-584056123.png",
      "PostFee": null,
      "PostageId": 10109079570,
      "Price": "1.00",
      "ProductId": 0,
      "PromotedService": null,
      "PropImgs": [],
      "PropertyAlias": null,
      "Props": "1627207:130164;1627207:28324;1627207:28329",
      "PropsName": null,
      "Qualification": null,
      "Score": 0,
      "SecondKill": null,
      "SellPoint": null,
      "SellPromise": false,
      "SellerCids": "-1",
      "Skus": [],
      "SoldQuantity": 14,
      "SpuConfirm": false,
      "StuffStatus": null,
      "SubStock": 0,
      "SupportChargeFree": false,
      "TemplateId": null,
      "Title": "某电影票A0066666",
      "Type": "fixed",
      "ValidThru": 7,
      "VerticalImgs": [],
      "VideoId": 0,
      "Videos": [],
      "Violation": false,
      "Volume": 0,
      "WapDesc": null,
      "WapDetailUrl": null,
      "WhiteBgImage": null,
      "WirelessDesc": null,
      "WithHoldQuantity": 0,
      "WwStatus": false
    }],
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Title | String | 商品标题,不能超过60字节 |

**备注：** 返回参数说明请参考：[淘宝文档（点击查看）](https://open.taobao.com/api.htm?docId=18&docType=2)

---

## 获取单个商品详细信息

**简要描述：** 获取单个商品详细信息

**请求URL：** `/Item/SellerGet`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fields | 是 | String | 需要返回的商品字段列表。示例：num_iid,title,nick,price,approve_status,sku            更多字段参考[文档](https://open.taobao.com/api.htm?docId=24625&docType=2) |
| numIid | 是 | Number | 商品数字ID |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "AfterSaleId": 0,
      "ApproveStatus": "onsale",
      "AuctionPoint": 0,
      "AutoFill": null,
      "AutoRepost": false,
      "Barcode": null,
      "ChangeProp": null,
      "ChaoshiExtendsInfo": null,
      "ChargeFreeList": null,
      "Cid": 0,
      "CodPostageId": 0,
      "CpvMemo": null,
      "Created": null,
      "CuntaoItemSpecific": null,
      "CustomMadeTypeId": null,
      "DelistTime": null,
      "DeliveryTime": null,
      "Desc": null,
      "DescModuleInfo": null,
      "DescModules": null,
      "DetailUrl": null,
      "EmsFee": null,
      "ExpressFee": null,
      "Features": null,
      "FoodSecurity": null,
      "FreightPayer": null,
      "GlobalStockCountry": null,
      "GlobalStockDeliveryPlace": null,
      "GlobalStockTaxFreePromise": false,
      "GlobalStockType": null,
      "HasDiscount": false,
      "HasInvoice": false,
      "HasShowcase": false,
      "HasWarranty": false,
      "Iid": null,
      "Increment": null,
      "InnerShopAuctionTemplateId": 0,
      "InputCustomCpv": null,
      "InputPids": null,
      "InputStr": null,
      "Is3D": false,
      "IsAreaSale": false,
      "IsCspu": false,
      "IsEx": false,
      "IsFenxiao": 0,
      "IsLightningConsignment": false,
      "IsPrepay": false,
      "IsTaobao": false,
      "IsTiming": false,
      "IsVirtual": false,
      "IsXinpin": false,
      "ItemImgs": [],
      "ItemRectangleImgs": [],
      "ItemSize": null,
      "ItemWeight": null,
      "ItemWirelessImgs": [],
      "LargeScreenImageUrl": null,
      "ListTime": null,
      "LocalityLife": null,
      "Location": null,
      "Modified": null,
      "MpicVideo": null,
      "MsPayment": null,
      "Newprepay": "default",
      "Nick": "168商务休闲馆",
      "Num": 0,
      "NumIid": 41820050917,
      "O2oBindService": false,
      "OneStation": false,
      "OuterId": null,
      "OuterShopAuctionTemplateId": 0,
      "PaimaiInfo": null,
      "PeriodSoldQuantity": 0,
      "PicUrl": null,
      "PostFee": null,
      "PostageId": 0,
      "Price": "0.10",
      "ProductId": 0,
      "PromotedService": null,
      "PropImgs": [],
      "PropertyAlias": null,
      "Props": null,
      "PropsName": null,
      "Qualification": null,
      "Score": 0,
      "SecondKill": null,
      "SellPoint": null,
      "SellPromise": false,
      "SellerCids": null,
      "Skus": [],
      "SoldQuantity": 0,
      "SpuConfirm": false,
      "StuffStatus": null,
      "SubStock": 0,
      "SupportChargeFree": false,
      "TemplateId": null,
      "Title": "agiso阿奇索自动发货软件自动发旺旺机器人24小时无人职守提取",
      "Type": null,
      "ValidThru": 0,
      "VerticalImgs": [],
      "VideoId": 0,
      "Videos": [],
      "Violation": false,
      "Volume": 0,
      "WapDesc": null,
      "WapDetailUrl": null,
      "WhiteBgImage": null,
      "WirelessDesc": null,
      "WithHoldQuantity": 0,
      "WwStatus": false
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Title | String | 商品标题,不能超过60字节 |

**备注：** 返回参数说明请参考：[淘宝文档（点击查看）](https://open.taobao.com/api.htm?docId=24625&docType=2)

---

## 获取卖家信息

**简要描述：** 获取卖家信息

**请求URL：** `/User/SellerGet`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fields | 是 | String | 需要返回的字段列表，示例：nick,sex            更多字段参考[文档](https://open.taobao.com/api.htm?docId=21349&docType=2) |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "Age": 0,
      "AlipayAccount": null,
      "AlipayBind": null,
      "AlipayNo": null,
      "AutoRepost": null,
      "Avatar": null,
      "Birthday": null,
      "BuyerCredit": null,
      "ConsumerProtection": false,
      "Created": null,
      "Email": null,
      "HasMorePic": false,
      "HasShop": false,
      "HasSubStock": false,
      "IsGoldenSeller": false,
      "IsLightningConsignment": false,
      "ItemImgNum": 0,
      "ItemImgSize": 0,
      "LastVisit": null,
      "Liangpin": false,
      "Location": null,
      "MagazineSubscribe": false,
      "ManageBook": false,
      "Mobile": null,
      "Nick": "168商务休闲馆",
      "OnlineGaming": false,
      "OpenUid": null,
      "Phone": null,
      "PromotedType": null,
      "PropImgNum": 0,
      "PropImgSize": 0,
      "RealName": null,
      "SellerCredit": null,
      "Sex": "m",
      "SignConsumerProtection": false,
      "SignFoodSellerPromise": false,
      "Status": null,
      "Type": null,
      "Uid": null,
      "UserId": 0,
      "VerticalMarket": null,
      "VipInfo": null,
      "VipLevel": 0
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Nick | String | 用户昵称 |

**备注：** 返回参数说明请参考：[淘宝文档（点击查看）](https://open.taobao.com/api.htm?docId=21349&docType=2)

---

## 获取卡券卡种列表

**简要描述：** 获取卡券卡种列表

**请求URL：** `/CardPwdCategory/GetList`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| pageNo | 是 | Number | 页码 |
| pageSize | 是 | Number | 分页大小, 最多值100 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "List": [{
        "IdNo": 551426,  // 卡种ID
        "Idx": 292,  // 排序值
        "Title": "1122新地生",  // 卡种名称
        "ClassId": 0,  // 卡种分类ID
        "CardType": 820,  // 卡种类型
        "TotalNum": 5,  // 卡券总数
        "UsedNum": 0,  // 卡券已用数量
        "PurPrice": 0.0,  // 成本单价
        "ModifyTime": "2019-10-18T15:16:05",  // 修改时间
        "CreateTime": "2019-09-03T14:28:45",  // 创建时间
      }],
      "HasNext": false  // 是否有下一页
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 获取卡券卡种库存量

**简要描述：** 获取卡券卡种库存量大概值

**请求URL：** `/CardPwdCategory/GetStorage`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| idNos | 是 | String | 卡种ID, 多个卡种ID间用,分隔开（半角逗号分隔） |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": [{
      "IdNo": 456633,  // 卡种ID
      "Qty": 2   // 卡种库存量
    }, {
      "IdNo": 551391,
      "Qty": 7
    }],
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| IdNo | Number | 卡种ID |
| Qty | Number | 卡种库存量 |

**备注：** 更多返回错误代码请看首页的错误代码描述

---

## 获取商品SKU信息

**简要描述：** 获取商品SKU信息

**请求URL：** `/Item/SkusGet`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fields | 是 | String[] | 需返回的字段列表，示例值：sku_id,iid,properties,quantity,price,outer_id,created,modified,status            更多字段参考[文档](https://open.taobao.com/api.htm?docId=28&docType=2) |
| numIids | 是 | String | sku所属商品数字id，必选。numIid个数不能超过40个。示例值：1230005 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": [{
      "Barcode": null,
      "ChangeProp": null,
      "Created": null,
      "DeliveryTimeType": null,
      "ExtraId": 0,
      "GmtModified": null,
      "Iid": null,
      "Memo": null,
      "Modified": null,
      "NumIid": 556850391855,
      "OuterId": null,
      "Price": null,
      "Properties": null,
      "PropertiesName": null,
      "Quantity": 0,
      "SkuDeliveryTime": null,
      "SkuFeature": null,
      "SkuId": 3894069941929,
      "SkuSpecId": 0,
      "SpecId": null,
      "Status": null,
      "WithHoldQuantity": 0
    }, {
      "Barcode": null,
      "ChangeProp": null,
      "Created": null,
      "DeliveryTimeType": null,
      "ExtraId": 0,
      "GmtModified": null,
      "Iid": null,
      "Memo": null,
      "Modified": null,
      "NumIid": 556850391855,
      "OuterId": null,
      "Price": null,
      "Properties": null,
      "PropertiesName": null,
      "Quantity": 0,
      "SkuDeliveryTime": null,
      "SkuFeature": null,
      "SkuId": 3447354505357,
      "SkuSpecId": 0,
      "SpecId": null,
      "Status": null,
      "WithHoldQuantity": 0
    }],
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**备注：** 返回参数说明请参考：[淘宝文档（点击查看）](https://open.taobao.com/api.htm?docId=28&docType=2)

---

## 获取所有的菜鸟标准电子面单模板 

**简要描述：** 获取所有的菜鸟标准电子面单模板

**请求URL：** `/Waybill/Stdtemplates`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": {
        "Datas": [{
            "CpCode": "YTO",
            "StandardTemplates": [{
                "StandardTemplateId": 1024,
                "StandardTemplateName": "YTO模板",
                "StandardTemplateUrl": "模板url",
                "StandardWaybillType": 1
            }]
        }],
      },
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null
    }
```

**备注：** 参考：[获取所有的菜鸟标准电子面单模板](https://open.taobao.com/api.htm?docId=26756&docType=2)

---

## 获取提取记录

**简要描述：** 可获取订单网页提取【通过网页提取的提取记录】及卡券明细提取【单笔订单中卡券较多显示不完整时，完整卡券提取记录】

**请求URL：** `/Log/GetTiqu`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单编号 |
| selDataType | 是 | String | 提取类型："cpd"：卡券明细提取，"tiqu"：订单网页提取。默认是"tiqu" |
| pageNo | 否 | Number | 页码 |
| pageSize | 否 | Number | 分页大小，默认：20，最多值100 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": [{
      "Tid": 105118887066025524,
      "RealIp": "127.0.0.1",
      "CreateTime": "2017-12-14T10:11:24",
      "AldsType": 2
    }, {
      "Tid": 105118887066025524,
      "RealIp": "127.0.0.1",
      "CreateTime": "2017-12-08T09:22:32",
      "AldsType": 2
    }, {
      "Tid": 105118887066025524,
      "RealIp": "127.0.0.1",
      "CreateTime": "2017-12-08T09:21:24",
      "AldsType": 2
    }],
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Tid | String | 订单编号 |
| RealIp | String | Ip地址 |
| CreateTime | DateTime | 创建时间 |
| AldsType | Number | 当请求类型 selDataType=cpd 时才有此列，类型: 1: 付款后发,2: 确认收货发, 3:好评赠送 |

---

## 追加采购单备注

**简要描述：** 追加采购单备注

**请求URL：** `/Trade/MemoAppend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单编号 |
| memo | 否 | String | 备注,在原备注上追加 |
| flag | 否 | Long | 旗帜,为0-10的数字,如果不传则表示保留原旗帜,如果传入大于10则会识别为10 |
| operator | 否 | Long | 可填操作员的淘宝账号UserID |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": ""
  }
```

---

## 通过Tid查询发送的卡种

- 通过Tid查询发送的卡种
- 注意：仅支持查询淘宝本地仓出库的订单，不支持91卡券。如果接口没返回卡券，可能是还在出库中，等待5分钟后再尝试。

**请求URL：** `/Trade/QueryTradeCPSendLog`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Number | 淘宝订单号。 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Data": {
      "Orders": [{
        "Oid": 1645083471867778,  // 子订单号
        "NumIid": 4564,  // 宝贝ID
        "OuterIid": "34543",  // 宝贝外部编码
        "OuterSkuId": "453564",  // Sku外部编码
        "Title": "自动发货24小时无人值守",  // 宝贝标题
        "SkuPropertiesName": "dfds4534",  // Sku属性名称
        "Price": "0.01",  // 价格
        "Num": 2,  // 数量
        "TotalFee": "0.01",  // 总价
        "Payment": "0.01",  // 支付金额
        "SendCards": [{
          "CpcId": 345,  // 卡种ID
          "Title": "100元充值券",  // 卡种标题
          "Cards": [{
            "Card": "343254654365435",  // 卡号
            "Pwd": "567575634"  // 密码
          }]
        }]
      }]
    },
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null
  }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| CpcId | Number | 卡种Id |
| Title | String | 卡种标题 |
| Card | String | 卡号 |
| Pwd | String | 卡券 |

**备注：** 更多返回参数说明请参考淘宝API文档的对应接口的返回信息

---
