# 快手自动发货 (AldsKwai) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

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

**请求URL：** `KwaiTradePay`

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
        "oid":2215900041470428,  // 订单id
        "sellerId":2131430925,   // 商家id
        "buyerOpenId":"456",     // 买家openId
        "status":30,             // 订单状态：[0, "未知状态"], [10, "待付款"], [30, "已付款"], [40, "已发货"], [50, "已签收"], [70, "订单成功"], [80, "订单失败"]
        "beforeStatus":10,       // 修改之前状态
        "updateTime":1657183098  // 变更时间
    }
```

---

## 付款成功后，自动发货完成通知

**简要描述：** 平台，参数值：

- 付款成功后，自动发货完成，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdlePayAutoSendCompleted`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，32:付款成功后，自动发货完成; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
                "Tid":"2215900041470428",        // 原始订单号
                "PlatformShopId":"2131430925",   // 原始店铺Id
                "AldsType":1,                    // 自动发货的类型：1付款后发货、2买家确认收货后、4好评后赠送
                "CreateTime":"2022-08-29T10:12:51",  // 原始订单创建时间/下单时间。
                "PayTime":"2022-06-08T12:05:52",     // 原始付款时间
                "Status":"70",                       // 原始订单状态，具体查看平台订单详情
                "Orders":[                           // 子订单列表
                    {
                        "Num":2,                     // 购买数量
                        "GoodsName":"保鲜可抽真空红酒塞不锈钢葡萄酒瓶塞 红酒塞子酒具用品", // 商品名称
                        "GoodsId":"888390669925",    // 原始商品id
                        "OuterGoodsId":null,         // 原始商品外部编码
                        "SkuId":"888390671925",      // 原始商品SkuId
                        "OuterSkuId":"",             // 原始商品外部SkuId
                        "Oid":"2215900041470428",    // 原始子订单Id
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

## 确认收货后通知

**简要描述：** 平台，参数值：

- 确认收货后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `KwaiTradeSuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2:确认收货后; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "oid":2215900041470428,  // 订单id
        "sellerId":2131430925,   // 商家id
        "buyerOpenId":"456",     // 买家openId
        "status":30,             // 订单状态：[0, "未知状态"], [10, "待付款"], [30, "已付款"], [40, "已发货"], [50, "已签收"], [70, "订单成功"], [80, "订单失败"]
        "beforeStatus":10,       // 修改之前状态
        "updateTime":1657183098  // 变更时间
    }
```

---

## 确认收货后，自动发货完成通知

**简要描述：** 平台，参数值：

- 确认收货后，自动发货完成，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleConfirmAutoSendCompleted`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，64:确认收货后，自动发货完成; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
                "Tid":"2215900041470428",        // 原始订单号
                "PlatformShopId":"2131430925",   // 原始店铺Id
                "AldsType":2,                    // 自动发货的类型：1付款后发货、2买家确认收货后、4好评后赠送
                "CreateTime":"2022-08-29T10:12:51",  // 原始订单创建时间/下单时间。
                "PayTime":"2022-06-08T12:05:52",     // 原始付款时间
                "Status":"70",                       // 原始订单状态，具体查看平台订单详情
                "Orders":[                           // 子订单列表
                    {
                        "Num":2,                     // 购买数量
                        "GoodsName":"保鲜可抽真空红酒塞不锈钢葡萄酒瓶塞 红酒塞子酒具用品", // 商品名称
                        "GoodsId":"888390669925",    // 原始商品id
                        "OuterGoodsId":null,         // 原始商品外部编码
                        "SkuId":"888390671925",      // 原始商品SkuId
                        "OuterSkuId":"",             // 原始商品外部SkuId
                        "Oid":"2215900041470428",    // 原始子订单Id
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

## 退款创建后通知

**简要描述：** 平台，参数值：

- 退款创建后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `KwaiRefundCreated`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，4:退款创建; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "oid": 2015600006452419,  // 订单id
        "sellerId": 487711849,    // 商家id
        "refundId": 32142132,     // 退款单id
        "status": 1,              // 退款状态，枚举：[10, "买家仅退款申请"] [11, "买家退货退款申请"] [20, "平台介入-买家仅退款申请"] [21, "平台介入-买家退货退款申请"] [22, "平台介入-已确认退货退款"] [30, "商品回寄信息待买家更新"] [40, "商品回寄信息待卖家确认"] [50, "退款执行中"] [60, "退款成功"] [70, "退款失败"]
    }
```

---

## 退款失败后通知

**简要描述：** 平台，参数值：

- 退款失败后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `KwaiRefundClosed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，8:退款失败; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "oid": 2015600006452419,  // 订单id
        "sellerId": 487711849,    // 商家id
        "refundId": 32142132,     // 退款单id
        "handlingWay": 1,         // 退款方式，枚举： [1, "退货退款"] [10, "仅退款"]
        "negotiateStatus": 1,     // 协商状态，枚举：[0, "未知状态"] [1, "待商家处理"] [2, "商家同意"] [3, "商家驳回，等待买家修改"]
        "status": 1,              // 退款状态，枚举：[10, "买家仅退款申请"] [11, "买家退货退款申请"] [20, "平台介入-买家仅退款申请"] [21, "平台介入-买家退货退款申请"] [22, "平台介入-已确认退货退款"] [30, "商品回寄信息待买家更新"] [40, "商品回寄信息待卖家确认"] [50, "退款执行中"] [60, "退款成功"] [70, "退款失败"]
        "refundFee": 1000,        // 退款金额，单位：分
        "logisticsId": 4877849,   // 物流id
        "expressNo": "XAxx9",     // 物流单号
        "expressCode": 1,         // 物流公司 1百世快递 2EMS 3申通快递 4顺丰速运 5天天快递 6圆通速递 7韵达快运 8邮政快递包裹 9中通快递
        "receiptStatus": 1,       // 货物状态，枚举： UNKNOWN(0, "未知状态"), HAS_NOT_RECEIPT(1, "未收到货"), HAS_RECEIPT(2, "已收到货")
        "refundReason": 1,        // 退款原因，枚举：[3, "质量问题"] [4, "卖家发错货"] [5, "未按约定时间发货"] [7, "其他"] [8, "商品与商家宣传不符"] [10, "拍错、拍多"] [11, "不喜欢、不想要了"] [12, "地址填错了"] [13, "缺货"] [14, "快递/物流一直未送到"] [15, "假冒品牌"] [16, "商品少件/漏发"] [17, "商品破损"] [18, "退运费"][19, "7天无理由退货"] [20, "7天无理由退货(拆封后不支持)"] [21, "7天无理由退货(激活后不支持)"] [22, "7天无理由退货(安装后不支持)"][23, "7天无理由退货(定制类不支持)"] [24, "7天无理由退货(使用后不支持)"] [25, "7天无理由退货(开窗后不支持)"]
        "refundDesc": "没收到货",  // 退款说明
        "updateTime": 321222132   // 退款单更新时间，带毫秒的时间戳
    }
```

---

## 退款成功后通知

**简要描述：** 平台，参数值：

- 退款成功后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `KwaiRefundSuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，16:退款成功; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "oid": 2015600006452419,  // 订单id
        "sellerId": 487711849,    // 商家id
        "refundId": 32142132,     // 退款单id
        "handlingWay": 1,         // 退款方式，枚举： [1, "退货退款"] [10, "仅退款"]
        "negotiateStatus": 1,     // 协商状态，枚举：[0, "未知状态"] [1, "待商家处理"] [2, "商家同意"] [3, "商家驳回，等待买家修改"]
        "status": 1,              // 退款状态，枚举：[10, "买家仅退款申请"] [11, "买家退货退款申请"] [20, "平台介入-买家仅退款申请"] [21, "平台介入-买家退货退款申请"] [22, "平台介入-已确认退货退款"] [30, "商品回寄信息待买家更新"] [40, "商品回寄信息待卖家确认"] [50, "退款执行中"] [60, "退款成功"] [70, "退款失败"]
        "refundFee": 1000,        // 退款金额，单位：分
        "logisticsId": 4877849,   // 物流id
        "expressNo": "XAxx9",     // 物流单号
        "expressCode": 1,         // 物流公司 1百世快递 2EMS 3申通快递 4顺丰速运 5天天快递 6圆通速递 7韵达快运 8邮政快递包裹 9中通快递
        "receiptStatus": 1,       // 货物状态，枚举： UNKNOWN(0, "未知状态"), HAS_NOT_RECEIPT(1, "未收到货"), HAS_RECEIPT(2, "已收到货")
        "refundReason": 1,        // 退款原因，枚举：[3, "质量问题"] [4, "卖家发错货"] [5, "未按约定时间发货"] [7, "其他"] [8, "商品与商家宣传不符"] [10, "拍错、拍多"] [11, "不喜欢、不想要了"] [12, "地址填错了"] [13, "缺货"] [14, "快递/物流一直未送到"] [15, "假冒品牌"] [16, "商品少件/漏发"] [17, "商品破损"] [18, "退运费"][19, "7天无理由退货"] [20, "7天无理由退货(拆封后不支持)"] [21, "7天无理由退货(激活后不支持)"] [22, "7天无理由退货(安装后不支持)"][23, "7天无理由退货(定制类不支持)"] [24, "7天无理由退货(使用后不支持)"] [25, "7天无理由退货(开窗后不支持)"]
        "refundDesc": "没收到货",  // 退款说明
        "updateTime": 321222132   // 退款单更新时间，带毫秒的时间戳
    }
```

---
