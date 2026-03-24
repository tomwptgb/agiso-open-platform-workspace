# 抖店自动发货 (AldsDoudian) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

---

## 买家发起售后申请

**简要描述：** 平台，参数值：

- 买家发起售后申请后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianRefundCreated`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2:买家发起售后申请; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "aftersale_id":7000893114000949000,  // 售后单ID
        "aftersale_status":6,                // 售后状态：0-售后初始化， 6-售后申请， 7-售后退货中， 27-拒绝售后申请， 12-售后成功， 28-售后失败， 11-售后已发货， 29-退货后拒绝退款， 13-售后换货商家发货， 14-售后换货用户收货， 51-取消成功， 53-逆向交易完成
        "aftersale_type":2,                  // 售后类型： 0: 退货 ，1: 售后仅退款， 2: 发货前退款， 3：换货 ， 4:系统取消，5：用户取消，6：价保，7：补寄
        "apply_time":1630022518,             // 售后申请时间
        "p_id":4835804142146757000,          // 父订单ID
        "reason_code":1,                     // 申请售后原因码，枚举值如下
        "refund_amount":8900,                // 申请退款的金额（含运费）
        "refund_post_amount":0,              // 申请退的运费金额
        "refund_voucher_num":0,              // 申请退款的卡券的数量
        "s_id":4835804142146757000,          // 子订单ID
        "shop_id":10437917                   // 店铺ID
      }
```

**备注：** 推送参数详细说明可参考[抖店买家发起售后申请消息文档](https://op.jinritemai.com/docs/message-docs/31/115)

---

## 付款成功后自动发货完成通知

**简要描述：** 平台，参数值：

- 付款成功后，自动发货完成，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianPayAutoSendCompleted`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，16:付款成功后，自动发货完成; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
                "Tid":"2215900041470428",        // 订单号
                "PlatformShopId":"2131430925",   // 店铺Id
                "AldsType":1,                    // 自动发货的类型：1付款后发货、2买家确认收货后、4好评后赠送
                "CreateTime":"2022-08-29T10:12:51",  // 原始平台订单创建时间/下单时间。
                "PayTime":"2022-06-08T12:05:52",     // 原始平台付款时间
                "Status":"70",                       // 原始平台订单原始状态
                "Orders":[                           // 子订单列表
                    {
                        "Num":2,                     // 购买数量
                        "GoodsName":"保鲜可抽真空红酒塞不锈钢葡萄酒瓶塞 红酒塞子酒具用品", // 商品名称
                        "GoodsId":"888390669925",    // 原始商品id
                        "OuterGoodsId":null,         // 原始商品外部编码
                        "SkuId":"888390671925",      // 原始商品SkuId
                        "OuterSkuId":"",             // 原始商品外部SkuId
                        "Oid":"2215900041470428",    // 原始商品订单号
                        "SpType":1,                  // 自动发货内容方式：1单卡种、2组合卡、3无卡、4、接口
                        "SpecName":"",               // 原始sku信息
                        "SendCards":[                // 自动发货卡券列表
                            {
                                "Card":"15449",      // 卡号
                                "Pwd":""             // 密码
                            },
                            {
                                "Card":"15450",
                                "Pwd":""
                            }
                        ]
                    }
                ]
            }
```

---

## 付款成功后通知

**简要描述：** 平台，参数值：

- 付款成功后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianTradePay`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，1:付款成功后; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "p_id": 4900477063905653860,   // 父订单ID
        "s_ids": [],      // 子订单ID列表
        "shop_id": 7784061, // 店铺ID
        "order_status": 5,  // 父订单状态，交易完成消息的status值为"5"
        "order_type": 2,  // 订单类型： 0: 实物 2: 普通虚拟 4: poi核销 5: 三方核销 6: 服务市场
        "complete_time": 1630373504,  // 交易完成时间
        "pay_amount": 1990,  // 订单实付金额
        "s_ids": []  // 子订单ID列表
      }
```

---

## 同意补寄申请消息

**简要描述：** 平台，参数值：

- 1、买家申请补寄后，商家同意买家申请
- 2、卖家由拒绝补寄申请转为同意买家申请
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianSmsReceipt`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，256:同意补寄申请消息; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
          "aftersale_id":7000893114000949000,  // 售后单ID
          "after_sale_status":6,                // 售后状态：0-售后初始化， 6-售后申请， 7-售后退货中， 27-拒绝售后申请， 12-售后成功， 28-售后失败， 11-售后已发货， 29-退货后拒绝退款， 13-售后换货商家发货， 14-售后换货用户收货， 51-取消成功， 53-逆向交易完成
          "aftersale_type":2,                  // 售后类型： 0: 退货 ，1: 售后仅退款， 2: 发货前退款， 3：换货 ， 4:系统取消，5：用户取消，6：价保，7：补寄
          "p_id":1630022518,             // 父订单
          "s_id":4835804142146757000,          // 子订单
          "reason_code":1,                     // 申请售后原因码
          "shop_id":8900,                // 店铺ID
          "update_time":0,              // 售后单更新时间
}
```

**备注：** 推送参数详细说明可参考[抖店同意补寄申请消息文档](https://op.jinritemai.com/docs/message-docs/31/122)

---

## 售后关闭通知

**简要描述：** 平台，参数值：

- 当买家取消申请或系统超时机制导致退款取消时，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianRefundClosed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，4:售后关闭; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "aftersale_id":7000893114000949000,  // 售后单ID
        "aftersale_status":6,                // 售后状态：0-售后初始化， 6-售后申请， 7-售后退货中， 27-拒绝售后申请， 12-售后成功， 28-售后失败， 11-售后已发货， 29-退货后拒绝退款， 13-售后换货商家发货， 14-售后换货用户收货， 51-取消成功， 53-逆向交易完成
        "aftersale_type":2,                  // 售后类型： 0: 退货 ，1: 售后仅退款， 2: 发货前退款， 3：换货 ， 4:系统取消，5：用户取消，6：价保，7：补寄
        "close_time":1630022518,             // 售后关闭时间
        "p_id":4835804142146757000,          // 父订单ID
        "reason_code":1,                     // 申请售后原因码，枚举值如下
        "refund_amount":8900,                // 申请退款的金额（含运费）
        "refund_post_amount":0,              // 申请退的运费金额
        "refund_voucher_num":0,              // 申请退款的卡券的数量
        "s_id":4835804142146757000,          // 子订单ID
        "shop_id":10437917                   // 店铺ID
      }
```

**备注：** 推送参数详细说明可参考[抖店售后关闭消息文档](https://op.jinritemai.com/docs/message-docs/31/122)

---

## 商家同意退款消息

**简要描述：** 平台，参数值：

- 买家在发货前申请整单退款，卖家同意退款或超时自动同意退款时。
- 买家在发货后申请仅退款，卖家同意退款或超时自动同意退款时。
- 买家在发货后申请申请退货，卖家确认收货或系统超时自动确认收货时。
- 卖家收到买家换货包裹，核验后无法换货，同意换货但转直接退款时。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianRefundRefundAgreed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，128:商家同意退款消息; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
          "agree_time":1630306403                        // 同意退款时间         
          "update_time": "2022-09-02T10:27:50+08:00",    // 售后单更新时间
          "p_id": 457824112312123,                       // 父订单ID
          "s_id": 457824112312123,                       // 子订单ID
          "shop_id": 7784061,                            // 店铺ID
          "aftersale_id": 657824112312121,               // 父订单ID
          "aftersale_status": 6,                         // 售后状态码
          "aftersale_type": 0,                           // 售后类型： 0: 退货 1: 售后仅退款 2: 发货前整单退款 3：换货
          "refund_amount": 1000,                         // 申请退款的金额（含运费）
          "reason_code": 1,                              // 申请售后原因码
          "refund_voucher_num": 1,                       // 申请退款的卡券的数量
          "refund_post_amount": 100                      // 申请退的运费金额
        }
```

---

## 商家同意退货申请消息

**简要描述：** 平台，参数值：

- 当买家在发货后申请退货退款，卖家同意时，推送对应消息。
- 订单已发货，买家发起换货申请后，卖家同意申请，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianRefundReturnApplyAgreed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，64:商家同意退货申请消息; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "update_time": "2022-09-02T10:27:50+08:00",  // 售后单更新时间
        "p_id": 457824112312123,     // 父订单ID
        "s_id": 457824112312123,     // 子订单ID
        "shop_id": 7784061,    // 店铺ID
        "aftersale_id": 657824112312121,     // 父订单ID
        "aftersale_status": 6,     // 售后状态码
        "aftersale_type": 0,     // 售后类型： 0: 退货 1: 售后仅退款 2: 发货前整单退款 3：换货
        "refund_amount": 1000,     // 申请退款的金额（含运费）
        "reason_code": 1,    // 申请售后原因码
        "refund_voucher_num": 1,     // 申请退款的卡券的数量
        "refund_post_amount": 100    // 申请退的运费金额
      }
```

---

## 短信回执消息

**简要描述：** 平台，参数值：

- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianRefundAuditAgreeResend`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，512:短信回执消息; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
            "status_code": "0",                       // 状态码,"0"代表成功，其余表示失败
            "description": "发送成功",                // 状态描述
            "signature": "阿奇索",                   // 短信签名
            "template_id": "ST_82aba028",             // 模板ID
            "channel_type": "CN_NTC",                 // 短信类型
            "message_id": "226758fc-13e8-4971-a168-98b6beb15447",     // 发送时返回的MessageID
            "msg_count": 2,                           // 计费条数
        }
```

**备注：** 推送参数详细说明可参考[抖店同意补寄申请消息文档](https://op.jinritemai.com/docs/message-docs/31/122)

---

## 确认收货后自动发货完成通知

**简要描述：** 平台，参数值：

- 确认收货后，自动发货完成，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianConfirmAutoSendCompleted`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，32:确认收货后，自动发货完成; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
                "Tid":"2215900041470428",        // 订单号
                "PlatformShopId":"2131430925",   // 店铺Id
                "AldsType":2,                    // 自动发货的类型：1付款后发货、2买家确认收货后、4好评后赠送
                "CreateTime":"2022-08-29T10:12:51",  // 原始平台订单创建时间/下单时间。
                "PayTime":"2022-06-08T12:05:52",     // 原始平台付款时间
                "Status":"70",                       // 原始平台订单原始状态
                "Orders":[                           // 子订单列表
                    {
                        "Num":2,                     // 购买数量
                        "GoodsName":"保鲜可抽真空红酒塞不锈钢葡萄酒瓶塞 红酒塞子酒具用品", // 商品名称
                        "GoodsId":"888390669925",    // 原始商品id
                        "OuterGoodsId":null,         // 原始商品外部编码
                        "SkuId":"888390671925",      // 原始商品SkuId
                        "OuterSkuId":"",             // 原始商品外部SkuId
                        "Oid":"2215900041470428",    // 原始商品订单号
                        "SpType":1,                  // 自动发货内容方式：1单卡种、2组合卡、3无卡、4、接口
                        "SpecName":"",               // 原始sku信息
                        "SendCards":[                // 自动发货卡券列表
                            {
                                "Card":"15449",      // 卡号
                                "Pwd":""             // 密码
                            },
                            {
                                "Card":"15450",
                                "Pwd":""
                            }
                        ]
                    }
                ]
            }
```

---

## 退款成功后通知

**简要描述：** 平台，参数值：

- 当商家同意退款后，实际退款到账时，推送对应消息。
- 卖家收到买家换货包裹，核验后无法换货，同意换货但转直接退款，退款成功时
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `DoudianRefundSuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，8:退款成功; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "aftersale_id":7000893114000949000,  // 售后单ID
        "aftersale_status":6,                // 售后状态：0-售后初始化， 6-售后申请， 7-售后退货中， 27-拒绝售后申请， 12-售后成功， 28-售后失败， 11-售后已发货， 29-退货后拒绝退款， 13-售后换货商家发货， 14-售后换货用户收货， 51-取消成功， 53-逆向交易完成
        "aftersale_type":2,                  // 售后类型： 0: 退货 ，1: 售后仅退款， 2: 发货前退款， 3：换货 ， 4:系统取消，5：用户取消，6：价保，7：补寄
        "success_time":1630022518,           // 退款成功时间
        "p_id":4835804142146757000,          // 父订单ID
        "reason_code":1,                     // 申请售后原因码，枚举值如下
        "refund_amount":8900,                // 申请退款的金额（含运费）
        "refund_post_amount":0,              // 申请退的运费金额
        "refund_voucher_num":0,              // 申请退款的卡券的数量
        "s_id":4835804142146757000,          // 子订单ID
        "shop_id":10437917                   // 店铺ID
      }
```

**备注：** 推送参数详细说明可参考[抖店退款成功消息文档](https://op.jinritemai.com/docs/message-docs/31/121)

---
