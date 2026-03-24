# 卡券自动充值 (ACPR) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/acpr/`

---

## 创建入库批次号

**请求URL：** `/CardPwd/CreateStockInBatchId`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpkId | 是 | Long | 卡种Id |
| price | 否 | Decimal | 成本单价 |
| summary | 否 | String | 批次描述 |

**返回示例：**

```json
{
            "IsSuccess": true,
            "Data": "fe71483c21a846b58e0c369224eee38f",
            "Error_Code": 0,
            "Error_Msg": "",
            "AllowRetry": null,
            "RequestId": "20211108142251106"
          }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| Data | String | 批次号 |

---

## 加卡

**请求URL：** `/CardPwd/StockIn`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| stockInBatchId | 是 | String | 入库批次号 |
| data | 是 | String | 卡券内容，内容格式需要根据卡种类型，具体查看备注 |
| isUseFirst | 否 | Bool | 优先出售 |
| allowReplace | 否 | Bool | 覆盖已存在的 |
| expireTime | 否 | String | 注：卡种开启到期日时必填，其他忽略 |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
            "AddFailCount": 0,
            "AddSuccessCount": 2,
            "ReplaceSoldSuccessCount": 0,
            "ReplaceUnSoldSuccessCount": 0,
            "ResultMsg": ""
          },
          "Error_Code": 0,
          "Error_Msg": "",
          "AllowRetry": null,
          "RequestId": "20211108142251106"
        }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| AddFailCount | Int | 添加失败数量 |
| AddSuccessCount | String | 添加成功数量 |
| ReplaceSoldSuccessCount | String | 覆盖成功数量 |
| ReplaceUnSoldSuccessCount | String | 覆盖失败 |
| ResultMsg | String | 消息内容 |

**备注：** 卡种类型对应加卡"data"参数JSON格式例子：700:循环卡:[{"CardNo":"卡号","Pwd":"卡密"}]  800:套卡：[{"CardNo":"卡号"}]820:唯一卡：[{"CardNo":"卡号","Pwd":"卡密"}]  840:重复卡：[{"CardNo":"卡号","Pwd":"卡密"}] 850:图片卡：[{"Url":"图片URL地址","Md5":"图片M5d值","OriName":"图片名称"}] 如果只有卡号没有卡密的场景，Pwd就不用传了。eg：820:唯一卡：[{"CardNo":"卡号"}]

---

## 发卡方案提卡

**简要描述：** 发卡方案提卡

**请求URL：** `/SendCardPlan/HandPick`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| buyer | 否 | String | 买家名称 |
| spId | 是 | Long | 发卡方案idNo |
| num | 是 | Number | 数量 |
| payment | 是 | Decimal | 金额 |
| keyword | 否 | String | 关键词，根据发卡方案类型（按地址组合、按留言组合）传值 |

**返回示例：**

```json
{
            "IsSuccess": true,
            "Data": [
              {
                  "CardNoShowType": 0,   // 卡号展示类型
                  "PwdShowType": 0,      // 卡密展示类型
                  "PrefixCardNo": "卡号：",  // 卡号前缀
                  "PrefixPwd": "密码：",   // 卡密前缀
                  "Title": "n1",   // 卡种名称
                  "CpkId": 729,    // 卡种ID
                  "CardPwdArr": [  // 卡号卡密数组
                      {
                          "c": "【3】卡号：1000",  // 卡号
                          "p": ""                 // 卡密
                      },
                      {
                          "c": "【4】卡号：1000",
                          "p": ""
                      }
                  ]
              },
              {
                  "CardNoShowType": 0,
                  "PwdShowType": 0,
                  "PrefixCardNo": "卡号：",
                  "PrefixPwd": "密码：",
                  "Title": "n2",
                  "CpkId": 730,
                  "CardPwdArr": [
                      {
                          "c": "【6】卡号：2000",
                          "p": ""
                      },
                      {
                          "c": "【7】卡号：2000",
                          "p": ""
                      },
                      {
                          "c": "【8】卡号：2000",
                          "p": ""
                      },
                      {
                          "c": "【9】卡号：2000",
                          "p": ""
                      }
                  ]
              }
          ],
            "Error_Code": 0,
            "Error_Msg": "",
            "AllowRetry": null,
            "RequestId": "20230108142251106"
          }
```

**备注：** 发卡方案类型：0:组合卡、1:按数量组合、2:按数量区间组合、3:按地址组合、4:按留言组合、4:多组合顺序选一、5:多组合随机选一

---

## 提卡

**简要描述：** 提卡

**请求URL：** `/CardPwd/HandPick`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpkId | 是 | Long | 卡种Id |
| num | 是 | Int | 提卡数量 |
| handPickOrderId | 是 | String | 接入方订单编号 |
| buyer | 否 | String | 买家名称 |
| buildCpd | 否 | Bool | 生成完整卡券提取链接，默认False |
| usePriority | 否 | Bool | 优先出库标识为“优先出售”的卡密，默认True |

**返回示例：**

```json
{
        "IsSuccess": true,
        "Data": {
          // buildCpd传true时返回
          "CpdUrl": "https://mai.91kami.com/cpd/lu3hmk684kfch1n9wfauphnkx7eyrncqf78a39462da14270bd8666333404d81b.aspx" 
          //buildCpd传false时返回
          "CardPwdArr": [
            {
              "c": "xx003",              // 卡号
              "p": "123",                // 密码
              "d": "2024-11-21 23:59:59" // 到期时间
            }
          ]
        },
        "Error_Code": 0,
        "Error_Msg": "",
        "AllowRetry": null,
        "RequestId": "20211108142251106"
      }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| CpdUrl | String | 请求参数 “buildCpd” 为 true 返回链接地址 |
| CardPwdArr | String | 请求参数 “buildCpd” 为 false 时返回卡密信息集合如：[ {"c":"卡号1", "p":"密码1", "d":"2024-11-15 23:59:59"},{"c":"卡号2", "p":"密码3", "d":"2024-11-15 23:59:59"} ] |

---

## 更新发卡方案

**简要描述：** 更新发卡方案

**请求URL：** `/SendCardPlan/Update`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| IdNo | 是 | Long | 发卡方案IdNo |
| PlanJson | 是 | String | JSON数据结构（根据PlanType类型）字符串，可参考发卡方案列表接口示例 |
| Title | 是 | String | 发卡方案名称 |
| AliasName | 否 | String | 别名 |

**返回示例：**

```json
{
            "IsSuccess": true,
            "Error_Code": 0,
            "Error_Msg": "",
            "AllowRetry": null,
            "RequestId": "20230108142251106"
          }
```

---

## 获取卡种列表

**简要描述：** 获取卡种列表

**请求URL：** `/CardPwd/GetList`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| pageIndex | 是 | Long | 页码默认 1 |
| pageSize | 是 | Long | 默认100，最大100 |
| filterName | 否 | String | 卡种名称，支持模糊匹配 |
| classId | 否 | Int | 卡种分类Id |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
            {
              "List":[
                {
                  "IdNo":123110,
                  "CardType":820,
                  "Title":"测试Jd",
                  "RemainingCount":13,
                  "UsedCount":1,
                  "TotalCount":14,
                  "CreateTime":"2021-06-15 18:43:16",
                  "PurPrice":"1"
                }
              ],
              "TotalCount":65,
              "PageNo":1,
              "PageSize":20
            }
          },
          "Error_Code": 0,
          "Error_Msg": "",
          "AllowRetry": null,
          "RequestId": "20211108142251106"
        }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| IdNo | Long | Id |
| CardType | Long | 卡种类型 |
| title | String | 卡种名称 |
| RemainingCount | Int | 库存 |
| UsedCount | Int | 已用数量 |
| TotalCount | Int | 总数量 |
| CreateTime | String | 创建时间 |
| PurPrice | Decimal | 成本单价 |

**备注：** 卡种类型：700:循环卡、800:套卡、820:唯一卡、840:重复卡、850:图片卡

---

## 获取卡种详情

**简要描述：** 获取卡种详情

**请求URL：** `/CardPwdKind/GetDetails`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| cpkId | 是 | Long | 卡种Id |

**返回示例：**

```json
{
            "IsSuccess": true,
            "Data": {
              "IdNo": 32,
              "Title": "京东激活码",
              "AliasName": null,
              "ClassId": 0,
              "Sort": 0,
              "WarningNum": 5,
              "TotalCount": 3,
              "UsedCount": 1,
              "LockingCount": 0,
              "CardType": 800,
              "CardNoShowType": 0,
              "PwdShowType": 0,
              "ShowTpl": "{卡号}",
              "PrefixCardNo": "",
              "PrefixPwd": "",
              "SplitCardPwd": null,
              "PurPrice": 0.00000000,
              "ModifyTime": "2017-12-07T16:59:54",
              "CreateTime": "2017-12-07T16:40:59"
            },
            "Error_Code": 0,
            "Error_Msg": "",
            "AllowRetry": null,
            "RequestId": "20211122942251106"
          }
```

**返回参数说明：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| IdNo | Long | Id |
| title | String | 卡种名称 |
| AliasName | String | 卡种别名 |
| ClassId | Long | 卡种分类 |
| Sort | Int | 排序 |
| WarningNum | Int | 预警数量 |
| TotalCount | Int | 总数量 |
| UsedCount | Int | 已用数量 |
| LockingCount | Int | 锁定数量 |
| CardType | Long | 卡种类型 |
| CardNoShowType | Int | 卡号显示类型 |
| PwdShowType | Int | 密码显示类型 |
| ShowTpl | String | 显示模板 |
| PrefixCardNo | String | 卡号前缀 |
| PrefixPwd | String | 密码前缀 |
| SplitCardPwd | String | 分隔符 |
| PurPrice | Decimal | 成本单价 |
| ModifyTime | String | 修改时间 |
| CreateTime | String | 创建时间 |

**备注：** 卡种类型：700:循环卡、800:套卡、820:唯一卡、840:重复卡、850:图片卡卡号及密码显示类型：0:文本、1:条形码、2:二维码、4:条形码+二维码

---

## 获取发卡方案列表

**简要描述：** 获取发卡方案列表

**请求URL：** `/SendCardPlan/getlist`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| pageIndex | 是 | Long | 页码默认 1 |
| pageSize | 是 | Long | 默认20 |
| filterName | 否 | String | 发卡方案名称 |

**返回示例：**

```json
{
            "IsSuccess": true,
            "Data": {
              "List": [
                {
                    "IdNo": 193,
                    "Title": "多组合随机选一",
                    "PlanType": 6,
                    "PlanJson": "[[{"Name":"n1","GroupCard":[{"Denom":1.0,"CpkId":721}]}],[{"Name":"n2","GroupCard":[{"Denom":1.0,"CpkId":720}]}]]",  // 多组合随机选一 Json字符串数据结构
                    "CardKindIds": ",721,720,",
                    "CreateTime": "2023-03-21 10:38:37",
                    "ModifyTime": "2023-03-21 10:41:49",
                    "ShowName": "多组合随机选一"
                },
                {
                    "IdNo": 192,
                    "Title": "多组合顺序选一",
                    "PlanType": 5,
                    "PlanJson": "[[{"Name":"n1","GroupCard":[{"Denom":1.0,"CpkId":716}]}],[{"Name":"n2","GroupCard":[{"Denom":1.0,"CpkId":714}]}]]",  // 多组合顺序选一 Json字符串数据结构
                    "CardKindIds": ",716,714,",
                    "CreateTime": "2023-03-21 10:32:07",
                    "ShowName": "多组合顺序选一"
                },
                {
                    "IdNo": 191,
                    "Title": "按留言组合",
                    "PlanType": 4,
                    "PlanJson": "[{"Keyword":"ka1","Pri":1,"GroupCard":[{"Denom":1.0,"CpkId":721}]}]",  // 按留言组合 Json字符串数据结构
                    "CardKindIds": ",721,",
                    "CreateTime": "2023-03-21 10:30:14",
                    "ShowName": "按留言组合"
                },
                {
                    "IdNo": 190,
                    "Title": "按地址",
                    "PlanType": 3,
                    "PlanJson": "[{"Keyword":"厦门","Pri":1,"GroupCard":[{"Denom":1.0,"CpkId":719}]},{"Keyword":"福州","Pri":2,"GroupCard":[{"Denom":1.0,"CpkId":721}]}]",  // 按地址 Json字符串数据结构
                    "CardKindIds": ",719,721,",
                    "CreateTime": "2023-03-21 10:28:25",
                    "ShowName": "按地址"
                },
                {
                    "IdNo": 189,
                    "Title": "按数量组合",
                    "PlanType": 1,
                    "PlanJson": "[{"BuyNum":1,"GroupCard":[{"Num":1,"CpkId":721},{"Num":1,"CpkId":719}]}]",  // 按数量组合 Json字符串数据结构
                    "CardKindIds": ",721,719,",
                    "CreateTime": "2023-03-21 10:19:06",
                    "ShowName": "按数量组合"
                },
                {
                    "IdNo": 188,
                    "Title": "普通组合",
                    "PlanType": 0,
                    "PlanJson": "[{"Denom":1.0,"CpkId":721},{"Denom":2.0,"CpkId":720}]",  // 普通组合 Json字符串数据结构
                    "CardKindIds": ",721,720,",
                    "CreateTime": "2023-03-21 10:18:25",
                    "ShowName": "普通组合"
                },
                {
                    "IdNo": 187,
                    "Title": "按数量区间组合",
                    "PlanType": 2,
                    "PlanJson": "[{"Interval":{"S":1,"E":1},"GroupCard":[{"Denom":2.0,"Num":1,"CalcType":1,"CpkId":692},{"Denom":1.0,"Num":1,"CalcType":1,"CpkId":693}]}]",  // 按数量区间组合 Json字符串数据结构
                    "CardKindIds": ",692,693,",
                    "CreateTime": "2023-01-29 09:40:43",
                    "ModifyTime": "2023-01-29 11:50:49",
                    "ShowName": "按数量区间组合"
                }
            ],
            "TotalCount": 7,
            "PageNo": 1,
            "PageSize": 20
          },
            "Error_Code": 0,
            "Error_Msg": "",
            "AllowRetry": null,
            "RequestId": "20230108142251106"
          }
```

**备注：** 发卡方案类型：0:组合卡、1:按数量组合、2:按数量区间组合、3:按地址组合、4:按留言组合、4:多组合顺序选一、5:多组合随机选一 PlanJson对象属性说明： CpkId：卡种Id； Denom：发货倍数； Num：实发数量； CalcType：数量计算方式，1：按发货倍数计算（Denom）2：按实发数量计算（Num）； Interval：数量区间， Interval.S：区间起始数量、Interval.E：区间结束数量； Pri：优先级；

---

## 获取发卡方案详情

**简要描述：** 获取发卡方案详情

**请求URL：** `/Sendcardplan/Get`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| idNo | 是 | Long | 发卡方案idNo |

**返回示例：**

```json
{
            "IsSuccess": true,
            "Data": {
              "IdNo": 187, 
              "Title": "按数量区间组合",
              "PlanType": 2,  // 发卡方案类型
              "PlanJson": "[{"Interval":{"S":1,"E":1},"GroupCard":[{"Denom":2.0,"Num":1,"CalcType":1,"CpkId":692},{"Denom":1.0,"Num":1,"CalcType":1,"CpkId":693}]}]",  // 发卡方案Json字符串数据结构
              "CardKindIds": ",692,693,",  // 卡种Id
              "CreateTime": "2023-01-29 09:40:43",
              "ModifyTime": "2023-01-29 11:50:49",
              "ShowName": "按数量区间组合"
          },
            "Error_Code": 0,
            "Error_Msg": "",
            "AllowRetry": null,
            "RequestId": "20230108142251106"
          }
```

**备注：** 发卡方案类型：0:组合卡、1:按数量组合、2:按数量区间组合、3:按地址组合、4:按留言组合、4:多组合顺序选一、5:多组合随机选一

---
