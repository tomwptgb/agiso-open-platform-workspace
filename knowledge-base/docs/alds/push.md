# 淘宝自动发货 (ALDS) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

---

## 双方已评价推送

**简要描述：** 平台，参数值：

- 当双方已评或评价可见时，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以Tid，Oid组合为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `traderatedvisible`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，16:双方已评价; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
    "Tid":"110770592823138",  // 订单编号
    "Oid":"110770592823138",  // 子订单编号
    "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx", // 卖家ID
    "NumIid":"592823138",  // 宝贝ID
    "BuyerNick":"碎**",  // 买家昵称
    "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
    "Content":"商品不错！",  // 评语内容
    "Result":"good",  // 评价
    "ValidScore":true,  // 评价信息是否用于记分
    "Created":"2020-03-09 14:59:11"  // 创建时间
  }
```

---

## 自动发货成功推送（含出库卡券信息）

**简要描述：** 平台，参数值：

- 自动发货成功时，会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `autosendsuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2048:自动发货成功推送; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
      "Tid": 2067719225654838,  // 订单编号
      "BuyerMessage": "",  // 买家留言
      "BuyerNick": "张**",  // 买家昵称
      "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
      "Created": "2016-07-11 11:20:09",  // 创建时间
      "Num": 1,  // 数量
      "Payment": "3.00",  // 支付金额
      "PayTime": "2016-07-11 11:20:20",  // 支付时间
      "Price": "3.00",  // 价格
      "SellerNick": "168**闲馆",  // 卖家昵称
      "Status": "WAIT_BUYER_CONFIRM_GOODS",  // 订单状态
      "TotalFee": "3.00",  // 总金额
      "ExpandCardExpandPriceUsed": "3.00",  // 用卡订单所用的权益金
      "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx", // 卖家ID
      "Orders": [
        {
          "Num": 1,  // 数量
          "NumIid": 45533870790,  // 宝贝ID
          "Oid": 2067719225654838,  // 子订单编号
          "OuterIid": "ALDS1000",  // 宝贝外部编码
          "OuterSkuId": "3432432",  // Sku外部编码
          "SkuId": "3423",  // Sku编号
          "Payment": "3.00",  // 支付金额
          "Price": "3.00",  // 价格
          "SkuPropertiesName": null,  // Sku属性名称
          "Title": "宝贝标题",  // 宝贝标题
          "TotalFee": "3.00",  // 总金额
          "DivideOrderFee": "5.00",  // 分摊之后的实付金额
          "PartMjzDiscount": "1.0",   // 优惠分摊
          "ExpandCardExpandPriceUsedSuborder": "3.00",   // 购物金核销子订单权益金分摊金额（单位为元）
          "SendCards": [  // 发送卡券列表
            {
              "CpcId": 123456,  // 卡种ID
              "Title": "300元京东卡",  // 卡种名称
              "Cards": [
                {
                    "Card": "125845451212",  // 卡号
                    "Pwd": "125845451212"  // 密码
                },
                {
                    "Card": "248521321541",
                    "Pwd": "248521321541"
                }
              ]
            }
          ]
        }
      ]
  }
```

---

## 采购下单

**简要描述：** 平台，参数值：

- 推送触发，仅在买家完成支付时推送，因此理论上推送的状态只有：WAIT_SELLER_SEND_GOODS(等待卖家发货,即:买家已付款)。
- 推送的签名请务必验证，验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：<span style=\
- >$.post('http://test.com/agiso?timestamp=11222212121&aopic=2&sign=f8aa165fc951f266667e0605d78b93af', { json: '{\
- :2067719225654838,......}' })

**请求URL：** `tradesuccess`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2:买家付款; |
| json |  | String | [Form/Post] 交易信息,如： |

**推送消息示例：**

```json
{
      "Tid": 2067719225654838,  // 订单编号
      "Status": "WAIT_BUYER_CONFIRM_GOODS",  // 订单状态
      "SellerNick": "168休闲馆",  // 卖家昵称
      "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx" // 卖家ID
      "BuyerNick": "碎**",  // 买家昵称
      "BuyerMessage": null,  // 买家留言
      "Price": "3.00",  // 价格
      "Num": 1,  // 数量
      "TotalFee": "3.00",  // 总价
      "Payment": "3.00",  // 支付金额
      "PayTime": "2016-07-11 11:20:20",  // 支付时间
      "Created": "2016-07-11 11:20:09",  // 订单创建时间
      "ExpandCardExpandPriceUsed": "3.00",  // 用卡订单所用的权益金
      "Orders": [
          {
              "Num": 1,   // 数量
              "NumIid": 45533870790,  // 宝贝ID
              "Oid": 2067719225654838,  // 子订单编号
              "OuterIid": "ALDS_1000",  // 宝贝外部编号
              "OuterSkuId": "ALDS_SKU_1000",   // Sku外部编号
              "Payment": "3.00",  // 支付金额
              "Price": "3.00",  // 价格
              "SkuPropertiesName": null,  // Sku属性名称
              "Title": "宝贝标题",  // 宝贝标题
              "TotalFee": "3.00"  // 总价
              "ExpandCardExpandPriceUsedSuborder": "3.00",   // 购物金核销子订单权益金分摊金额（单位为元）
          }
      ]
    }
```

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

**备注：** 推送参数详细说明可参考[淘宝API文档](https://open.taobao.com/tmc.htm?docId=105&docType=9)，对于部分敏感信息，需要找客服单独授权才会推送

---

## 采购下单通知

**简要描述：** 平台，参数值：

- 推送触发，仅在买家完成支付时推送，因此理论上推送的状态只有：WAIT_SELLER_SEND_GOODS(等待卖家发货,即:买家已付款)。
- 推送的签名请务必验证，验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：<span style=\
- >$.post('http://test.com/agiso?timestamp=11222212121&aopic=2&sign=f8aa165fc951f266667e0605d78b93af', { json: '{\
- :2067719225654838,......}' })

**请求URL：** `tradeBuyerPaySimple`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2097152:买家付款; |
| json |  | String | [Form/Post] 推送消息,如： |

**推送消息示例：**

```json
{
      "Tid": 2067719225654838,  // 订单编号
      "Status": "WAIT_BUYER_CONFIRM_GOODS",  // 订单状态
      "SellerNick": "168休闲馆",  // 卖家昵称
      "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx", // 卖家ID
      "BuyerNick": "碎**",  // 买家昵称
      "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
      "Payment": "3.00",  // 支付金额
      "Type": "fixed",  // 交易类型
    }
```

**备注：** 推送参数详细说明可参考[淘宝API文档](https://open.taobao.com/tmc.htm?docId=105&docType=9)

---

## 采购单创建通知

**简要描述：** 平台，参数值：

- 推送触发，仅在买家拍下时推送。
- 推送的签名请务必验证，验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和推送类型。
- 推送方式，用jquery做示例：<span style=\
- >$.post('http://test.com/agiso?timestamp=11222212121&aopic=1&sign=f8aa165fc951f266667e0605d78b93af', { json: '{\
- : 2067719225654838,......}' })

**请求URL：** `tradecreate`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，1:买家拍下; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 交易信息,如： |

**推送消息示例：**

```json
{
    "Tid": 2067719225654838,   // 订单编号
    "Status": "WAIT_BUYER_CONFIRM_GOODS",  // 订单状态
    "SellerNick": "168休闲馆",  // 卖家昵称
    "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx" // 卖家ID
    "BuyerNick": "碎**",  // 买家昵称
    "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
    "Payment": "3.00",  // 支付金额
    "type": "fixed"  // 类型
  }
```

**备注：** 推送参数详细说明可参考[淘宝API文档](https://open.taobao.com/api.htm?docId=121&docType=2)

---

## 采购单备注修改

**简要描述：** 平台，参数值：

- 推送触发，在交易创建后，买家或者卖家修改交易备注
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `tradememomodified`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，524288:卖家修改订单备注 |
| sign |  | String | [Query/Get] **签名算法：                      将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。                  **例：                  **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，                  **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，                  **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，                  **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8                  再对连接后的字符串，进行MD5加密，                  **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 卖家修改订单备注消息,如： |

**推送消息示例：**

```json
{
                "BuyerNick":"碎**",  // 买家昵称
                "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
                "Oid":"110770592823138",  // 子订单编号
                "Tid":"110770592823138",  // 订单编号
                "SellerNick":"麦包包",  // 卖家昵称
                "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx" // 卖家ID
                "SellerMemo":"备注",  // 卖家备注
                "SellerFlag":"旗帜"  // 卖家备注标的旗帜
                }
```

---

## 采购单已发货通知

**简要描述：** 平台，参数值：

- 淘宝订单状态变更为“已发货”时触发推送。
- 推送的签名请务必验证，验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：<span style=\
- >$.post('http://test.com/agiso?timestamp=11222212121&aopic=1&sign=f8aa165fc951f266667e0605d78b93af', { json: '{\
- : 2067719225654838,......}' })

**请求URL：** `tradesellership`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，1048576:卖家发货; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 交易信息,如： |

**推送消息示例：**

```json
{
    "Tid": 2067719225654838,
    "Status": "WAIT_BUYER_CONFIRM_GOODS",
    "SellerNick": "168休闲馆",
    "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx" // 卖家ID
    "BuyerNick": "碎**",
    "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",
    "Payment": "3.00",
    "type": "fixed"
  }
```

**备注：** 推送参数详细说明可参考[淘宝API文档](https://open.taobao.com/tmc.htm?docId=106&docType=9)

---

## 采购单申请退款

**简要描述：** 平台，参数值：

- 推送触发，仅在买家申请退款时推送。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以退款编号RefundId为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- RefundId
- 592823138
- })

**请求URL：** `refundcreated`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，256:买家申请退款; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 退款消息,如： |

**推送消息示例：**

```json
{
    "RefundId":"592823138",  // 退款ID
    "BuyerNick":"碎**",  // 买家昵称
    "BuyerOpenUid":"AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
    "RefundFee":"21.32",  // 退款金额
    "Oid":"110770592823138",  // 子订单编号
    "Tid":"110770592823138",  // 订单编号
    "RefundPhase":"onsale",  // 退款阶段
    "BillType":"refund_bill",  // 退款类型
    "SellerNick":"麦包包",  // 卖家昵称
    "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx", // 卖家ID
    "Modified":"2000-12-30 12:32:20"  // 修改时间
  }
```

**备注：** 推送参数详细说明可参考[淘宝退款创建消息文档](https://open.taobao.com/api.htm?docId=121&docType=2)

---

## 采购单退款关闭

**简要描述：** 平台，参数值：

- 当页面买家将退款关闭时，会产生此消息； 未确认收货时，发起退款过程，卖家拒绝退款后，买家还确认收货时，此时也会产生此消息。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。在业务进行之前，对消息进行去重判断，以退款编号RefundId为唯一标识。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- RefundId
- 592823138
- })

**请求URL：** `refundclosed`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，32768:撤销退款; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 退款消息,如： |

**推送消息示例：**

```json
{
    "RefundId":"592823138",  // 退款ID
    "BuyerNick":"碎**",  // 买家昵称
    "BuyerOpenUid": "AaEL_gqxAAShiml5geo3bVTa",  // 买家ID
    "RefundFee":"21.32",  // 退款金额
    "Oid":"110770592823138",  // 子订单编号
    "Tid":"110770592823138",  // 订单编号
    "RefundPhase":"onsale",  // 退款阶段
    "BillType":"refund_bill",  // 退款类型
    "SellerNick":"麦包包",  // 卖家昵称
    "SellerOpenUid":"AAEF_gqxAAShiml5xxxxxxxx", // 卖家ID
    "Modified":"2000-12-30 12:32:20"  // 修改时间
  }
```

**备注：** 推送参数详细说明可参考[淘宝退款关闭消息文档](https://open.taobao.com/api.htm?docId=121&docType=2)

---
