# 打印 (Print) - 推送通知

推送的签名请务必验证，以验证数据来源的合法性。
推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。

---

## 订单备注修改推送

**简要描述：** 平台，参数值：

- 推送触发，仅在卖家修改平台订单备注时推送。
- 推送的签名请务必验证，以验证数据来源的合法性。验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和订单状态。
- 推送方式，用jquery做示例：$.post(\
- , { json: \
- Tid
- 592823138
- })

**请求URL：** `ebprinttradememomodified`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，2:卖家修改订单备注 |
| sign |  | String | [Query/Get] **签名算法：                      将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。                  **例：                  **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，                  **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，                  **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，                  **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8                  再对连接后的字符串，进行MD5加密，                  **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 卖家修改订单备注消息,如： |

**推送消息示例：**

```json
{
                "Tid":"1313131316313", //订单编号
                "Platform":"110770592823138", //平台 taobao:淘宝; pdd:拼多多;
                "SellerMemo":"我是备注", //卖家备注
                "UserId":"08fa59e4675b42dca9bff41b2b6039c1", //用户id
                }
```

---

## 运单号变动通知

**简要描述：** 平台，参数值：

- 推送触发，获取到电子面单后推送。
- 推送的签名请务必验证，验证方法参考以下说明。
- 推送时，有可能消息重复推送。实际开发中，请一定要在使用消息前进行去重判断。主要依据是订单编号Tid和推送类型。
- 推送方式，用jquery做示例：<span style=\
- >$.post('http://test.com/agiso?timestamp=11222212121&aopic=1&sign=f8aa165fc951f266667e0605d78b93af', { json: '{\
- : 2067719225654838,......}' })

**请求URL：** `ebprintwaybillcodechange`

**请求方式：** Query/Get

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromPlatform |  | string | [Query/Get] 平台，参数值： |
| timestamp |  | Number | [Query/Get] 时间戳 |
| aopic |  | Number | [Query/Get] 推送类型，1:运单号变动; |
| sign |  | String | [Query/Get] **签名算法：                将json和timestamp参数名和参数值组合起来（注意：json在前，timestamp在后），然后前后添加上AppSecret ，再进行Md5加密（加密算法参考接入指南-完整调用API示例代码中MD5算法）。            **例：            **url：http://test.com/agiso?timestamp=11222212121&sign=f8aa165fc951f266667e0605d78b93af&aopic=256，            **postData: { json: {"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"} }，            **_appsecret: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8(开发者AppSecret)，            **连接后的串: 9f8g9d78sg9d8f8ew9f89ds9f8ds9af8json{"Tid":2067719225654838,"Status":"WAIT_BUYER_CONFIRM_GOODS",......,"TotalFee":"3.00"}timestamp112222121219f8g9d78sg9d8f8ew9f89ds9f8ds9af8            再对连接后的字符串，进行MD5加密，            **MD5结果: f8aa165fc951f266667e0605d78b93af（不区分大小写） |
| json |  | String | [Form/Post] 推送信息,如： |

**推送消息示例：**

```json
{
        "ExpressCompanyName":"中通",    // 快递公司名称
        "ParentWaybillCode":"123456",   // 子母件中的母单号，当为子母件模式时，需要此单号为实际挂载物流详情的单号，需要使用此单号进行发货，查询物流详情，非子母件，此字段为空
        "WaybillCode":"123456789",      // 面单号, 子母件模式下为子面单号
        "WaybillCodeList":[             // 一单多包时的所有运单号
            "123456789",
            "123456780",
            "123456781"
        ],
        "Tids":[                        // 订单编号
            "202010-31654641656"
        ]
    }
```

---
