# 闲鱼自动发货 (AldsIdle) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

---

## 买家申请退款通知

**简要描述：** 平台，参数值：

- 买家已经申请退款，等待卖家同意，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleRefundCreated`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，8:买家申请退款; |
| sign |  | String | [Query/Get] **签名算法：              将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。          **例：          **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，          **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，          **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，          **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8          再对连接后的字符串，进行MD5加密，          **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
        "biz_order_id":1520087523676842592,  // 交易订单号
        "item_id":646466274136,              // 商品Id
        "order_status":2,                    // 退款订单状态描述 1: 买家已经申请退款，等待卖家同意, 2: 卖家已经同意退款，等待买家退货, 3: 买家已经退货，等待卖家确认收货, 4: 退款关闭, 5: 退款成功, 6: 卖家拒绝退款, 8: 等待卖家确认退货地址, 9: 没有申请退款, 11: 退款结束
        "seller_id":584056073,               // 闲鱼商家的Id
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

**请求URL：** `IdleTradePay`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，1:付款成功后; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "biz_order_id": 9112588,  // 交易订单号
 "item_id": 1,  // 商品Id
 "order_status": 2, // 订单状态 0:未知状态、1：订单已创建、2：订单已付款、3：已发货、4：交易成功、5：已退款、6：交易关闭
 "seller_id": 1556356040640,  // 闲鱼商家的Id
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
| aopic |  | Number | [Query/Get] 推送类型，2:付款成功后，自动发货完成; |
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

## 囤囤券逆向消息

**简要描述：** 平台，参数值：

- 囤囤券逆向消息，未使用随时退和过期自动退时，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleEticketOrderMsg`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，256:电子凭证订单消息; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
    "msg_type":"expire_refund",  // expire_refund：过期自动退，unuse_refund:未使用退款
    "biz_order_id":"123",        // 交易订单号
    "refund_id":"123"            // 退款Id
    "seller_id":"132456456"      // 商家Id
}
```

---

## 接收助手IM消息

**简要描述：** 平台，参数值：

- 助手接收到消息后，推送对应内容。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是接收到的MsgId
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleReceiveClientMsg`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，128:鱼店长收到买家消息; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息结构体，json格式。              **业务id（BizId）： 相同的业务id，表示是同一会话。              **消息id（MsgId）： 全局唯一，长度一般在131~194之间，这个id在发送消息时需要带回。              **消息类型（ContentType）：1表示图片消息 ；2表示付款消息；3表示创建订单消息              **消息内容（Content）：不同contentType（消息类型），content内容（数据结构）不同，注意区分，如： |

**推送消息示例：**

```json
图片消息：
{
 "PlatformShopId": 9112588,  // 店铺id
 "ContentType": 1, // 消息类型：1表示图片消息 2表示付款消息 3表示创建订单消息
 "Content": "https://img.alicdn.com/imgextra/i2/1876527340/O1CN01KDigh2245mCgElZUR.heic",  // 消息内容：字符串，图片链接
 "MsgId": 1234567.45555.6666, // 消息id，长度一般在131~194之间，这个id在发送消息时需要带回
 "BizId": 1234567,  // 业务id
 "BuyerId": "2088123456789012",  // 买家id
 "BuyerNick": "买家昵称"  // 买家昵称
}

付款卡片消息：
{
 "PlatformShopId": 9112588,  // 店铺id
 "ContentType": 2, // 消息类型：1表示图片消息 2表示付款消息 3表示创建订单消息
 "Content": {
    "Tid": 2067719225654838,  // 交易号（订单号）
    "PayTime": "2025-10-01 12:00:00",  // 付款时间（非官方付款时间，这里实际为消息创建时间）
 },  // 消息内容：对象
 "MsgId": 1234567.456854.123, // 消息id，长度一般在131~194之间，这个id在发送消息时需要带回
 "BizId": 1234567,  // 业务id
 "BuyerId": "2088123456789012",  // 买家id
 "BuyerNick": "买家昵称"  // 买家昵称
}

创建订单（我已拍下，待付款）卡片消息：
{
 "PlatformShopId": 9112588,  // 店铺id
 "ContentType": 3, // 消息类型：1表示图片消息 2表示付款消息 3表示创建订单消息
 "Content": {
    "Tid": 2067719225654838,  // 交易号（订单号）
    "CreateTime": "2025-10-01 12:00:00",  // 创建时间（非官方创建时间，这里实际为消息创建时间）
 },  // 消息内容：对象
 "MsgId": 1234567.444444.124, // 消息id，长度一般在131~194之间，这个id在发送消息时需要带回
 "BizId": 1234567,  // 业务id
 "BuyerId": "2088123456789012",  // 买家id
 "BuyerNick": "买家昵称"  // 买家昵称
}
```

---

## 查询订单核销状态消息

**简要描述：** 平台，参数值：

- 查询核销状态时，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleEticketOrderMsg`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，512:查询订单核销状态消息; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
    "biz_order_id": "123",        // 交易订单号
    "code_list": [{
        "code_id": "E1115555",     // 码ID
        "code_password": 123456,   // 码密码
        "code_type": "1:码,2:卡密"   // 码类型
    }]
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

**请求URL：** `IdleTradeConfirm`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，16:确认收货后; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "biz_order_id": 9112588,  // 交易订单号
 "item_id": 1,  // 商品Id
 "order_status": 2, // 订单状态 0:未知状态、1：订单已创建、2：订单已付款、3：已发货、4：交易成功、5：已退款、6：交易关闭
 "seller_id": 1556356040640,  // 闲鱼商家的Id
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
| aopic |  | Number | [Query/Get] 推送类型，4:确认收货后，自动发货完成; |
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

## 订单关闭后通知

**简要描述：** 平台，参数值：

- 订单关闭后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleTradeClose`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，64:订单关闭后; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "biz_order_id": 9112588,  // 交易订单号
 "item_id": 1,  // 商品Id
 "order_status": 6, // 订单状态 0:未知状态、1：订单已创建、2：订单已付款、3：已发货、4：交易成功、5：已退款、6：交易关闭
 "seller_id": 1556356040640,  // 闲鱼商家的Id
}
```

---

## 订单创建成功后通知

**简要描述：** 平台，参数值：

- 订单创建成功后，推送对应消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `IdleTradeCreate`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，32:订单创建后; |
| sign |  | String | [Query/Get] **签名算法：                  将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。              **例：              **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，              **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，              **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，              **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8              再对连接后的字符串，进行MD5加密，              **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
 "biz_order_id": 9112588,  // 交易订单号
 "item_id": 1,  // 商品Id
 "order_status": 1, // 订单状态 0:未知状态、1：订单已创建、2：订单已付款、3：已发货、4：交易成功、5：已退款、6：交易关闭
 "seller_id": 1556356040640,  // 闲鱼商家的Id
}
```

---
