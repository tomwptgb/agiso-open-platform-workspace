# 闲鱼自动发货 (AldsIdle) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsIdle/`

---

## 关闭订单

**简要描述：** 关闭订单

**请求URL：** `/Order/CloseOrder`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| reason | 是 | String | 关闭原因 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 发布的商品列表

**简要描述：** 为服务商的卖家提供发布的闲鱼商品列表

**请求URL：** `/Product/GetList`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| page_no | 否 | Number | 页号 |
| page_size | 否 | Number | 页大小（最大值200） |
| status | 否 | List<string> | 商品状态 0:在线 1售出 注意：对于列表类型传多个值的情况，可以添加多个相同键(status),不同值来传递。        完整的参数请求示例：       param1:page_no = 1       param2:page_size = 10       param3:status = 0       param4:status = 1 |

**返回示例：**

```json
{
    "isSuccess": true,
    "data": {
      "item_list": [                   // 商品列表
        {
          "auction_type": "b",         // 商品类型： b 一口价；a 拍卖
          "category_id": "50023914",   // 商品类目
          "division_id": 350211,       // 行政区划Id(城市编码)，最小行政单位code，若是地区级别，则为地区级别的id；否则为城市级别的id(long型，6位)
          "img_urls": [                // 商品图片
            "http://img.alicdn.com/bao/uploaded/i1/O1CN01PNqI1P1OaGOLMx2dF_!!0-fleamarket.jpg"
          ],
          "item_biz_type": 0,                // 业务模式 0不入仓，1入仓，2 C2C; （经常会新增，具体参见接入文档）
          "item_id": 677585043507,           // 商品ID
          "original_price": "0.00",          // 商品原价, 单位：元(最大99999999)
          "reserve_price": "0.01",           // 商品价格
          "seller_nick": "爱***网",           // 卖家昵称（不唯一且用户可以自己更改）
          "status": 0,                        // 商品状态，可选值为0（表示上架），-2（表示下架），-1（表示删除），99（其他）
          "stuff_status": 90,                 // 商品新旧程度, 值为-1～100的整数，例如100代表全新，95代表95新，-1比较特殊代表准新
          "title": "#粉丝福利# 全店统一测试"    // 商品标题
        }
      ],
      "next_page": false,                    // 是否有下一页
      "total": 1                             // 总数
    },
    "error_Code": 0,
    "error_Msg": ""
  }
```

**备注：** 参考咸鱼：[闲鱼已验货订单查询](https://open.taobao.com/api.htm?docId=56245&docType=2&source=search)

---

## 发送助手IM消息接口

**简要描述：** 发送助手IM消息接口（注：助手不在线最多投送三次，投送间隔1、3、5分钟。同一条消息仅投送一次。）

**请求URL：** `/Assistant/SendImMsg`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| platformShopId | 是 | String | 店铺id |
| msgId | 是 | String | 助手推送的原始消息id，表示是对该消息进行回复 |
| content | 是 | String | 消息内容，json字符串  支持单独发文本或者图片，也支持同时发送图文，内容格式：   {      "text": "消息内容", //要发的文本内容， 非必填，长度限制1000字符内      "images": [          "http://img.alicdn.com/bao/uploaded/i1/O1CN01mPM33A2CP1bgJGkgt_!!2-fleamarket.jpg",          "https://gw.alicdn.com/bao/uploaded/i3/O1CN01HOnhmf1OaGgk0eMSl_!!4611686018427385769-2-fleamarket.jpg"      ]  // 要发的图片URL， 非必填，限制10张内，图片格式限制PNG、JPG  } |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20221027142251106"
    }
```

---

## 发送消息

**简要描述：** 发送聊天窗口消息

**请求URL：** `/ImMsg/SendMsg`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| msg | 是 | String | 消息内容（长度限制1000，一笔订单限制5条） |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20221027142251106"
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
      "error_Msg": "",
      "requestId": "20220822142251106"
    }
```

**备注：** 注：店铺需要绑定91卡密，短信发送到绑定91卡密预留手机号码。

---

## 同意退款

**简要描述：** 同意退款

**请求URL：** `/Refund/AgreeRefund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

**返回示例：**

```json
{
        "isSuccess": true,
        "error_Code": 0,
        "error_Msg": "",
        "allowRetry": null,
        "requestId": "20222087142251106"
    }
```

---

## 商品下架

**简要描述：** 商品下架接口

**请求URL：** `/Product/DownShelf`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| item_id | 是 | Long | 商品ID |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 商品详情

**简要描述：** 根据闲鱼商品Id，查询商品详情。

**请求URL：** `/Product/Details`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| item_id | 是 | Number | 闲鱼商品Id |
| need_sku | 否 | Boolean | 是否需要sku信息(不需要的业务场景，不要设置为true，会增加查询耗时) |

**返回示例：**

```json
{
    "isSuccess": true,
    "data": {
      "auction_type": "b",                       // 商品类型： b 一口价；a 拍卖
      "category_id": 50023914,                   // 类目Id
      "desc": "感兴趣的话点“我想要”和我私聊吧～",   // 商品描述(长度<=5000)
      "division_id": 350211,                     // 行政区划Id(城市编码)，最小行政单位code，若是地区级别，则为地区级别的id；否则为城市级别的id(long型，6位)
      "img_urls": [                              // 图片
        "http://img.alicdn.com/bao/uploaded/i1/O1CN01PNqI1P1OaGOLMx2dF_!!0-fleamarket.jpg"
      ],
      "item_biz_type": 0,                        // 业务模式 0不入仓，1入仓，2寄卖
      "item_id": 677585043507,                   // 商品Id（long型）
      "item_sku_list": [                         // sku列表
        {
          "outer_id": "2342345456",              // 外部商家标识(商品编码对接ERP等)
          "price": 1,                            // 价格，单位分
          "property_list": [                     // 销售属性列表(最多2个销售属性,每一个的属性值个数为2～10)
            {
              "property_text": "尺码",           // 属性名文本
              "value_text": "XL"                 // 属性值文本
            }
          ],
          "quantity": 0,                        // 库存
          "sku_id": 0                           // skuId
        }
      ],
      "item_tags": [],                         // 商品业务标签，不可修改
      "original_price": "0.00",                // 商品原价, 单位：元(最大99999999)
      "quantity": 193,                         // 商品库存
      "reserve_price": "0.01",                 // 商品售价, 单位：元(最大99999999)
      "status": 0,                             // 商品状态，可选值为0（表示上架），-2（表示下架），-1（表示删除），99（其他）
      "stuff_status": 90,                      // 商品新旧程度, 值为0-100的整数，例如100代表全新，95代表95新
      "title": "#粉丝福利# 全店统一测试",        // 商品标题
      "trade_type": 0,                         // 交易方式, 仅在线交易: 0,仅线下交易: 1,线上OR线下交易: 2（int型，1位）
      "transport_fee": "0.00",                 // 邮费, 单位：元(最大99999999)
      "white_bg_img_urls": []                  // 商品白底图
    },
    "error_Code": 0,
    "error_Msg": ""
  }
```

**备注：** 参考咸鱼：[服务商闲鱼商品查询](https://open.taobao.com/api.htm?docId=49488&docType=2&source=search)

---

## 囤囤券发码

**简要描述：** 囤囤券发码

**请求URL：** `/Eticket/EticketMaOnlySend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| couponEticketStr | 是 | String | 发码json串(列表的序列化),示例:[{"CodeId":"ET20260114001","CodePassword":null,"CodeType":1,"CodeUseUrl":"https://coupon.taobao.com/use?code=ET20260114001"}] |
| couponEticket[].CodeId | 是 | String | 码id  注意:这里是couponEticketStr参数里对象的属性说明 |
| couponEticket[].CodePassword | 否 | String | 密码，没有可以为空 注意:这里是couponEticketStr参数里对象的属性说明 |
| couponEticket[].CodeType | 是 | Long | 码类型，1:码,2:卡密 注意:这里是couponEticketStr参数里对象的属性说明 |
| couponEticket[].CodeUseUrl | 是 | String | 使用链接 注意:这里是couponEticketStr参数里对象的属性说明 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 囤囤券发货发码

**简要描述：** 囤囤券发货发码

**请求URL：** `/Eticket/EticketMaSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| couponEticketStr | 是 | String | 发码json串(列表的序列化),示例:[{"CodeId":"ET20260114001","CodePassword":null,"CodeType":1,"CodeUseUrl":"https://coupon.taobao.com/use?code=ET20260114001"}] |
| couponEticket[].CodeId | 是 | String | 码id  注意:这里是couponEticketStr参数里对象的属性说明 |
| couponEticket[].CodePassword | 否 | String | 密码，没有可以为空 注意:这里是couponEticketStr参数里对象的属性说明 |
| couponEticket[].CodeType | 是 | Long | 码类型，1:码,2:卡密 注意:这里是couponEticketStr参数里对象的属性说明 |
| couponEticket[].CodeUseUrl | 是 | String | 使用链接 注意:这里是couponEticketStr参数里对象的属性说明 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 囤囤券更新码状态

**简要描述：** 囤囤券更新码状态

**请求URL：** `/Eticket/EticketUpdateStatus`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| codeId | 是 | String | 核销码 |
| codeStatus | 是 | Int | 核销码状态,状态，1:未使用,2:已使用，3:过期，4:作废 |
| codeType | 否 | Int | 核销码类型,码类型，1:码,2:卡密 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 囤囤券退款

**简要描述：** 囤囤券退款

**请求URL：** `/Eticket/EticketRefund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| refundId | 是 | Long | 退款Id |
| refundOperation | 是 | String | 退款操作，支持：AGREE_REFUND(同意退款)，REFUSE_REFUND(拒绝退款) |
| requestType | 是 | String | 请求类型, 支持:unuse_refund(未使用自动退), expire_refund(过期自动退) |
| leaveMessage | 否 | String | 退款说明 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20221027142251106"
    }
```

---

## 执行自动发货

**简要描述：** 调用该接口将根据您在自动发货后台设定的发货规则，进行一次发货逻辑的处理。该操作等同于在[手动发货页面](https://aldsidle.agiso.com/#/alds/manualSend)的操作。注意：该页面执行后，也会自动发送闲鱼消息，可以通过参数中的选项控制发货中的一些限制。

**请求URL：** `/Alds/AldsSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tids | 是 | String | 订单编号,多个订单编号间用,分隔开 |
| ignoreAldsLog | 否 | Boolean | 忽略发货记录            默认值:'false',可选值'true'、'false' |
| ignoreBlackList | 否 | Boolean | 忽略黑名单            默认值:'false',可选值'true'、'false' |
| ignoreOnOff | 否 | Boolean | 忽略发货开关            默认值:'false',可选值'true'、'false' |
| ignoreRefundCheck | 否 | Boolean | 退款中也发            默认值:'false',可选值'true'、'false' |
| ignoreRestricted | 否 | Boolean | 忽略限拍限购            默认值:'false',可选值'true'、'false' |
| ignoreTradeStatusCheck | 否 | Boolean | 忽略订单状态验证            默认值:'false',可选值'true'、'false' |
| aldsType | 是 | Int | 自动发货类型，具体查看底部备注 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

**备注：** aldsType自动发货类型：付款后发货=1，确认收货后赠送=2

---

## 拒绝退款

**简要描述：** 拒绝退款

**请求URL：** `/Refund/RefuseRefund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| refuseMsg | 否 | String | 拒绝退款的原因说明 |

**返回示例：**

```json
{
        "isSuccess": true,
        "error_Code": 0,
        "error_Msg": "",
        "allowRetry": null,
        "requestId": "20222087142251106"
    }
```

---

## 撤销商品囤囤券标识

**简要描述：** 撤销商品囤囤券标识

**请求URL：** `/Eticket/CancelEticket`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| itemId | 是 | Long | 商品Id |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 更新发货状态

**简要描述：** 执行无物流发货，更新发货状态

**请求URL：** `/Order/DummySend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 标识囤囤券商品

**简要描述：** 标识囤囤券标识或者编辑囤囤券设置

**请求URL：** `/Eticket/EditEticket`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| itemId | 是 | Long | 商品Id |
| ticketEffectiveTimeMode | 是 | Long | 生效时间模式(0 固定时间(设置固定的到期时间),1 相对时间(设置有效天数)) |
| ticketRelativeEffectiveTime | 否 | Long | 有效期(天数7-90天之内),TicketEffectiveTimeMode=1时必填 |
| ticketEffectiveEndTime | 否 | Datetime | 固定失效时间,TicketEffectiveTimeMode=0时必填,格式:yyyy-MM-dd HH:mm:ss |
| supportUnUseAutoRefund | 是 | Bool | 是否支持未使用随时退(必须支持) |
| supportExprieAutoRefund | 是 | Bool | 是否支持超时自动退 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null
      "Error_Code": 0,
      "Error_Msg": ""
      "AllowRetry": null,
      "RequestId": "20221027142251106"
    }
```

---

## 直充订单发货

**简要描述：** 直充订单发货（通知平台充值成功）

**请求URL：** `/Order/RechargeSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 直充订单退款

**简要描述：** 直充订单退款（通知平台充值失败）

**请求URL：** `/Order/RechargeRefund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 获取商品分类信息列表

**请求URL：** `/Product/CategoryList`

**请求方式：** Post

**返回示例：**

```json
{
    "isSuccess": true,
    "data": [
      {
        "value": 25,
        "label": "卡券",
        "children": [
          {
            "value": "fd437e67a3f106f3e8b3e6ac99cf3e83",
            "label": "卡券充值",
            "children": [
              {
                "value": "7797f5f563de5f13f7c9b3ea5c0fc18b",
                "label": "虚拟币",
                "children": [
                  {
                    "value": "869e12180b92e789ac899d2620c5df2b",
                    "label": "3DQQ秀",
                    "category_id": 50025461,
                    "is_recharge": 0
                  }
                ]
              }
            ]
          }
        ],
        "is_dist": 0,
        "is_yx": 0,
        "recruit_link": ""
      }
    ],
    "error_Code": 0,
    "error_Msg": ""
  }
```

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

## 订单价格修改

**简要描述：** 订单价格修改接口

**请求URL：** `/Order/AdjustPrice`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单id |
| new_price | 是 | decimal | 最新价格 |
| new_transport_fee | 是 | decimal | 最新邮费 |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": null
        "Error_Code": 0,
        "Error_Msg": ""
        "AllowRetry": null,
        "RequestId": "20221027142251106"
      }
```

---

## 订单查询

**简要描述：** 根据订单号，查询订单信息

**请求URL：** `/Order/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
            "biz_order_id": 1520087523676842500,     // 订单号
            "buy_amount": 1,                         // 商品购买数量
            "buyer_nick": "地铁吃火锅当真",           // 买家昵称（不唯一且买家可以自己更改）
            "encryption_buyer_id": "RAzN8214YLDBs4AJxFJBYp5DdeHrBPKq4QsbFL",           // 加密的买家id（唯一且不会改变）
            "create_time": 1647677835000,            // 订单创建时间,时间戳,毫秒
            "end_time": 1647677858000,               // 订单完结时间,时间戳,毫秒
            "item": {                                // 商品信息
              "item_id": 669513624774,               // 商品ID
              "pic_url": "https://gw.alicdn.com/bao/uploaded/i4/O1CN01X6Nw841OaGN6dvZtx_!!0-fleamarket.jpg", // 商品图片,绝对途径
              "price": 1,                            // 商品价格，单位分
              "title": "测试宝贝5",                   // 商品标题
              "outer_id_sku": "XY02",                // 商品外部编码（SKU维度）
              "outer_id_spu": "XY01",                // 商品外部编码（SPU维度）
            },
            "order_status": 5,                       // 0:未知状态、1：订单已创建、2：订单已付款、3：已发货、4：交易成功、5：已退款、6：交易关闭
            "pay_time": 1647677841000,               // 订单下单付款时间,时间戳,毫秒
            "payment": 1,                            // 实付金额, 单位分
            "post_fee": 0,                           // 邮费
            "seller_nick": "爱***网",                // 卖家昵称（不唯一且买家可以自己更改）
            "ship_time": 0,                          // 订单发货时间,时间戳,毫秒
            "sku": 0,                                // sku信息（格式： skuId|属性名:属性值;属性名:属性值）
            "isRecharge":true,                       // 是否直冲标识
            "recharge_amount":"135xxxx",             // 充值信息
            "isEticket":"true",                      // 是否囤囤券订单
            "coupon_eticket_info":[                  // 核销码信息(囤囤券)
              {
                "code_id":"x222223",                 // 核销码
                "code_password":"123",               // 核销码密码
                "code_status":"1",                   // 核销码状态
                "code_type":1,                       // 核销码类型
                "code_use_url":"http://localhost:26450/t/zbdjyu_9137A"  // 核销码使用链接
              }
          ]
          },
          "Error_Code": 0,
          "Error_Msg": ""
          "AllowRetry": null,
          "RequestId": "20220322142251106"
        }
```

---

## 订单退款详情查询

**简要描述：** 根据订单号，查询订单退款信息

**请求URL：** `/Refund/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
            "biz_order_id": 1520087523676842500,     // 订单号
            "buy_amount": 1,                         // 商品购买数量
            "buyer_apply_desc": "商品破损",           // 买家申请退款描述
            "buyer_apply_reason": "商品质量问题",     // 买家申请退款原因
            "buyer_apply_sub_reason": "商品问题",     // 买家退款说明,买家申请退款二级原因
            "buyer_nick": "123asdf",                 // 买家昵称（不唯一且用户可以自己更改）
            "goods_status": 4,                       // 货物状态 	4: 未发货, 6: 已发货, 1: 未收到货, 2: 已收到货, 3: 已寄回, 5: 卖家确认收货
            "item": {                                // 商品信息
                "item_id": 1234234345,               // 商品Id
                "pic_url": "http://dsfakasdf.jpg",   // 商品图片,绝对途径
                "price": 23100,                      // 商品价格，单位分
                "title": "商品标题"                   // 商品标题
            },
            "need_return_goods": false,              // 买家是否需要退货
            "order_status": 2,                       // 订单状态：null/0:未知状态, 1:订单已创建/等待买家付款, 2:订单已付款/等待卖家发货, 3:已发货/等待买家确认收货, 4:交易成功, 5:已退款, 6:交易关闭
            "payment": 23000,                        // 订单实付金额,单位分
            "refund_create_time": 1616155551128,     // 退款申请时间,时间戳,单位分
            "refund_fee": 20000,                     // 退还金额(退还给买家的金额),单位分
            "refund_id": 13423464356,                // 退款订单号
            "refund_modify_time": 1616155551128,     // 退款最新修改时间,时间戳,单位分
            "refund_status": 0,                      // 退款订单状态：1: 买家已经申请退款，等待卖家同意, 2: 卖家已经同意退款，等待买家退货, 3: 买家已经退货，等待卖家确认收货, 4: 退款关闭, 5: 退款成功, 6: 卖家拒绝退款, 8: 等待卖家确认退货地址, 9: 没有申请退款, 11: 退款结束
            "seller_agree_msg": "可以退货",           // 卖家同意退货说明
            "seller_nick": "sadfqwef",               // 卖家昵称（不唯一且用户可以自己更改）
            "seller_refuse_msg": "商品没问题",        // 卖家拒绝退款说明
            "seller_refuse_reason": "不支持退货"      // 卖家拒绝退款原因
          },
          "Error_Code": 0,
          "Error_Msg": ""
          "AllowRetry": null,
          "RequestId": "20230815142251106"
        }
```

**备注：** 参考咸鱼：[闲鱼已验货交易订单退款信息查询](https://open.taobao.com/api.htm?docId=55375&docType=2&source=search)

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
        "error_Msg": "",
        "requestId": "20220822142251106"
    }
```

**备注：** 注：短信验证码可通过，发送重置退款限制短信接口获取。

---

## 闲鱼商品价格库存编辑

**简要描述：** 闲鱼商品价格库存编辑

**请求URL：** `/Product/Edit`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| item_id | 是 | Number | 闲鱼商品Id |
| reserve_price | 是 | Boolean | 商品售价, 单位：元(最大99999999) |
| original_price | 是 | Boolean | 商品原价, 单位：元(最大99999999) |
| item_sku_list | 否 | string | 字符串JSON数组[{"price" : 1 // 价格，单位分 , sku_id : 23421354345, quantity: 1 //库存，必须是非负整数}]，注：修改SKU价格需要全量提交 |

**返回示例：**

```json
{
    "isSuccess": true,
    "error_Code": 0,
    "error_Msg": ""
  }
```

---

## 闲鱼商品发布

**简要描述：** 闲鱼商品发布

**请求URL：** `/Product/Publish`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| data | 是 | String | JSON字符串，数据格式请参考示例 |

**返回示例：**

```json
{
    "isSuccess": true,
    "error_Code": 0,
    "error_Msg": ""
  }
```

---

## 闲鱼商品属性查询

**简要描述：** 闲鱼商品属性查询

**请求URL：** `/Product/SearchPv`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| channel_cat_id | 是 | string | 叶子类目id，来源： 获取商品分类信息列表 的返回结果中最后一个层级的value字段 |
| property_id | 否 | string | 属性id |
| value_id | 否 | string | 属性值Id |

**返回示例：**

```json
{
    "isSuccess": true,
    "data": [
      {
        "propertyName": "品牌",
        "pvList": [
          {
            "propertyId": "83b8f62c43df34e6",
            "propertyName": "品牌",
            "channelCatId": "f3dc5bb21a7cbfe9b108d382c4e6ea42",
            "valueId": "65f50b194511b0db",
            "valueName": "肯德基",
            "showSubProperty": true
          },
          {
            "propertyName": "适用门店",
            "pvList": []
          },
        ]
      }
    ],
    "error_Code": 0,
    "error_Msg": ""
  }
```

**备注：** showSubProperty为是否包含子属性，如果有则需要把选中的属性ID和值ID再次查询

---

## 闲鱼商品编辑

**简要描述：** 闲鱼商品编辑

**请求URL：** `/Product/FullEdit`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| data | 是 | String | JSON字符串，数据格式请参考示例 |

**返回示例：**

```json
{
    "isSuccess": true,
    "error_Code": 0,
    "error_Msg": ""
  }
```

---

## 闲鱼图片上传

**简要描述：** 闲鱼图片上传

**请求URL：** `/Product/MediaUpload`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| file | 是 | file | 文件对象 |

**返回示例：**

```json
{
    "isSuccess": true,
    "data":0,
    "error_Code": 0,
    "error_Msg": ""
  }
```

---

## 闲鱼行政区划

**简要描述：** 闲鱼行政区划

**请求URL：** `/Product/Division`

**请求方式：** Post

**返回示例：**

```json
{
   "IsSuccess": true,
   "Data": {
     "id": 110000,                            // 主键ID
     "parentId": 100000,                      // 父级ID，即如果当前是市，则父级ID就是对应的省的区域ID
     "name": "北京",                           // 当前区域的名称
     "mergerName": "中国,北京",                // 省市区合并后的全称，每一级用逗号隔开
     "shortName": "北京市",                    // 当前区域的简称，去掉 省、市、县 等字眼
     "mergerShortName": "中国,北京市",         // 合并后的简称，去掉省、市、县等字眼，每一级用逗号隔开
     "levelType": 1,                         //  级别，1-省，2-市，3-区县/span>
     "cityCode": 010,                         // 城市码
     "children":[                  // 下一级的区域合集 使用递归结构
       {
          "id": 110100,                            // 主键ID
          "parentId": 110000,                      // 父级ID，即如果当前是市，则父级ID就是对应的省的区域ID
          "name": "北京市",                           // 当前区域的名称
          "mergerName": "中国,北京,北京市",                // 省市区合并后的全称，每一级用逗号隔开
          "shortName": "北京市",                    // 当前区域的简称，去掉 省、市、县 等字眼
          "mergerShortName": "中国,北京市,北京市",         // 合并后的简称，去掉省、市、县等字眼，每一级用逗号隔开
          "levelType": 2,                         //  级别，1-省，2-市，3-区县/span>
          "cityCode": 010,                         // 城市码
          "children":[]                            // 下一级的区域合集 使用递归结构             
       }
   ]
 }
```

---
