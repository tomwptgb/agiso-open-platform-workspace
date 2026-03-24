# 微信小店自动发货 (AldsWxVideoShop) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsWxVideoShop/`

---

## 发送短信

**简要描述：** 根据订单号，发送短信

**请求URL：** `/Sms/SendSms`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| templateId | 是 | Long | 模板Id(Sms/GetSmsTemplates接口返回的Id) |
| templateParam | 是 | string | 模板参数,替换短信模板里的占位符，示例:短信模板内容为：订单尾号${orderSn}已发货，卡号：${cardNo}。请妥善保管，传递：{'orderSn':'123','cardNo':'xxx'}会将对应的占位符替换，输出内容：订单尾号123已发货，卡号：xxx。请妥善保管 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "message_id": "897223057406534192^0", // 调用短信接口成功返回的消息Id
            "success": true // 是否调用成功
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 发送短信(根据短信模板Id)

**简要描述：** 根据订单号，发送短信

**请求URL：** `/Sms/SendSmsByTplId`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| templateId | 是 | String | 短信模板Id |
| templateParam | 是 | string | 模板参数,替换短信模板里的占位符，示例:短信模板内容为：恭喜您成功购买了${groupName}课程，请尽快兑换课程权限：下载CCtalk App，注册登陆，复制兑换码 ${code}后，再次打开app，即可开通学习！若已兑换，请忽略。传递：{'groupName':'学习','code':'xxx'}会将对应的占位符替,输出内容:换恭喜您成功购买了学习课程，请尽快兑换课程权限：下载CCtalk App，注册登陆，复制兑换码 xxx后，再次打开app，即可开通学习！若已兑换，请忽略。 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "message_id": "897223057406534192^0", // 调用短信接口成功返回的消息Id
            "success": true // 是否调用成功
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 商品详情

**简要描述：** 根据微信小店商品Id，查询商品详情。

**请求URL：** `/Product/Details`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| productId | 是 | String | 微信小店商品Id |

**返回示例：**

```json
{
    "isSuccess": true,
    "data": {
      "product_id": "10000043902725",           // 商品ID。
      "out_product_id": "",                     // 商家自定义商品ID。
      "title": "标签贴纸便利贴全粘式自粘索引贴",   // 商品标题
      "sub_title": "",                          // 商品副标题
      "head_imgs": [                            // 主图 Url 列表
        "https://mmecimage.cn/p/wxbc71ad7b270355e6/HN1nr3DMxXmtFZV2Iq0Wm4hXX7QKxQmE5SKeBR7_LA",
      ],
      "deliver_method": 0,                      // 发货方式：0-快递发货；1-无需快递，默认为0，若为无需快递，则无需填写运费模版id
      "express_info":                           // 运费
      {
          "template_id": "238528452004",        // 运费模板ID。如果添加时没录入，回包可能不包含该字段。
          "weight": 0                           // 商品重量，单位克。
      },
      "aftersale_desc": "",                     // 售后说明
      "status": 5,                              // 0-初始值，5-上架，6-回收站，9-逻辑删除，11-自主下架，12-售罄下架，13-违规下架/风控系统下架。
      "path": "",                               // 小程序页面路径。
      "min_price": 1,                           // SKU 最低价格（单位：分）。
      "cats": [                                 // 商品类目列表。
        {
          "cat_id": "6706"                      // 商品类目 ID。
        },
      ],
      "attrs": [                                // 商品属性列表。
        {
          "attr_key": "规格",                   // 属性的 Key。
          "attr_value": "张"                    // 属性的值。
        },
      ]
      "spu_code": "dx",                         // 商品编码。
      "brand_id": "2100000000",                 // 品牌id，无品牌为“2100000000”。
      "skus":[                                  // sku列表。
        {
          "sku_id": "1247535030",               // SKU ID。
          "out_sku_id": "",                     // 商家自定义skuID。如果添加时没录入，回包可能不包含该字段。
          "thumb_img": "",                      // sku小图。如果添加时没录入，回包可能不包含该字段。
          "sale_price": 1,                      // 售卖价格，以分为单位。
          "stock_num": 96,                      // sku库存。
          "sku_code": "d1",                     // sku编码。如果添加时没录入，回包可能不包含该字段。
          "sku_attrs":                          // sku属性。
          [
              {
                  "attr_key": "大小",           // 属性的 Key。
                  "attr_value": "大"            // 属性的值。
              }
          ],
          "status": 5,                          // 0-初始值，5-上架，6-回收站，9-逻辑删除，11-自主下架，12-售罄下架，13-违规下架/风控系统下架。
          "sku_deliver_info":                   // sku物流信息
          {
              "stock_type": 0,                   // sku库存情况。0:现货（默认），1:全款预售。部分类目支持全款预售，具体参考文档获取类目信息中的字段attr.pre_sale
              "full_payment_presale_delivery_type": 0, // sku发货节点，该字段仅对stock_type=1有效。0:付款后n天发货，1:预售结束后n天发货
              "presale_begin_time": 0,           // sku预售周期开始时间，秒级时间戳，该字段仅对delivery_type=1有效。
              "presale_end_time": 0,             // sku预售周期结束时间，秒级时间戳，该字段仅对delivery_type=1有效。
              "full_payment_presale_delivery_time": 0 // sku发货时效，即付款后/预售结束后{full_payment_presale_delivery_time}天内发货，该字段仅对stock_type=1时有效。
          }
        },
      ],
    },
    "error_Code": 0,
    "error_Msg": ""
  }
```

**备注：** 参考官方：[获取商品详情](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/ministore/minishopopencomponent/API/spu/get_spu.html)

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

## 查询短信模板

**简要描述：** 查询可用的短信模板

**请求URL：** `/Sms/GetSmsTemplates`

**请求方式：** POST

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
          {
            "id": 3, // 发送短信时,使用的模板ID
            "name": "卡号场景",
            "tpl_type": 1, // 0:发提取网站,1:发卡号,2:发卡号和密码
            "tpl_content": "订单尾号{#订单尾号}已发货，卡号：{#卡号}。请妥善保管(公共模版)",
            "platform_tpl_content": "订单尾号#{orderSn}已发货，卡号：#{cardNo}。请妥善保管", // 实际发送的内容(调用发送短信接口是使用文本里对应的参数传值:orderSn,cardNo)
            "create_time": "2025-07-04 14:47:32"
          },
          {
            "id": 4, // // 发送短信时,使用的模板ID
            "name": "卡号和卡密场景",
            "tpl_type": 2, // 0:发提取网站,1:发卡号,2:发卡号和密码
            "tpl_content": "订单尾号{#订单尾号}已发货，卡号：{#卡号}。请妥善保管(公共模版)",
            "platform_tpl_content": "订单尾号#{orderSn}的卡号：#{cardNo} 密码：#{pwd} 请妥善保管", // 实际发送的内容(调用发送短信接口是使用文本里对应的参数传值:orderSn,cardNo,pwd)
            "create_time": "2025-07-04 14:47:32"
          }
        ],
        "error_Code": 0,
        "error_Msg": ""
      }
```

---

## 获取短信发送结果

**简要描述：** 根据订单号，获取短信发送结果

**请求URL：** `/Sms/GetSmsSendResult`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
            {
                "send_time": "2025-09-09 16:28:54",                                         // 发送时间
                "sms_content": "【阿奇索】订单尾号123已发货，提取网址：http://91kami.cn/xxss", // 短信内容
                "status": "3",                                                              //未回执：1 发送失败：2 发送成功：3
                "count": "1",                                                               // 计费条数，如果短信过长，会分多次计费
                "code": "DELIVERED",                                                        //错误码
                "message": "DELIVERED",                                                     // 错误说明
                "message_id": "897223057406534192^0",                                       // message_id
                "phone": "187****5711",                                                     // 手机号
                "tag": "WxVideoShop_gh_3587c6da8674"                                        // 透传字段
            }
        ],
        "error_Code": 0,
        "error_Msg": ""
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
            "order_id": 3713475752656242688,       // 订单号
            "create_time": 1691395994,             // 订单创建时间，时间戳，秒
            "update_time": 1691568871,             // 订单更新时间，时间戳，秒
            "status": 200,                         // 10：待付款、15：拼团活动支付成功等待成团中、16：支付成功等待商家接单中同城配送线下自提、17：支付成功待核销、20：待发货、21：部分发货、30：待收货、100：完成、200：全部商品售后之后订单取消、250：用户主动取消或待付款超时取消
            "order_detail": {                      // 订单详情
              "product_infos":[                    // 商品信息列表
                {
                  "product_id": "10000043902725",  // 商品id
                  "sku_id": "1247535030",          // skuId
                  "thumb_img": "https://store.mp.video.tencent-cloud.com/161/20304/snscosdownload/SH/reserved/6477f2ce00065ae3250b09a6bc34b00b000000a000004f50",          // 缩略图
                  "sale_price": 1,                // 售卖价格（单位：分）
                  "sku_cnt": 1,                   // sku数量
                  "on_aftersale_sku_cnt": 0,      // 正在售后/退款流程中的sku数量
                  "finish_aftersale_sku_cnt": 1,  // 完成售后/退看的sku数量
                  "sku_code": "d1",               // 商品编码
                  "market_price": 1,              // 市场价格（单位：分）
                  "sku_attrs": [                  // 商品属性列表
                    {
                      "attr_key": "大小",         // 属性key
                      "attr_value": "大",         // 属性的值
                    }
                  ],
                  "real_price": 1,                // sku实付价格，取estimate_price和change_price中较小值
                  "out_product_id":"",            // 商品外部spuid
                  "out_sku_id":"",                // 商品外部skuid
                  "is_discounted":false,          // 是否有优惠金额，非必填，默认为false
                  "estimate_price":false,         // 优惠后sku价格，非必填，is_discounted为true时有值
                  "is_change_price":false,        // 是否修改过价格，非必填，默认为false
                  "change_price":false,           // 改价后sku价格，非必填，is_change_price为true时有值
                  "out_warehouse_id": "",         // 区域库存id
                },
              ],
              "price_info": {                        // 商品金额信息。
                "product_price": 1,                  // 商品金额（单位：分）。
                "order_price": 1,                    // 订单金额（单位：分）。
                "freight": 0                         //  运费（单位：分）。
              },
              "pay_info": {                          // 支付信息
                "pay_time": 1691396011,              // 支付时间，时间戳，秒。
                "pay_method": "1",                   // 支付方式1 - 微信支付、2 - 先用后付、3 - 抽奖商品0元订单。
              },
              "delivery_info": {                     // 快递信息
                "deliver_method": 0,                 // 订单发货方式，0：普通物流，1：虚拟发货，由商品的同名字段决定。
                "ship_done_time": 1691396013,        // 发货完成时间，时间戳，秒。
              },
              "ext_info": {
                "customer_notes": "",                // 顾客备注。
                "merchant_notes": "",                // 商家备注。
              }
            },
            "aftersale_detail": {                    // 售后详细信息。
              "on_aftersale_order_cnt": 0,           // 正在售后流程的售后单数。
              "aftersale_order_list": [              // 售后单列表
                {
                  "aftersale_order_id": "2000000075529920",  // 售后单 ID
                }
              ],
            },
          },
          "Error_Code": 0,
          "Error_Msg": ""
          "AllowRetry": null,
          "RequestId": "20220322142251106"
        }
```

**备注：** 参考官方：[获取订单详情](https://developers.weixin.qq.com/doc/channels/API/order/get.html)

---
