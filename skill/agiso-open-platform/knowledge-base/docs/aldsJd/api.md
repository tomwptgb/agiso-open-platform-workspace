# 京东自动发货 (AldsJd) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsJd/`

---

## 更新发货状态

**简要描述：** 执行无物流发货，更新发货状态

**请求URL：** `/Order/DummySend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| orderId | 是 | Long | 订单号 |
| logiCoprId | 是 | String | 物流公司ID(只可通过获取商家物流公司接口获得),多个物流公司以|分隔。如：2100|4700。请注意：如果填写厂家自送（1274），则不会保存物流单号，也不会有具体的跟踪信息。 |
| logiNo | 否 | String | 运单号(当厂家自送时运单号可为空，不同物流公司的运单号用|分隔，如果同一物流公司有多个运单号，则用英文逗号分隔) 。如：1200458628372,111232|468778814888,323232323 |

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

## 检索单个SOP订单信息

**简要描述：** 输入单个SOP订单id，得到所有相关订单信息

**请求URL：** `/Order/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| order_id | 是 | String | 订单号 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
          "orderId": "153652861660",  // 订单id
          "venderId": "624092",       // 商家id，商家编号
          "orderType": "22",          // 订单类型（22 SOP； 75 LOC；21:FBP，112:FCS，142:IBS） 可选字段，需要在输入参数optional_fields中写入才能返回
          "orderState": "FINISHED_L",  // 订单状态（英文）；枚举值：1）WAIT_SELLER_STOCK_OUT 等待出库 2）WAIT_GOODS_RECEIVE_CONFIRM 等待确认收货 3）WAIT_SELLER_DELIVERY等待发货（只适用于海外购商家，含义为“等待境内发货”标签下的订单,非海外购商家无需使用） 4) POP_ORDER_PAUSE POP暂停 5）FINISHED_L 完成 6）TRADE_CANCELED 取消 7）LOCKED 已锁定 8）WAIT_SEND_CODE 等待发码（LOC订单特有状态） 9）PAUSE 暂停（等待出库之前的状态） 10)DELIVERY_RETURN 配送退货 11）UN_KNOWN 未知 请联系运营
          "orderRemark": "",          // 订单状态说明（中文）
          "orderStartTime": "2021-04-07 19:35:50",   // 下单时间
          "itemInfoList": [ 
            {
              "skuId": "72143855364",    // 京东内部SKU的ID
              "outerSkuId": "TTB007x05", // SKU外部ID（极端情况下不保证返回，建议从商品接口获取
              "skuName": "二代OMS测试-勿拍", // 商品的名称+SKU规格
              "jdPrice": "1.00",  // 	SKU的京东价
              "giftPoint": "0",  // 赠送积分
              "wareId": "14459363073",  // 京东内部商品ID（极端情况下不保证返回，建议从商品接口获取）
              "itemTotal": "1",  // 数量
              "productNo": "",   // 货号
              "newStoreId": "0"  // item维度的仓库id
            }
          ],
          "returnOrder": "0",        // 售后订单标记 0:不是换货订单 1返修发货,直接赔偿,客服补件 2售后调货 可选字段，需要在输入参数optional_fields中写入才能返回
          "paymentConfirmTime": "2021-04-07 19:36:14"    // 付款确认时间 如果没有付款时间 默认返回0001-01-01 00:00:00 可选字段
        },
        "error_Code": 0,
        "error_Msg": ""
      }
```

---

## 游戏点卡点卡订单发货

**简要描述：** 点卡订单发货（不同的订单类型需要调用不同接口发货）

**请求URL：** `/GameCard/CardSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |
| cardJson | 是 | String | [{"cardno":"卡号1","cardpass":"卡密1"},{"cardno":"卡号2","cardpass":"卡密2"}] |

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

## 游戏点卡直充订单发货

**简要描述：** 直充订单发货（不同的订单类型需要调用不同接口发货）

**请求URL：** `/GameCard/RechargeSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

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

## 游戏点卡订单退款

**简要描述：** 将游戏点卡订单退款掉

**请求URL：** `/GameCard/Refund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

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

## 获取商家已签约承运商

**简要描述：** 获取商家已签约承运商

**请求URL：** `/User/GetVenderCarrier`

**请求方式：** POST

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
          {
            "id": 2087,
            "name": "京东快递"
          },
          {
            "id": 1499,
            "name": "中通速递"
          },
          {
            "id": 465,
            "name": "邮政EMS"
          },
          {
            "id": 256059,
            "name": "DHL"
          },
          {
            "id": 1327,
            "name": "韵达快递"
          },
          {
            "id": 2170,
            "name": "邮政快递包裹"
          },
          {
            "id": 1665004,
            "name": "云仓速递"
          },
          {
            "id": 463,
            "name": "圆通快递"
          },
          {
            "id": 773574,
            "name": "京东快运"
          },
          {
            "id": 3046,
            "name": "德邦快递"
          },
          {
            "id": 1819479,
            "name": "丰网速运"
          },
          {
            "id": 1747,
            "name": "优速快递"
          },
          {
            "id": 2094,
            "name": "快捷速递"
          },
          {
            "id": 2096,
            "name": "联邦快递"
          },
          {
            "id": 2105,
            "name": "速尔快递"
          },
          {
            "id": 323141,
            "name": "亚风快运"
          },
          {
            "id": 599866,
            "name": "跨越速运"
          },
          {
            "id": 605050,
            "name": "中铁CRE"
          },
          {
            "id": 596494,
            "name": "安能快递"
          },
          {
            "id": 692584,
            "name": "品骏快递"
          },
          {
            "id": 732960,
            "name": "EWE智慧物流"
          },
          {
            "id": 740588,
            "name": "久耶供应链"
          },
          {
            "id": 668392,
            "name": "RoyalMail"
          },
          {
            "id": 1362538,
            "name": "联通码上购"
          },
          {
            "id": 2130,
            "name": "德邦物流"
          },
          {
            "id": 2462,
            "name": "天地华宇"
          },
          {
            "id": 4832,
            "name": "安能物流"
          },
          {
            "id": 5419,
            "name": "中铁物流"
          },
          {
            "id": 336878,
            "name": "京东大件物流"
          },
          {
            "id": 247899,
            "name": "安得物流"
          },
          {
            "id": 680414,
            "name": "中通快运"
          },
          {
            "id": 832230,
            "name": "顺心捷达"
          },
          {
            "id": 1325880,
            "name": "壹米滴答"
          },
          {
            "id": 467,
            "name": "顺丰快递"
          },
          {
            "id": 171686,
            "name": "易宅配物流"
          },
          {
            "id": 222693,
            "name": "贝业新兄弟"
          },
          {
            "id": 731302,
            "name": "韵达快运"
          },
          {
            "id": 1549,
            "name": "宅急便"
          },
          {
            "id": 568096,
            "name": "万家康"
          },
          {
            "id": 6012,
            "name": "斑马物联网"
          },
          {
            "id": 617027,
            "name": "POP国际物流"
          },
          {
            "id": 688636,
            "name": "增速益"
          },
          {
            "id": 689816,
            "name": "集成"
          },
          {
            "id": 724080,
            "name": "珠海广丰"
          },
          {
            "id": 1369364,
            "name": "麦哲伦跨境物流"
          },
          {
            "id": 2171,
            "name": "中国邮政挂号信"
          },
          {
            "id": 332098,
            "name": "用户自提"
          },
          {
            "id": 831932,
            "name": "京东同城速配"
          },
          {
            "id": 3668,
            "name": "邮政EMS标准快递"
          },
          {
            "id": 1274,
            "name": "厂家自送"
          },
          {
            "id": 1409,
            "name": "宅急送"
          },
          {
            "id": 471,
            "name": "龙邦快递"
          },
          {
            "id": 881232,
            "name": "众邮快递"
          }
        ],
        "error_Code": 0,
        "error_Msg": "",
        "allowRetry": null,
        "requestId": "20222027142251106"
      }
```

---

## 通用交易订单发货

**简要描述：** 通用交易订单发货

**请求URL：** `/Vtp/Send`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

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

## 通用交易订单退款

**简要描述：** 将通用交易订单退款掉

**请求URL：** `/Vtp/Refund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | Long | 订单号 |

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
