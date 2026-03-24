# 小红书自动发货 (AldsXhs) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsXhs/`

---

## 发布的商品列表

**简要描述：** 为服务商的卖家提供发布的小红书商品列表

**请求URL：** `/Product/GetList`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| page_no | 是 | Number | 页码从 1 开始 |
| page_size | 是 | Number | 每页的数量,最大100 |
| on_sale | false | Bool | 是否在架上,true:只查询上架的商品,false:查询所有(上架/下架)商品 |
| item_id | false | String | 商品Id(因为历史原因,我们将sku当做商品,实际这个是Sku的Id,对应小红书接口:product.getDetailSkuList) |

**返回示例：**

```json
{
    "isSuccess": true,
    "data": {
      "pageNO": 1,                                              // 页码
      "pageSize": 50,                                           // 每页的数量
      "total": 1,
      "data": [
        {
          "item": {
              "name": "测试商品，虚拟商品，勿拍，勿改",           // 商品标题
              "ename": "",                                     // 商品英文名
              "brandId": 0,                                    // 品牌ID
              "categoryId": "65f996e83e946300016b27e8",        // 末级商品类目ID
              "attributes": [
                  {
                      "propertyId": "626902ed01b3b400010d5b67",     // 属性ID
                      "name": "是否带框",                            // 属性名
                      "valueId": "66264eb02c821c0001a3db57",         // 属性值ID
                      "value": "否",                                 // 属性值，单选属性使用
                      "valueList": []                                // 属性值列表，多选属性填入列表
                  },
                  {
                      "propertyId": "626902ee01b3b400010d5b6d",      // 属性ID
                      "name": "是否限量",                             // 属性名
                      "valueId": "66264eb02c821c0001a3db57",         // 属性值ID
                      "value": "否",                                 // 属性值，单选属性使用
                      "valueList": []                                // 属性值列表，多选属性填入列表
                  },
                  {
                      "propertyId": "626902ee01b3b400010d5ba7",      // 属性ID
                      "name": "作品尺寸",                             // 属性名
                      "value": "10mm*10mm",                          // 属性值，单选属性使用
                      "valueList": []                                // 属性值列表，多选属性填入列表
                  },
                  {
                      "propertyId": "626902ed01b3b400010d5b4d",      // 属性ID
                      "name": "创作年份",                             // 属性名
                      "value": "2025",                               // 属性值，单选属性使用
                      "valueList": []                                // 属性值列表，多选属性填入列表
                  },
                  {
                      "propertyId": "626902ee01b3b400010d5b70",      // 属性ID
                      "name": "题材",                                // 属性名
                      "value": "风景",                               // 属性值，单选属性使用
                      "valueList": [
                          {
                              "valueId": "66264ec22c821c0001a3e02d",     // 属性值ID,接口查不到需要的属性可不填
                              "value": "风景"                            // 属性值，接口查不到需要的属性可自行填写
                          }
                      ]
                  },
                  {
                      "propertyId": "626902ed01b3b400010d5b6a",      // 属性ID
                      "name": "是否签名",                             // 属性名
                      "valueId": "66264eb02c821c0001a3db57",         // 属性值ID，单选属性时必填
                      "value": "否",                                 // 属性值，单选属性使用
                      "valueList": []                                // 属性值列表，多选属性填入列表
                  }
              ],
              "shippingTemplateId": "64f196dee1f0f10001fd8bb1",     // 运费模板ID
              "shippingGrossWeight": 0,                             // 商品物流重量（克），当运费模版选择按重量计费时，该值必须大于0
              "variantIds": [                                       // 商品规格列表
                  "5a60c42f69bd891ed8939bc2"
              ],    
              "images": [
                  "http://qimg.xiaohongshu.com/arkgoods/1040g0o03111p5bu1mk8g5p7hi6f14q14ocupbo0"    // 商品主图
              ],    
              "videoUrl": "",                                        // 主图视频
              "articleNo": "",                                       // 商品货号
              "imageDescriptions": [
                  "http://qimg.xiaohongshu.com/arkgoods/104100ao31bqrrtvr0s069sclc5qg0000000005t6t3hds"    // 图文描述
              ],    
              "transparentImage": "",                                  // 透明图
              "description": "",                                       // 商品描述
              "faq": [],                                               // 常见的问题
              "deliveryMode": 1,                                       // 物流模式,0：普通，1：支持无物流发货（限定类目支持，不支持的类目创建会报错）
              "freeReturn": 1,                                         // 是否支持7天无理由,1：支持，2：不支持，不传会按照规则给默认值，必须支持则支持，不必须则不支持
              "id": "67b6831c7b3de40001a9fb78",                        // spuId,创建时不填，删除更新必填
              "createTime": 1740014364000,                             // spu创建时间
              "updateTime": 1740014448000                              // spu更新时间
          },
          "sku": {
              "itemId": "67b6831c7b3de40001a9fb78",                    // 商品id
              "ipq": 1,                                                // 打包数
              "originalPrice": 100000,                                 // 市场价，单位分
              "price": 99900,                                          // 售价，单位分，要求小于市场价，上限10w元，即10000000分 原来这个字段单位是元
              "stock": 100,                                            // 库存
              "logisticsPlanId": "64f58c46138fbd00012e23b8",           // 物流方案Id
              "whcode": "CPartner",                                    // 仓库号
              "priceType": 0,                                          // 是否包税，0：不包税；1：包税
              "erpCode": "",                                           // 商家编码
              "variants": [
                  {
                      "id": "5a60c42f69bd891ed8939bc2",                // 规格ID(spl与spv规格根据common.getVariations区分，spl规格和spv规格集合需要与spu规格对齐)
                      "name": "款式",                                  // 规格名称
                      "value": "04款",                                 // 规格值(通过common.getAttributeValues获取)，查不到则自行填写
                      "valueId": "662651af2c821c0001a453b1"            // 规格值ID(通过common.getAttributeValues获取)查不到可以不填
                  }
              ],
              "deliveryTime": {
                  "time": "48",                                        // 发货时间，相对时间(X)付款后X天内发货，绝对时间(YYYY/MM/DD)该天24点之前发货
                  "type": "RELATIVE_TIME_NEW"                          // 发货时间类型，DEFAULT:不设置 RELATIVE_TIME:相对时间 ABSOLUTE_TIME:绝对时间
              },
              "specImage": "",                                         // 规格图
              "barcode": "XHS-32JY3DKV2Q68",                           // 商品条形码，创建特定品类必填，普通品类可不填
              "id": "67b6831c7b3de40001a9fb97",                        // skuId,仅更新删除返回使用
              "scSkucode": "XHS-32JY3DKV2Q68",                         // scSkuCode编号,小红书编码
              "logisticsName": "",                                     // 物流模式名
              "buyable": true,                                         // 是否在架上，仅用于返回
              "unionItemDetails": [],                                  // 组合商品子商品信息，仅返回使用
              "createTime": 1740014364000,                             // 商品创建时间，仅返回使用
              "updateTime": 1740014436000,                             // 商品更新时间，仅返回使用
              "name": "测试商品，虚拟商品，勿拍，勿改 04款",             // 商品名称，仅返回使用
              "isGift": false                                          // 是否是赠品
          }
      ]
    },
    "error_Code": 0,
    "error_Msg": ""
  }
```

**备注：** 参考咸鱼：[闲鱼已验货订单查询](https://open.taobao.com/api.htm?docId=56245&docType=2&source=search)

---

## 发送消息

**简要描述：** 发送聊天窗口消息

**请求URL：** `/ImMsg/SendMsg`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| msg | 是 | String | 消息内容（长度限制1000，一笔订单限制2条） |

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

## 商品详情

**简要描述：** 根据小红书商品Id，查询商品详情。

**请求URL：** `/Product/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| item_id | 是 | String | 小红书商品Id(因为历史原因,我们将sku当做商品,实际这个是Sku的Id,对应小红书接口:product.getDetailSkuList) |

**返回示例：**

```json
{
    "isSuccess": true,     // 是否成功
    "data": {
        "item": {
            "name": "测试商品，虚拟商品，勿拍，勿改",           // 商品标题
            "ename": "",                                     // 商品英文名
            "brandId": 0,                                    // 品牌ID
            "categoryId": "65f996e83e946300016b27e8",        // 末级商品类目ID
            "attributes": [
                {
                    "propertyId": "626902ed01b3b400010d5b67",     // 属性ID
                    "name": "是否带框",                            // 属性名
                    "valueId": "66264eb02c821c0001a3db57",         // 属性值ID
                    "value": "否",                                 // 属性值，单选属性使用
                    "valueList": []                                // 属性值列表，多选属性填入列表
                },
                {
                    "propertyId": "626902ee01b3b400010d5b6d",      // 属性ID
                    "name": "是否限量",                             // 属性名
                    "valueId": "66264eb02c821c0001a3db57",         // 属性值ID
                    "value": "否",                                 // 属性值，单选属性使用
                    "valueList": []                                // 属性值列表，多选属性填入列表
                },
                {
                    "propertyId": "626902ee01b3b400010d5ba7",      // 属性ID
                    "name": "作品尺寸",                             // 属性名
                    "value": "10mm*10mm",                          // 属性值，单选属性使用
                    "valueList": []                                // 属性值列表，多选属性填入列表
                },
                {
                    "propertyId": "626902ed01b3b400010d5b4d",      // 属性ID
                    "name": "创作年份",                             // 属性名
                    "value": "2025",                               // 属性值，单选属性使用
                    "valueList": []                                // 属性值列表，多选属性填入列表
                },
                {
                    "propertyId": "626902ee01b3b400010d5b70",      // 属性ID
                    "name": "题材",                                // 属性名
                    "value": "风景",                               // 属性值，单选属性使用
                    "valueList": [
                        {
                            "valueId": "66264ec22c821c0001a3e02d",     // 属性值ID,接口查不到需要的属性可不填
                            "value": "风景"                            // 属性值，接口查不到需要的属性可自行填写
                        }
                    ]
                },
                {
                    "propertyId": "626902ed01b3b400010d5b6a",      // 属性ID
                    "name": "是否签名",                             // 属性名
                    "valueId": "66264eb02c821c0001a3db57",         // 属性值ID，单选属性时必填
                    "value": "否",                                 // 属性值，单选属性使用
                    "valueList": []                                // 属性值列表，多选属性填入列表
                }
            ],
            "shippingTemplateId": "64f196dee1f0f10001fd8bb1",     // 运费模板ID
            "shippingGrossWeight": 0,                             // 商品物流重量（克），当运费模版选择按重量计费时，该值必须大于0
            "variantIds": [                                       // 商品规格列表
                "5a60c42f69bd891ed8939bc2"
            ],    
            "images": [
                "http://qimg.xiaohongshu.com/arkgoods/1040g0o03111p5bu1mk8g5p7hi6f14q14ocupbo0"    // 商品主图
            ],    
            "videoUrl": "",                                        // 主图视频
            "articleNo": "",                                       // 商品货号
            "imageDescriptions": [
                "http://qimg.xiaohongshu.com/arkgoods/104100ao31bqrrtvr0s069sclc5qg0000000005t6t3hds"    // 图文描述
            ],    
            "transparentImage": "",                                  // 透明图
            "description": "",                                       // 商品描述
            "faq": [],                                               // 常见的问题
            "deliveryMode": 1,                                       // 物流模式,0：普通，1：支持无物流发货（限定类目支持，不支持的类目创建会报错）
            "freeReturn": 1,                                         // 是否支持7天无理由,1：支持，2：不支持，不传会按照规则给默认值，必须支持则支持，不必须则不支持
            "id": "67b6831c7b3de40001a9fb78",                        // spuId,创建时不填，删除更新必填
            "createTime": 1740014364000,                             // spu创建时间
            "updateTime": 1740014448000                              // spu更新时间
        },
        "sku": {
            "itemId": "67b6831c7b3de40001a9fb78",                    // 商品id
            "ipq": 1,                                                // 打包数
            "originalPrice": 100000,                                 // 市场价，单位分
            "price": 99900,                                          // 售价，单位分，要求小于市场价，上限10w元，即10000000分 原来这个字段单位是元
            "stock": 100,                                            // 库存
            "logisticsPlanId": "64f58c46138fbd00012e23b8",           // 物流方案Id
            "whcode": "CPartner",                                    // 仓库号
            "priceType": 0,                                          // 是否包税，0：不包税；1：包税
            "erpCode": "",                                           // 商家编码
            "variants": [
                {
                    "id": "5a60c42f69bd891ed8939bc2",                // 规格ID(spl与spv规格根据common.getVariations区分，spl规格和spv规格集合需要与spu规格对齐)
                    "name": "款式",                                  // 规格名称
                    "value": "04款",                                 // 规格值(通过common.getAttributeValues获取)，查不到则自行填写
                    "valueId": "662651af2c821c0001a453b1"            // 规格值ID(通过common.getAttributeValues获取)查不到可以不填
                }
            ],
            "deliveryTime": {
                "time": "48",                                        // 发货时间，相对时间(X)付款后X天内发货，绝对时间(YYYY/MM/DD)该天24点之前发货
                "type": "RELATIVE_TIME_NEW"                          // 发货时间类型，DEFAULT:不设置 RELATIVE_TIME:相对时间 ABSOLUTE_TIME:绝对时间
            },
            "specImage": "",                                         // 规格图
            "barcode": "XHS-32JY3DKV2Q68",                           // 商品条形码，创建特定品类必填，普通品类可不填
            "id": "67b6831c7b3de40001a9fb97",                        // skuId,仅更新删除返回使用
            "scSkucode": "XHS-32JY3DKV2Q68",                         // scSkuCode编号,小红书编码
            "logisticsName": "",                                     // 物流模式名
            "buyable": true,                                         // 是否在架上，仅用于返回
            "unionItemDetails": [],                                  // 组合商品子商品信息，仅返回使用
            "createTime": 1740014364000,                             // 商品创建时间，仅返回使用
            "updateTime": 1740014436000,                             // 商品更新时间，仅返回使用
            "name": "测试商品，虚拟商品，勿拍，勿改 04款",             // 商品名称，仅返回使用
            "isGift": false                                          // 是否是赠品
        }
    },
    "error_Code": 0,     // 错误码
    "error_Msg": ""     // 错误信息
}
```

**备注：** 参考咸鱼：[服务商闲鱼商品查询](https://open.taobao.com/api.htm?docId=49488&docType=2&source=search)

---

## 执行自动发货

**简要描述：** 调用该接口将根据您在自动发货后台设定的发货规则，进行一次发货逻辑的处理。该操作等同于在[手动发货页面](https://aldsxhs.agiso.com/#/alds/manualSend)的操作。注意：该页面执行后，也会自动发送小红书消息，可以通过参数中的选项控制发货中的一些限制。

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

## 更新发货状态

**简要描述：** 执行无物流发货，更新发货状态

**请求URL：** `/Order/DummySend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| expressCode | 是 | String | 快递公司编码（如使用无物流发货，expressCode为selfdelivery） |
| expressNo | 是 | String | 快递单号（如使用的是无物流发货，expressNo为发货内容） |

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
                "tag": "xhs_3587c6da8674"                                                   // 透传字段
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
| tid | 是 | String | 订单号 |

**返回示例：**

```json
{
      "isSuccess": true,
        "data": {
            "orderId": "123456",                               // 订单号
            "orderType": 1,                                    // 包裹类型，1普通 2定金预售 3全款预售 4延迟发货 5换货补发
            "orderStatus": 2,                                  // 包裹状态，1已下单待付款 2已支付处理中 3清关中 4待发货 5部分发货 6待收货 7已完成 8已关闭 9已取消 10换货申请中
            "orderAfterSalesStatus": 1,                        // 售后状态，1无售后 2售后处理中 3售后完成(含取消)
            "cancelStatus": 0,                                 // 申请取消状态，0未申请取消 1取消处理中
            "createdTime": 1640995200000,                      // 创建时间 单位ms
            "paidTime": 1640995200000,                         // 支付时间 单位ms
            "updateTime": 1640995200000,                       // 更新时间 单位ms
            "deliveryTime": 1640995200000,                     // 包裹发货时间 单位ms
            "cancelTime": 1640995200000,                       // 包裹取消时间 单位ms
            "finishTime": 1640995200000,                       // 包裹完成时间 单位ms
            "promiseLastDeliveryTime": 1640995200000,          // 承诺最晚发货时间 单位ms
            "planInfoId": "abc123",                            // 物流方案id
            "planInfoName": "物流方案名称",                     // 物流方案名称
            "receiverCountryId": "CN",                         // 收件人国家id
            "receiverCountryName": "中国",                     // 中国
            "receiverProvinceId": "123",                       // 收件人省份id
            "skuList": [
                {
                    "skuId": "sku123",                         // 商品id
                    "skuName": "商品名称",                      // 商品名称
                    "erpcode": "erp123",                       // 商家编码(若为组合品，暂不支持组合品的商家编码，但skulist会返回子商品商家编码)
                    "skuSpec": "规格",                         // 规格
                    "skuImage": "image.jpg",                   // 商品图片url
                    "skuQuantity": 10,                         // 商品数量
                    "skuDetailList": [
                        {
                            "skuId": "detailSku123",            // 单品商品Id(渠道商品为生成渠道商品的原商品单品id，组合商品为各个子商品的单品id，多包组为对应单包组商品id,商家编码同理)
                            "erpCode": "detailErp123",         // 商家编码
                            "barcode": "123456",               // 商品条码
                            "scSkuCode": "sc123",              // 商品编码
                            "quantity": 5,                     // 购买数量
                            "registerName": "商品1号",         // 商品备案名称 商品1号
                            "skuName": "商品1号",              // 商品名 商品1号
                            "pricePerSku": 100,                // 单个sku价格
                            "taxPerSku": 10,                   // 单个sku税金
                            "paidAmountPerSku": 90,            // 单个sku实付
                            "depositAmountPerSku": 20,         // 单个sku定金
                            "merchantDiscountPerSku": 5,       // 单个sku商家承担优惠
                            "redDiscountPerSku": 5,            // 单个sku平台承担优惠
                            "rawPricePerSku": 110              // 单个sku原价
                        }
                    ],
                    "totalPaidAmount": 900,                    // 总支付金额（考虑总件数）商品总实付
                    "totalMerchantDiscount": 50,               // 商家承担总优惠
                    "totalRedDiscount": 50,                    // 平台承担总优惠
                    "totalTaxAmount": 100,                     // 商品税金
                    "totalNetWeight": 500,                     // 商品总净重
                    "skuTag": 0,                               // 是否赠品，1 赠品 0 普通商品
                    "isChannel": false,                        // 是否是渠道商品
                    "Channel": false                           //
                }
            ],
            "boundExtendInfo": {
                "payNo": "pay123",                             // 交易流水号
                "payChannel": "AliPay",                        // 交易渠道，AliPay=支付宝，TP=微信
                "productValue": "1000",                        // 订单价值（货值，订单商品申价之和（税前价））
                "payAmount": "900",                            // 订单支付金额（含运费）
                "taxAmount": "100",                            // 订单税金
                "shippingFee": "50",                           // 运费 含运费税
                "discountAmount": "50",                        // 订单优惠
                "zoneCodes": ["123", "456"]                    // 海关三级地址区域编码
            },
            "transferExtendInfo": {
                "internationalExpressNo": "express123",        // 国际快递单号
                "orderDeclaredAmount": 1000,                   // 订单申报金额
                "paintMarker": "marker",                       // 大头笔
                "collectionPlace": "place",                    // 集包地
                "threeSegmentCode": "code"                     // 三段码
            },
            "simpleDeliveryOrderList": [
                {
                    "deliveryPackageIndex": "index123",        // 发货包裹索引标识 修改快递单号会使用
                    "status": 4,                               // 发货包裹状态,1:已下单待付款 2:已支付处理中 3:清关中 4:待发货 6:待收货 7:已完成 8:已关闭 9:已取消 10:换货申请中
                    "expressTrackingNo": "tracking123",        // 拆包快递单号
                    "expressCompanyCode": "company123",        // 快递公司代码
                    "skuIdList": ["sku1", "sku2"]              // 此发货包裹中有哪些商品，status=4待发货时，列表中的item可以拆包发货。status=6时，列表中的item共享相同的快递公司和单号，修改时一起修改
                }
            ]
        },
      "error_Code": 0,
      "error_Msg": ""
    }
```

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
