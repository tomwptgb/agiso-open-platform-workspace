# 拼多多自动发货 (AldsPdd) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsPdd/`

---

## 其它发货

**请求URL：** `/DummySend/OtherSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20201027142251106"
    }
```

---

## 卡号密码发货

**请求URL：** `/DummySend/CardPwdSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| cardNo | 是 | String | 卡号 |
| password | 是 | String | 密码 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20201027142251106"
    }
```

---

## 发送重置退款限制短信

**简要描述：** 获取重置退款限制验证码

**请求URL：** `/Refund/SendResetLimitSms`

**请求方式：** POST

**返回示例：**

```json
{
      "isSuccess": true,
      "data": "已成功发送至：186****5890",
      "error_Code": 0,
      "error_Msg": ""
    }
```

**备注：** 注：店铺需要绑定91卡密，短信发送到绑定91卡密预留手机号码。

---

## 取消电子面单号

**简要描述：** 取消电子面单号

**请求URL：** `/Waybill/PddWaybillCancel`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| wpCode | 是 | String | 物流公司code |
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

**备注：** 参考：[商家取消获取的电子面单号](https://open.pinduoduo.com/application/document/api?id=pdd.waybill.cancel)

---

## 同意退款

**简要描述：** 同意退款

**请求URL：** `/Refund/AgreeRefund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| refundId | 是 | Long | 售后Id |

**返回示例：**

```json
{
        "isSuccess": true,
        "error_Code": 0,
        "error_Msg": ""
    }
```

**备注：** 退款限制说明：1、单笔最大金额限制不超过500，错误码error_Code=20  2、每日退款总额不超过5000，错误码error_Code=22  3、每日退款次数限制20次，错误码 error_Code=23

---

## 商品列表

**简要描述：** 商品列表查询

**请求URL：** `/Goods/List`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| outerId | 否 | String | 商品外部编码（sku） |
| goodsName | 否 | String | 商品名称 |
| isOnsale | 否 | Number | 上下架状态，0-下架，1-上架 |
| page | 否 | Number | 页码默认 1 |
| pageSize | 否 | Number | 默认100，最大100 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": {
        "total_count": 10,   // 商品总数
        "goods_list:[   // 商品列表
          {
            "thumb_url":"https://xx.xx.com/xxx.jpg",   // 商品缩略图
            "goods_id": 1000,   // 商品Id
            "goods_name": "商品名称",   // 商品名称
            "image_url": "商品图片",   // 商品图片
            "is_more_sku": 0,   // 是否多sku，0-单sku，1-多sku
            "goods_quantity": 58,   // 商品总数量
            "is_onsale": 1,   // 是否在架上，0-下架中，1-架上
            "sku_list": [
              "spec": "规格名称",   // 规格名称
              "sku_id": 3163516514,   // sku Id
              "sku_quantity": 1000,   // sku库存
              "outer_id": "商家外部编码（sku）",   // 商家外部编码（sku）
              "outer_goods_id": "商家外部编码（商品）",   // 商家外部编码（商品）
              "is_sku_onsale": 1,   // sku是否在架上，0-下架中，1-架上
              "reserve_quantity": 0   // sku预扣库存
            ],
            "goods_reserve_quantity": 0   // 商品预扣库存
          }
        ]
      }
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20201027142251106"
    }
```

---

## 快递公司

**简要描述：** 获取快递公司名称

**请求URL：** `/Logistics/LogisticsCompanies`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": false,
      "Data": {
        logistics_companies: [{
            id: 123,
            logistics_company: "顺丰",
            code: "SF",
            available: 1
        }]
      }
      "Error_Code": 15,
      "Error_Msg": "发货失败"
    }
```

**备注：** 参考文档快递公司查看接口

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

## 查询面单服务订购及面单使用情况

**简要描述：** 查询面单服务订购及面单使用情况

**请求URL：** `/Waybill/SearchWaybill`

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
            "branch_account_cols":[
                {
                    "allocated_quantity":0,
                    "quantity":0,
                    "branch_code":null,
                    "branch_name":null,
                    "cancel_quantity":0,
                    "recycled_quantity":0,
                    "service_info_cols":[
                        {
                            "required":false,
                            "service_attributes":[
                                {
                                    "attribute_code":null,
                                    "attribute_name":null,
                                    "attribute_type":null,
                                    "type_desc":null
                                }
                            ],
                            "service_code":null,
                            "service_desc":null,
                            "service_name":null
                        }
                    ],
                    "shipp_address_cols":[
                        {
                            "city":null,
                            "detail":null,
                            "district":null,
                            "province":null
                        }
                    ]
                }
            ],
            "wp_code":null,
            "wp_type":0
        }],
       "Error_Code": 0,
       "Error_Msg": "",
       "AllowRetry": null
    }
```

**备注：** 参考：[查询面单服务订购及面单使用情况](https://open.pinduoduo.com/application/document/api?id=pdd.waybill.search)

---

## 消息发送

**简要描述：** 发送聊天窗口消息（需要开拼多多助手，每笔订单30天内只能发送两条消息）

**请求URL：** `/ImMsg/SendMsg`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| msg | 是 | String | 消息内容 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20201027142251106"
    }
```

---

## 激活码发货

**请求URL：** `/DummySend/ActivationCodeSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| activationCode | 是 | String | 激活码 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20201027142251106"
    }
```

---

## 电子面单云打印接口 

**简要描述：** 电子面单云打印接口

**请求URL：** `/Waybill/GetWaybill`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| sellerToken | 否 | String | 订单所属卖家的AccessToken，如果有传该参数并且Recipient为空时，会自动获取TradeOrderList的头一笔订单的收件人信息填充到Recipient |
| paramJson | 是 | String | {     "sender":{         "address":{             "city":null,             "detail":null,             "district":null,             "province":null,             "town":null         },         "mobile":"123",         "name":"123",         "phone":"123"     },     "trade_order_info_dtos":[         {             "logistics_services":null,             "object_id":null,             "order_info":{                 "order_channels_type":null,                 "trade_order_list":[                  ]             },             "package_info":{                 "goods_description":null,                 "id":null,                 "items":[                     {                         "count":0,                         "name":null                     }                 ],                 "packaging_description":null,                 "total_packages_count":null,                 "volume":null,                 "weight":null             },             "recipient":{                 "address":{                     "city":null,                     "detail":null,                     "district":null,                     "province":null,                     "town":null                 },                 "mobile":null,                 "name":null,                 "phone":null             },             "template_url":null,             "user_id":null         }     ],     "wp_code":null } |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": [
        {
            "object_id":"1",
            "parent_waybill_code":null,
            "print_data":"{
            }",
            "waybill_code":"YT45435431234777"
        }
    ],
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null
    }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Modules |  | 面单信息 |

**备注：** 参考：[电子面单云打印接口](https://open.pinduoduo.com/application/document/api?id=pdd.waybill.get) 、 [拼多多打印组件交互协议](https://open.pinduoduo.com/application/document/browse?idStr=455144ABC108ECE3)

---

## 获取所有标准电子面单模板 

**简要描述：** 获取所有标准电子面单模板

**请求URL：** `/Waybill/Stdtemplates`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| wpCode | 否 | String | 快递公司code |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": [{
        "wp_code": "YTO",
        "standard_templates": [{
            "standard_template_id": 1024,
            "standard_template_name": "YTO模板",
            "standard_template_url": "模板url",
            "standard_waybill_type": 1
        }]
    }],
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null
    }
```

**备注：** 参考：[获取所有标准电子面单模板](https://open.pinduoduo.com/application/document/api?id=pdd.cloudprint.stdtemplates.get) 、 [拼多多打印组件交互协议](https://open.pinduoduo.com/application/document/browse?idStr=455144ABC108ECE3)

---

## 获取最近一笔发送的卡密

**简要描述：** 根据订单号获取最近一笔发送的卡密

**请求URL：** `/Cpd/GetLastSentResult`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| aldsType | 是 | Int | 自动发货类型，具体查看底部备注 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
          {
            "title": "唯一卡别名",
            "cardPwdArr": [
              {
                "c": "10000004806",
                "p": ""
              },
              {
                "c": "10000004807",
                "p": ""
              }
            ]
          },
          {
            "title": "图片卡种",
            "cardPwdArr": [
              {
                "c": "http://imgcp.91kami.com/54/201908/c634af0498214e86bb0ec2f6fad5188b.png"
              }
            ]
          }
        ],
        "error_Code": 0,
        "error_Msg": ""
      }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| title | String | 卡种名称 |
| cardPwdArr | Array | 卡密数组 |
| c | String | 卡号 |
| p | String | 卡券 |

**备注：** aldsType自动发货类型：付款后发货=1，确认收货后赠送=2

---

## 订单发货

**简要描述：** 订单发货通知

**请求URL：** `/Logistics/LogisticsOnlineSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| orderSn | 是 | String | 订单号 |
| logisticsId | 是 | Long | 快递公司编号 |
| trackingNumber | 是 | String | 快递单号 |
| feature | 否 | String | 发货个性内容，支持imei（手机串号），deviceSn（设备序列号）内容。形如：imei=11,22,3333; 以 “imei=” 开头，以英文分号“;”结尾，中间为手机IMEI串号信息，多个串号以英文逗号 “,”拼接释义：该订单包含三个手机IMEI串号，分别为11、22和3333；其他内容的格式同理。 |
| refundAddressId | 否 | String | 退货地址的id，不填则取商家默认地址 |

**返回示例：**

```json
{
      "IsSuccess": false,
      "Data": null
      "Error_Code": 15,
      "Error_Msg": "发货失败"
    }
```

**备注：** 参考文档订单发货通知接口

---

## 订单备注

**简要描述：** 订单备注

**请求URL：** `/Trade/Remark`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| remark | 否 | String | 备注内容 |
| flag | 否 | int | 旗帜，1：红色，2：黄色，3：绿色，4：蓝色，5：紫色，6：橙色，7：浅蓝色，8：浅粉色，9：深绿色，10：桃红色 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20201027142251106"
    }
```

---

## 订单查询

**简要描述：** 根据订单号，查询订单信息

**请求URL：** `/Trade/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
            "buyer_memo": "",                          // 买家留言信息
            "after_sales_status": 0,   // 售后状态 0：无售后 2：买家申请退款，待商家处理 3：退货退款，待商家处理 4：商家同意退款，退款中 5：平台同意退款，退款中 6：驳回退款，待买家处理 7：已同意退货退款,待用户发货 8：平台处理中 9：平台拒绝退款，退款关闭 10：退款成功 11：买家撤销 12：买家逾期未处理，退款失败 13：买家逾期，超过有效期 14：换货补寄待商家处理 15：换货补寄待用户处理 16：换货补寄成功 17：换货补寄失败 18：换货补寄待用户确认完成 21：待商家同意维修 22：待用户确认发货 24：维修关闭 25：维修成功 27：待用户确认收货 31：已同意拒收退款，待用户拒收 32：补寄待商家发货
            "confirm_status": 1,                       // 成交状态：0：未成交、1：已成交、2：已取消
            "confirm_time": "2022-03-16 17:29:33",     // 成交时间
            "created_time": "2022-03-16 17:29:26",     // 创建时间
            "gift_list": [],                           // 赠品列表
            "item_list": [                             // 订单中商品sku列表
              {
                "goods_id": "246872501254",            // 商品编号
                "sku_id": "862379145877",              // 商品规格编码
                "outer_id": "1252",                    // 商家外部编码（sku），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。
                "outer_goods_id": "2252",              // 商家外部编码（商品），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。
                "goods_name": "照片素材材料印刷彩印新鹏线下各门店使用",  // 商品名称
                "goods_price": 0.1,                    // 商品销售价格
                "goods_spec": "A4,1张1寸体验装",        // 商品规格，使用（规格值1,规格值2）组合作为sku的表示，中间以英文逗号隔开
                "goods_count": 1,                      // 商品数量
                "goods_img": "https://img.pddpic.com/mms-material-img/2021-05-24/5f2605a7-35ed-4415-9385-5fd97f68fd23.jpeg.a.jpeg"   // 商品图片
              }
            ],
            "goods_amount": 0.1,                       // 商品金额（元）商品金额=商品销售价格*商品数量-订单改价折扣金额
            "pay_amount": 0.1,                         // 支付金额（元）支付金额=商品金额-折扣金额+邮费
            "pay_time": "2022-03-16 17:29:32",         // 支付时间
            "refund_status": 1,                        // 退款状态，枚举值：1：无售后或售后关闭，2：售后处理中，3：退款中，4： 退款成功
            "remark": "",                              // 商家订单备注
            "remark_tag": 0,                           // 订单备注标记，1-红色，2-黄色，3-绿色，4-蓝色，5-紫色
            "remark_tag_name"                          // 订单备注标记名称
          },
          "Error_Code": 0,  
          "Error_Msg": ""
          "AllowRetry": null,
          "RequestId": "20220322142251106"
        }
```

---

## 订单详情

**简要描述：** 订单详情

**请求URL：** `/Order/OrderInformation`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| orderSn | 是 | String | 订单号 |

**返回示例：**

```json
{
        "IsSuccess":true,
        "Data":{
            "order_info":{
                "pre_sale_time":null,
                "is_pre_sale":0,
                "invoice_status":0,
                "buyer_memo":"",
                "inner_transaction_id":"",
                "cat_id_1":8721,
                "cat_id_2":8749,
                "cat_id_3":8929,
                "cat_id_4":0,
                "stock_out_handle_status":-1,
                "is_stock_out":0,
                "country_id":0,
                "province_id":0,
                "city_id":0,
                "town_id":0,
                "receive_time":null,
                "order_sn":"200601-338104320801429",
                "trade_type":0,
                "confirm_time":"2020-06-01T19:00:23",
                "created_time":"2020-06-01T18:59:30",
                "country":"中国",
                "province":"",
                "city":"",
                "town":"",
                "address":"",
                "receiver_name":"",
                "receiver_phone":"",
                "pay_amount":0.1,
                "goods_amount":0.1,
                "discount_amount":0,
                "pay_no":"",
                "postage":0,
                "pay_type":"",
                "id_card_num":"",
                "id_card_name":"",
                "logistics_id":"999",
                "traking_number":null,
                "shipping_time":"2020-06-01T19:00:37",
                "order_status":2,
                "is_lucky_flag":1,
                "refund_status":1,
                "updated_at":"2020-06-01T19:00:37",
                "last_ship_time":"2020-06-03T19:00:23",
                "remark":"",
                "item_list":[
                    {
                        "goods_id":"245125",
                        "sku_id":"6386975",
                        "outer_id":"tes-01",
                        "outer_goods_id":"tet01",
                        "goods_name":"洗车抵用券",
                        "goods_price":0.1,
                        "goods_spec":"50元在线抵用券",
                        "goods_count":1,
                        "goods_img":""
                    }
                ],
                "platform_discount":0,
                "seller_discount":0,
                "capital_free_discount":0,
                "after_sales_status":0,
                "risk_control_status":0
            }
        },
        "Error_Code":0,
        "Error_Msg":"",
        "AllowRetry":null
    }
```

**备注：** 参考文档订单详情

---

## 重置每日退款限制

**简要描述：** 触发每日退款限制时，可通过此接口进行重置。

**请求URL：** `/Refund/ResetLimit`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| code | 是 | String | 短信验证码 |

**返回示例：**

```json
{
        "isSuccess": true,
        "error_Code": 0,
        "error_Msg": ""
    }
```

**备注：** 注：短信验证码可通过，发送重置退款限制短信接口获取。

---
