# 有赞自动发货 (AldsYouzan) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

---

## 买家发起退款申请

**简要描述：** 平台，参数值：

- 买家发起退款，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `YouzanRefundCreated`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2:买家发起退款; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "tid":"E2018123456789",                // 订单号
        "update_time":"2018-01-01 00:00:00",   // 更新时间
        "refund_type":"REFUND_ONLY",           // REFUND_ONLY 仅退款 REFUND_AND_RETURN 退货退款
        "refund_reason":"RETURNSNOT_BUYWRONG", // 退款原因枚举：详见文档
        "oids":"1234567",           // 交易明细id
        "refund_id":"123456789",    // 退款id
        "refunded_fee":"1.00",      // 退款金额
        "version":"1587218879305",  // 维权版本号，作为维权单后续操作的接口入参使用
      }
```

**备注：** 推送参数详细说明可参考[有赞买家发起退款消息文档](https://doc.youzanyun.com/detail/MSG/209)

---

## 买家取消退款通知

**简要描述：** 平台，参数值：

- 买家取消退款且退款单状态CLOSED(退款关闭)时触发，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `YouzanRefundClosed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，4:买家取消退款; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "tid":"E2018123456789",  // 订单号
        "update_time":"2018-01-01 00:00:00",   // 更新时间
        "refund_type":"REFUND_ONLY",           // REFUND_ONLY 仅退款 REFUND_AND_RETURN 退货退款
        "refund_reason":"RETURNSNOT_BUYWRONG", // 退款原因枚举：详见文档
        "oids":"1234567",           // 交易明细id
        "refund_id":"123456789",    // 退款id
        "refunded_fee":"1.00",      // 退款金额
      }
```

**备注：** 推送参数详细说明可参考[有赞买家取消退款消息文档](https://doc.youzanyun.com/detail/MSG/202)

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

**请求URL：** `YouzanPayAutoSendCompleted`

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

**请求URL：** `YouzanTradePay`

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
      "id": "E20220912003358008000001",  // 业务消息的标识，交易为订单号
      "kdt_id": 46240499,                // 店铺id
      "kdt_name": "Steam购",             // 店铺名称
      "root_kdt_id": 46240499,           // 有赞连锁总店店铺ID
      "status": "WAIT_SELLER_SEND_GOO"   // 主订单状态 WAIT_BUYER_PAY （等待买家付款）；TRADE_PAID（订单已支付 ）； WAIT_CONFIRM（待确认，包含待成团、待接单等等。即：买家已付款，等待成团或等待接单）； WAIT_SELLER_SEND_GOODS（等待卖家发货，即：买家已付款）；WAIT_BUYER_CONFIRM_GOODS (等待买家确认收货，即：卖家已发货) ；TRADE_SUCCESS（买家已签收以及订单成功）；TRADE_CLOSED（交易关闭）；PS：TRADE_PAID状态仅代表当前订单已支付成功，表示瞬时状态，稍后会自动修改成后面的状态。如果不关心此状态请再次请求详情接口获取下一个状态。
      }
```

---

## 卖家同意退款通知

**简要描述：** 平台，参数值：

- 卖家同意退款且退款单状态为SUCCESS(退款成功)时触发，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `YouzanRefundSuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，8:卖家同意退款; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "tid":"E2018123456789",  // 订单号
        "update_time":"2018-01-01 00:00:00",   // 更新时间
        "refund_type":"REFUND_ONLY",           // REFUND_ONLY 仅退款 REFUND_AND_RETURN 退货退款
        "refund_reason":"RETURNSNOT_BUYWRONG", // 退款原因枚举：详见文档
        "oids":"1234567",           // 交易明细id
        "refund_id":"123456789",    // 退款id
        "refunded_fee":"1.00",      // 退款金额
      }
```

**备注：** 推送参数详细说明可参考[卖家同意退款（终态）消息文档](https://doc.youzanyun.com/detail/MSG/206)

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

**请求URL：** `YouzanConfirmAutoSendCompleted`

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
