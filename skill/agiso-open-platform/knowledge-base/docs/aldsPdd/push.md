# 拼多多自动发货 (AldsPdd) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

---

## 买家取消订单时通知

**简要描述：** 平台，参数值：

- 消费者/系统/平台客服 创建售后单时，会触发此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddRefundCreated`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，8:退款创建; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "mall_id": 9112588,     // 店铺Id
 "refund_fee": 1,     // 退款金额(单位:分)
 "bill_type": 2,     // 售后类型: 1-仅退款；2-退货退款；3-换货；4-补寄；5-维修
 "modified": 1556356040640,     // 更新时间
 "refund_id": 408780010,     // 售后单id
 "operation": 1000,     // 售后操作:1000-消费者申请；1001-平台客服新建；1002-平台客服开启；1003-系统创建
 "tid": "190427-391328563312668"     // 订单编号
}
```

---

## 买家备注修改通知

**简要描述：** 平台，参数值：

- 在交易创建后，买家修改交易备注，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddTradeBuyerMemoModified`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，64:买家备注修改; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "mall_id": 9112588,     // 店铺Id
 "buyer_memo": "两个颜色",     // 买家留言
 "tid": "190427-391328563312668"     // 订单编号
}
```

---

## 交易备注修改

**简要描述：** 平台，参数值：

- 在交易创建后，卖家修改交易备注，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid，seller_memo组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddTradeMemoModified`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2:交易备注修改; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
    "mall_id":"110770592823138",    // 店铺Id
    "tid":"200624-0199468655650824",    // 订单编号
    "seller_memo": "卖家留言"    // 卖家留言
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

**请求URL：** `PddPayAutoSendCompleted`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，128:付款成功后，自动发货完成; |
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
                "Oid":"2215900041470428",    // 原始无返回，自动发货生成格式（Tid#SkuId或Tid）
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

## 售后单关闭通知

**简要描述：** 平台，参数值：

- 售后单关闭时，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddAfterSaleClose`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，512:售后单关闭; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "mall_id": 9112588,     // 店铺Id
 "refund_fee": 1,    // 退款金额(单位:分)
 "bill_type": 2,     // 售后类型: 1-仅退款；2-退货退款；3-换货；4-补寄；5-维修
 "modified": 1556356040640,     // 更新时间
 "refund_id": 408780010,     // 售后单id
 "operation": 1300,     // 售后操作（operation）：用户撤销1300 ；客服驳回1302 ；系统驳回1303 ；退款成功1304； 维修完成1305；售后超过有效期，退款关闭1306；用户处理逾期，退款失败1307；用户发货逾期，退款失败1308；用户拒收逾期，退款失败1309；逾期未确认，维修成功1310；用户确认换货补寄完成1311；用户逾期关闭1312；用户逾期系统确认完成1313；平台撤销1314
 "tid": "190427-391328563312668"     // 订单编号
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

**请求URL：** `PddConfirmAutoSendCompleted`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，256:确认收货后，自动发货完成; |
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
                        "Oid":"2215900041470428",    // 原始无返回，自动发货生成格式（Tid#SkuId或Tid）
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

## 订单取消成功后通知

**简要描述：** 平台，参数值：

- 售后单关闭退款成功时，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddRefundSuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，16:退款成功; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "mall_id": 9112588,     // 店铺Id
 "refund_fee": 1,    // 退款金额(单位:分)
 "bill_type": 2,     // 售后类型: 1-仅退款；2-退货退款；3-换货；4-补寄；5-维修
 "modified": 1556356040640,     // 更新时间
 "refund_id": 408780010,     // 售后单id
 "operation": 1300,     // 售后操作（operation）：用户撤销1300 ；客服驳回1302 ；系统驳回1303 ；退款成功1304； 维修完成1305；售后超过有效期，退款关闭1306；用户处理逾期，退款失败1307；用户发货逾期，退款失败1308；用户拒收逾期，退款失败1309；逾期未确认，维修成功1310；用户确认换货补寄完成1311；用户逾期关闭1312；用户逾期系统确认完成1313；平台撤销1314
 "tid": "190427-391328563312668"     // 订单编号
}
```

---

## 订单已发货通知

**简要描述：** 平台，参数值：

- 当通过api完成发货操作时，会产生此消息； 当通过页面完成发货操作时，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddTradeSellerShip`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，32:卖家发货; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "mall_id": 1511532,     // 店铺Id
 "tid": "20124-2012455211122"     // 订单编号
}
```

---

## 订单确认收货时通知

**简要描述：** 平台，参数值：

- 买家确认收货和订单自动收货后，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddTradeSuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，4:交易成功; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "mall_id": 1511532,     // 店铺Id
 "tid": "20124-2012455211122"     // 订单编号
}
```

---

## 订单确认时自动采购卡券

**简要描述：** 平台，参数值：

- 普通订单拼团成功会产生此消息；定金订单付完尾款，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `PddTradeConfirmed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，1:交易确认; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "MallId":"110770592823138",     // 店铺Id
        "Tid":"200624-0199468655650824",     // 订单编号
        "BuyerMemo":"",    // 买家留言信息
        "OrderSn":"200624-0199468655650824",    // 订单编号
        "ConfirmTime":"2020-06-24T10:42:51",    // 成交时间
        "CreatedTime":"2020-06-24T10:42:46",    // 创建时间
        "PayAmount":0.1,    // 支付金额（元）支付金额=商品金额-折扣金额+邮费
        "GoodsAmount":0.1,    // 商品金额（元）商品金额=商品销售价格*商品数量-订单改价折扣金额
        "Remark":"",    // 商家订单备注
        "ItemList":[    // 订单中商品sku列表
            {
                "goods_id":"2557644875",    // 商品编号
                "sku_id":"55533589398",    // 商品规格编码
                "outer_id":"003",    //商家外部编码（sku），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。
                "outer_goods_id":"87952",    // 商家外部编码（商品），注意：编辑商品后必须等待商品审核通过后方可生效，订单中商品信息为交易快照的商品信息。
                "goods_name":"卡通形象平面设计",    // 商品名称
                "goods_price":0.1,    // 商品销售价格
                "goods_spec":"定制(拍前联系)",    // 商品规格，使用（规格值1,规格值2）组合作为sku的表示，中间以英文逗号隔开
                "goods_count":1,    // 商品数量
                "goods_img":""    // 商品图片
            }
        ]
}
```

---
