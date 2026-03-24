# 快手自动发货 (AldsKwai) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsKwai/`

---

## 娱乐会员-取消直充订单（退款）

**简要描述：** 娱乐会员-取消直充订单（退款）

**请求URL：** `/VipOilCard/CancelTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ksOrderId | 是 | Number | 订单编号(在快手小店后台能看到的订单号) |
| reason | 是 | String | 取消原因 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null,
    "RequestId": "20220322142251106"
  }
```

---

## 娱乐会员-完成直充订单（发货）

**简要描述：** 娱乐会员-完成直充订单（发货）

**请求URL：** `/VipOilCard/FinishTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ksOrderId | 是 | Number | 订单编号(在快手小店后台能看到的订单号) |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null,
    "RequestId": "20220322142251106"
  }
```

---

## 执行发货

**简要描述：** 物流更新

**请求URL：** `/Order/DummySend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 店铺订单号 |
| expressNo | 否 | String | 快递单号 |
| expressCode | 否 | Int | 快递公司code |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": null,
          "Error_Code": 0,
          "Error_Msg": "",
          "AllowRetry": null,
          "RequestId": "20220322142251106"
        }
```

**备注：** 快递单号及快递公司code为空时，默认使用订单Id当作快递单号，快递公司Code使用9999(其他)。

---

## 订单查询

**简要描述：** 根据订单号，查询订单信息

**请求URL：** `/Order/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 店铺订单号 |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
              "orderBaseInfo":{
                "oid":2215900041470428,        // 订单id
                "payTime":1654661152607,       // 付款时间
                "buyerNick":"D**",          // 买家昵称
                "sellerOpenId":"f198e61793ab2da214bf5724a6dece4f",   // 卖家id
                "sellerNick":"PRO个性定制",     // 卖家昵称
                "expressFee":0,                // 运费
                "discountFee":0,               // 促销减价、折扣价格
                "totalFee":20,                 // 子订单商品总价
                "status":40,                   // 订单状态：[0, "未知状态"], [10, "待付款"], [30, "已付款"], [40, "已发货"], [50, "已签收"], [70, "订单成功"], [80, "订单失败"];
                "sendTime":1654661155041,      // 发货时间
                "refundTime":0,                // 退款时间
                "createTime":1654661142714,    // 创建时间
                "updateTime":1656390182523,    // 更新时间
                "remark":"",                   // 买家留言
                "theDayOfDeliverGoodsTime":120, // 发货间隔时间，单位：天
                "preSale":0,                   // 预售：preSale 0：非预售 1:预售
                "recvTime":0,                  // 收货时间
                "coType":0,                    // UNKNOWN = 0; JD = 1; RECHARGE_MOBILE = 2; // 券包 COUPON_PACKAGE = 3； // 话费充值 MI = 5; // 小米 CROSS_BORDER = 8; // 跨境
                "commentStatus":0,             // 评价状态： 0未评价，1评价    
                "payType":2,                   // 支付方式，1=微信；2=支付宝
                "riskCode":0                   // 风险Code码，10001=黑产订单，不建议商家发货  
            },
            "orderItemInfo":{
                "skuId":888390671925,          // 快手商品skuid  
                "relSkuId":0,                  // 服务商商品skuid
                "skuDesc":"按压式真空酒塞",     // sku描述   
                "skuNick":"",                  // sku编码
                "itemId":888390669925,         // 商品id  
                "relItemId":541831153308,      // 服务商商品id 
                "itemTitle":"保鲜可抽真空红酒塞不锈钢葡萄酒瓶塞 红酒塞子酒具用品",   // 商品名称
                "itemLinkUrl":"https://app.kwaixiaodian.com/merchant/shop/detail?id=888390669925&hyId=kwaishop&layoutType=4",  // 商品链接
                "itemPicUrl":"https://u1-000.ecukwai.com/ufile/adsocial/cb29d776-927d-41ef-9474-7a8ee29b3fea.jpg",             // 商品图片地址
                "num":2,                       // sku数量
                "originalPrice":10,            // 商品促销前单价快照 以分为单位
                "discountFee":0,               // 促销减价、折扣价格
                "price":10,                    // 商品单价快照，以分为单位    
                "itemType":1,                  // 1自建商品 2 闪电购商品
                "goodsCode":"",                // 外部货品编码
                "warehouseCode":"",            // 快手仓库编码  
                "orderItemId":46745568318428,  // 订单商品id，原有的id历史字段。商品id请使用itemId
                "goodStoreCode":0              // 电子凭证券码库ID
            },
            "orderRefundList":[                // 订单退款列表，按照创建时间逆序，最新的在第一个   
              {
                "refundId":  10987654,         // 退款id   
                "refundStatus":10              // 退款状态 枚举：[10, "买家仅退款申请"] [11, "买家退货退款申请"] [20, "平台介入-买家仅退款申请"] [21, "平台介入-买家退货退款申请"] [22, "平台介入-已确认退货退款"] [30, "商品回寄信息待买家更新"] [40, "商品回寄信息待卖家确认"] [50, "退款执行中"] [60, "退款成功"] [70, "退款失败"]   
              }
            ],                              
            "orderLogisticsInfo":[             // 订单物流信息
                {
                    "expressNo":"2215900041470428",  // 快递单号
                    "expressCode":"9999"             // 快递公司code
                }
            ],
            "orderNote":{
                "sellerNote":[                      // 订单备注，按照创建时间正序，最新的在最后一个           
                ]
            },
            "orderFlag":{                           // 订单插旗
                "flag":[
                    "grey_flag_tag_order"
                ]
            }
          },
          "Error_Code": 0,
          "Error_Msg": "",
          "AllowRetry": null,
          "RequestId": "20220322142251106"
        }
```

---

## 话费充值-取消直充订单（退款）

**简要描述：** 话费充值-取消直充订单（退款）

**请求URL：** `/PhoneRecharge/CancelTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ksOrderId | 是 | Number | 订单编号(在快手小店后台能看到的订单号) |
| reason | 是 | String | 取消原因 |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null,
    "RequestId": "20220322142251106"
  }
```

---

## 话费充值-完成直充订单（发货）

**简要描述：** 话费充值-完成直充订单（发货）

**请求URL：** `/PhoneRecharge/FinishTrade`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ksOrderId | 是 | Number | 订单编号(在快手小店后台能看到的订单号) |

**返回示例：**

```json
{
    "IsSuccess": true,
    "Error_Code": 0,
    "Error_Msg": "",
    "AllowRetry": null,
    "RequestId": "20220322142251106"
  }
```

---
