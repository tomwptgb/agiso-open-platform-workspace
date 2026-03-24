# 抖店自动发货 (AldsDoudian) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/aldsDoudian/`

---

## 一单多包发货

**简要描述：** 一单多包发货

**请求URL：** `/Order/LogisticsAddMultiPack`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | string | 订单号 |
| requestId | 是 | string | 请求唯一标识(一个guid)，相同request_id多次请求，第一次请求成功后，后续的请求会触发幂等，会直接返回第一次请求成功的结果，不会实际触发发货。格式：1267250f-8b9d-4d9e-9fad-0cd9629c83de |
| packParam | 是 | string | 包裹参数(内容:一个包裹含一个物流单号和单个/多个子订单号，单次请求包裹数过多容易引发超时，建议拆单数量不要超过20)，josn格式, 注意：反序列化后是List<>格式，例：[{"logistics_code":"SF1234567891011","company_code":"shunfeng","shipped_order_info":[{"shipped_order_id":"6932769172126242331","shipped_num":1}]}] |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "pack_list": [                                   // 包裹信息
                {
                    "logistics_code": "SF1234567891011",     // 物流单号
                    "shipped_order_info": [                  // 发货的订单信息
                        {
                            "shipped_order_id": "6932769172126242331",   // 发货的子订单id
                            "shipped_num": 1,                            // 发货的子订单数量
                            "shipped_item_ids": []                       // 发货的四层单id
                        }
                    ],
                    "pack_id": "7398056775972421900"                     // 包裹id
                }
            ]
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 发送消息

**简要描述：** 发送聊天窗口消息

**请求URL：** `/ImMsg/SendMsg`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 订单号 |
| msg | 是 | String | 消息内容（一笔订单限制2条） |

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

**简要描述：** 根据手机号码发送短信(支持多个)

**请求URL：** `/Sms/Send`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| phones | 是 | String | 密文手机号，多个号码用半角逗号分隔。（示例：A**tgghbdfs,A**SSDFVewr） |
| templateId | 是 | String | 短信模板Id |
| templateParam | 否 | JSON | 模板参数,替换短信模板里的占位符，示例:短信模板内容为：订单号：${orderId}，传递：{“orderId”:"123"}会将对应的占位符替换，输出内容：订单号：123 |
| signName | 否 | String | 指定发送短信时使用的签名，默认取最早有效签名 |
| smsAccountType | 否 | Int | 所属关联通道: 0普通短信(默认) 1教育类短信 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
            {
                "message_id": "",
                "code": 628003202,
                "message": "该商家向该手机号发送短信条数已达到限制: 187xxx"
            },
            {
                "message_id": "112cb8e3-debc-4a12-b669-d1dde1e120c7",
                "code": 0,
                "message": ""
            }
        ],
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 取消直充订单(退款)

**简要描述：** 取消直充订单（退款），该接口只适用抖店直充业务的订单状态更新，不支持其它类型的订单。

**请求URL：** `/Topup/Refund`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 直充订单号 |

**返回示例：**

```json
{
        "isSuccess": true,
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 售后商家填写物流信息

- 适用场景：
- send_type=1：用于补寄商家发货
- send_type=3：超市预约上门取货；退货退款和换货场景下商家帮买家填写退货物流信息；
- send_type=4：维修场景下商家帮买家填写退货物流信息；

**请求URL：** `/Order/AfterSaleFillLogistics`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| aftersaleId | 是 | Long | 售后单ID |
| sendType | 是 | int | 发货类型；适用场景： send_type=1：用于补寄商家发货 send_type=3：超市预约上门取货；退货退款和换货场景下商家帮买家填写退货物流信息； send_type=4：维修场景下商家帮买家填写退货物流信息； |
| companyCode | 是 | String | 物流公司编号 pick_up_type 2:线下取货;3:用户退回，无需物流公司，可传 - |
| trackingNo | 是 | String | 物流单号 pick_up_type 2:线下取货;3:用户退回，无需快递单号，可传 - |
| bookTimeBegin | 否 | Long | 预约上门取货时间戳，单位：秒（目前抖超小时达店铺使用） |
| bookTimeEnd | 否 | Long | 预约上门取货时间戳，单位：秒（目前抖超小时达店铺使用） |
| storeId | 否 | String | 门店Id |
| pickUpType | 否 | Int | 1:自行配送;2:线下取货;3:用户退回 ，不传默认自行配送；适用于send_type=3超市预约上门取货场景(不传默认是:1) |

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

## 售后订单查询

**简要描述：** 售后订单查询

**请求URL：** `/Order/AfterSaleList`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| page | 是 | int | 页码,第几页,从0开始 |
| size | 是 | int | 每页的数量,最多支持100条 |
| startTime | 否 | DateTime | 订单售后申请的开始时间 (2024-10-10 或 2024-10-10 00:00:00) |
| endTime | 否 | DateTime | 订单售后申请的结束时间 (2024-10-20 或 2024-10-20 23:59:59) |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "items": [
                {
                    "aftersale_info": {                                  // 售后信息
                        "aftersale_status_to_final_time": 1731986642,    // 售后完结时间，完结时间是平台根据商品的类型，售后状态等综合判断生成，当售后单有完结时间返回时售后单不可再做任何操作；未完结售后单的该字段值为0；Unix时间戳：秒
                        "aftersale_id": "146701382803677771",            // 售后单号
                        "aftersale_order_type": 1,                       // 售后订单类型，枚举为-1(历史订单),1(商品单),2(店铺单)
                        "aftersale_type": 1,                             // 售后类型，枚举为0(退货退款),1(已发货仅退款),2(未发货仅退款),3(换货),6(价保),7(补寄)
                        "aftersale_status": 12,                          // 售后状态和请求参数standard_aftersale_status字段对应；3-换货待买家收货；6-待商家同意；7-待买家退货；8-待商家发货；11-待商家二次同意；12-售后成功；14-换货成功；27-商家一次拒绝；28-售后失败；29-商家二次拒绝；
                        "related_id": "6936476692437472563",             // 关联的订单ID
                        "apply_time": 1731986326,                        // 申请时间
                        "update_time": 1731986645,                       // 最近更新时间
                        "status_deadline": 0,                            // 当前节点逾期时间
                        "refund_amount": 1,                              // 售后退款金额，单位为分
                        "refund_post_amount": 0,                         // 售后退运费金额，单位为分
                        "aftersale_num": 1,                              // 售后数量
                        "part_type": 0,                                  // 部分退类型
                        "aftersale_refund_type": 0,                      // 售后退款类型，枚举为-1(历史数据默认值),0(订单货款/原路退款),1(货到付款线下退款),2(备用金),3(保证金),4(无需退款),5(平台垫付)
                        "refund_type": 0,                                // 退款方式，枚举为1(极速退款助手)、2(售后小助手)、3(售后急速退)、4(闪电退货)
                        "arbitrate_status": 0,                           // 仲裁状态，枚举为0(无仲裁记录),1(仲裁中),2(客服同意),3(客服拒绝),4(待商家举证),5(协商期),255(仲裁结束)
                        "create_time": 1731986327,                       // 售后单创建时间
                        "refund_tax_amount": 0,                          // 退税费
                        "left_urge_sms_count": 0,                        // 商家剩余发送短信（催用户寄回）次数
                        "return_logistics_code": "",                     // 退货物流单号
                        "risk_decision_code": 0,                         // 风控码
                        "risk_decision_reason": "",                      // 风控理由
                        "risk_decision_description": "",                 // 风控描述
                        "return_promotion_amount": 0,                    // 退优惠金额
                        "refund_status": 3,                              // 退款状态；1-待退款;2-退款中;3-退款成功;4-退款失败;5-追缴成功;
                        "arbitrate_blame": 0,                            // 仲裁责任方
                        "return_logistics_company_name": "",             // 退货物流公司名称
                        "exchange_logistics_company_name": "",           // 换货物流公司名称
                        "remark": "",                                    // 售后商家备注
                        "got_pkg": 0,                                    // 买家是否收到货物，0表示未收到，1表示收到
                        "is_agree_refuse_sign": 0,                       // 是否拒签后退款（1：已同意拒签, 2：未同意拒签）
                        "store_id": 0,                                   // 门店ID
                        "store_name": "",                                // 门店名称
                        "aftersale_sub_type": 0,                         // 售后子类型；8001-以换代修。
                        "auto_audit_bits": [],                           // 自动审核方式：1-发货前极速退；2-小助手自动同意退款；3-发货后极速退；4-闪电退货；5-跨境零秒退；6-云仓拦截自动退；7-小助手自动同意退货；8-小助手自动同意拒签后退款；9-商家代客填写卡片发起售后；10-治理未发货自动同意退款；11-治理已发货自动同意退款；12-商家快递拦截成功自动退款；13-质检商品免审核；14-协商方案自动同意退款；15-平台卡券自动同意退款；16-三方卡券自动同意退款；17-治理一审自动同意退货退款
                        "exchange_sku_info": {                           // 换货SKU信息
                            "sku_id": "",                                // 换货SkuID
                            "code": "",                                  // 换货SKU code               
                            "num": 0,                                    // 换货数目
                            "out_sku_id": "",                            // 商家编号
                            "out_warehouse_id": "",                      // 区域库存仓ID
                            "supplier_id": "",                           // sku外部供应商编码供应商ID
                            "url": "",                                   // 商品图片url
                            "name": "",                                  // 商品名称
                            "price": "",                                 // 换货商品的价格，单位分
                            "spec_desc": ""                              // sku规格信息
                        },
                        "order_logistics": [                             // 商家首次发货的正向物流信息
                            {
                                "tracking_no": "6936476692437472563",    // 物流单号
                                "company_name": "顺丰同城",               // 物流公司名称
                                "company_code": "shenzhenshishun",       // 物流公司编码
                                "logistics_time": 1731916566,            // 物流状态到达时间
                                "logistics_state": 0                     // 正向物流状态
                            }
                        ],
                        "reason_second_labels": []                       // 用户申请售后时选择的二级原因标签
                    },
                    "order_info": {                                      // 订单信息
                        "shop_order_id": "6936476692437472563",          // 店铺单订单ID
                        "order_flag": 0,                                 // 订单插旗
                        "related_order_info": [                          // 售后关联的订单信息
                            {
                                "sku_order_id": "6936476692437472563",   // 商品单信息
                                "order_status": 4,                       // 订单状态，枚举为2(未发货),3(已发货),5(已收货或已完成),255(已完成)
                                "pay_amount": 1,                         // 付款金额
                                "post_amount": 0,                        // 付运费金额
                                "item_num": 1,                           // 购买数量
                                "create_time": 1731916551,               // 下单时间
                                "tax_amount": 0,                         // 税费
                                "is_oversea_order": 0,                   // 是否为海外订单
                                "product_name": "办公椅，测试商品，勿拍",   // 商品名称
                                "product_id": 3660207428038974464,       // 商品ID
                                "product_image": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_0b9d7c9892e9b1c905015b4ef1f32a07_sx_309394_www1500-1500",   // 商品图片
                                "shop_sku_code": "112233",                // 商家SKU编码
                                "logistics_code": "",                     // 商家SKU编码
                                "aftersale_pay_amount": 1,                // 售后退款金额
                                "aftersale_post_amount": 0,               // 售后退运费金额
                                "aftersale_tax_amount": 0,                // 售后退税费金额
                                "aftersale_item_num": 1,                  // 售后商品数量
                                "promotion_pay_amount": 0,                // 优惠券金额
                                "price": 1,                               // 价格
                                "given_sku_order_ids": [],                // 赠品订单id
                                "tags": [
                                    {
                                        "tag_detail": "7天",                         // 标签中文名称
                                        "tag_detail_en": "supply_7day_return",       // 标签编号
                                        "tag_link_url": "https://school.jinritemai.com/doudian/web/article/101835?from=shop_article"   //     // 标签链接
                                    },
                                    {
                                        "tag_detail": "15天售后期",
                                        "tag_detail_en": "after_sale_days",
                                        "tag_link_url": "https://school.jinritemai.com/doudian/web/article/109931"
                                    }
                                ],
                                "sku_spec": [
                                    {
                                        "name": "颜色",
                                        "value": "白色"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ],
            "total": 35,     // 总数
            "page": 1,       // 当前分页
            "size": 1        // 每页数量
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 完成直充订单(发货)

**简要描述：** 根据订单号完成直充订单(发货)，该接口只适用抖店直充业务的订单状态更新，不支持其它类型的订单。

**请求URL：** `/Topup/ManualSend`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tid | 是 | String | 直充订单号 |

**返回示例：**

```json
{
        "isSuccess": true,
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 批量查询商品列表

**简要描述：** 批量查询商品列表

**请求URL：** `/Product/List`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| page | 是 | int | 第几页（第一页为1，最大为100） |
| size | 是 | int | 每页返回条数，最多支持100条 |
| status | 否 | int? | 指定状态返回商品列表：0上架 1下架 |
| checkStatus | 否 | int? | 指定审核状态返回商品列表：1未提审 2审核中 3审核通过 4审核驳回 5封禁 7审核通过，待上架状态 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "data": [
                {
                    "product_id": 3693282087177158656,       // 商品ID
                    "status": 0,                             // 商品上下架状态：0上架 1下架
                    "check_status": 1,                       // 商品审核状态：1未提审 2审核中 3审核通过 4审核驳回 5封禁
                    "market_price": 0,                       // 划线价，单位分
                    "discount_price": 0,                     // 售价，单位分
                    "img": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_bdaff5747ab2c8a3bf81de7e2d9c5d81_sx_270988_www720-720",   // 商品图片url
                    "name": "测试用商家编码勿拍",              // 商品名
                    "pay_type": 1,                           // 支持的支付方式：0货到付款 1在线支付 2两者都支持
                    "product_type": 0,                       // 0-普通，3-虚拟，6玉石闪购，7云闪购
                    "spec_id": 1803361102927964,             // 规格id
                    "cos_ratio": 0,                          // 佣金比例
                    "create_time": 1719819168,               // 商品创建时间
                    "update_time": 1719819169,               // 商品更新时间
                    "out_product_id": 0,                     // 推荐使用，外部商家编码，支持字符串和数字2种
                    "description": "",                       // 商品描述
                    "mobile": "18065583339",                 // 手机号
                    "extra": "{"category_detail":{"enable":null,"first_cid":20048,"first_cname":"餐饮具","fourth_cid":0,"fourth_cname":"","is_leaf":true,"second_cid":20709,"second_cname":"餐具","third_cid":25363,"third_cname":"餐垫/隔热垫"},"is_publish":1,"quality_opId":"7386567066637189416","recruit_info":{"recruit_follow_id":"","recruit_follow_id_list":["27045807"],"recruit_source":"business_center","recruit_type":"3"},"spec_seq_info":{"child_spec_seq":["默认"],"spec_values_seq":[["默认"]]}}",     // 额外信息，如资质
                    "recommend_remark": "",                  // 商家推荐语
                    "category_detail": {
                        "first_cid": 20048,                  // 一级类目
                        "second_cid": 20709,                 // 二级类目
                        "third_cid": 25363,                  // 三级类目
                        "fourth_cid": 0,                     // 四级类目
                        "first_cname": "餐饮具",             // 一级类目名称
                        "second_cname": "餐具",              // 二级类目名称
                        "third_cname": "餐垫/隔热垫",        // 三级类目名称
                        "fourth_cname": ""                   // 四级类目名称
                    },
                    "outer_product_id": "",                  // 推荐使用，外部商家编码，支持字符串和数字2种
                    "is_package_product": false              // 是否是组套商品
                },
                {
                    "product_id": 3660207428038974464,
                    "status": 0,
                    "check_status": 3,
                    "market_price": 1,
                    "discount_price": 1,
                    "img": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_0b9d7c9892e9b1c905015b4ef1f32a07_sx_309394_www1500-1500",
                    "name": "办公椅，测试商品，勿拍",
                    "pay_type": 1,
                    "product_type": 0,
                    "spec_id": 1805244445943844,
                    "cos_ratio": 0,
                    "create_time": 1704416903,
                    "update_time": 1722233275,
                    "out_product_id": 0,
                    "description": "",
                    "mobile": "18065583339",
                    "extra": "{"category_detail":{"first_cid":20036,"first_cname":"商业/办公家具","fourth_cid":0,"fourth_cname":"","is_leaf":true,"second_cid":20658,"second_cname":"办公家具","third_cid":24998,"third_cname":"办公椅"},"is_publish":1,"quality_opId":"7394281245661921575","spec_seq_info":{"child_spec_seq":["颜色"],"spec_values_seq":[["白色","黑色"]]}}",
                    "recommend_remark": "",
                    "category_detail": {
                        "first_cid": 20036,
                        "second_cid": 20658,
                        "third_cid": 24998,
                        "fourth_cid": 0,
                        "first_cname": "商业/办公家具",
                        "second_cname": "办公家具",
                        "third_cname": "办公椅",
                        "fourth_cname": ""
                    },
                    "outer_product_id": "",
                    "is_package_product": false
                }
            ],
            "total": 4,      // 总数
            "page": 1,       // 当前分页
            "size": 2        // 每页数量
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 查询售后单

**简要描述：** 根据售后单Id查询售后单明细

**请求URL：** `/Order/AfterSaleDetail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| afterSaleId | 是 | Long | 售后单Id |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "order_info": {                                 
                "shop_order_id": 6931781998977357824,            // 店铺单ID
                "sku_order_infos": [                             // 售后单关联订单信息
                    {
                        "sku_order_id": 6931781998977357824,     // sku单ID
                        "order_status": 3,                       // 订单状态1 待确认/待支付（订单创建完毕）105 已支付(风控订单不发货) 2 备货中 101 部分发货 3 已发货（全部发货）4 已取消 5 已完成（已收货）
                        "pay_amount": 1,                         // 买家实付金额（分）
                        "post_amount": 0,                        // 买家购买运费（分）
                        "item_quantity": 1,                      // 订单件数
                        "create_time": 1720076744,               // 创建时间
                        "tax_amount": 0,                         // 购买税费（分）
                        "is_oversea_order": 0,                   // 是否为跨境业务
                        "product_name": "办公椅，测试商品，勿拍",  // 商品名称
                        "product_id": 3660207428038974464,       // 商品ID
                        "product_image": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_0b9d7c9892e9b1c905015b4ef1f32a07_sx_309394_www1500-1500",   // 商品图片
                        "sku_spec": [                            // 商品规格信息
                            {
                                "name": "默认", 
                                "value": "默认" 
                            }
                        ],
                        "shop_sku_code": "D007",                 // 商家sku自定义编码
                        "sku_id": 3393133152982786,              // skuID
                        "item_sum_amount": 1,                    // sku商品总原价（不含优惠）
                        "sku_pay_amount": 1,                     // 商品实际支付金额
                        "promotion_amount": 0,                   // 优惠总金额
                        "pay_type": 4,                           // 支付方式：0 : "货到付款" 1："在线支付"
                        "after_sale_item_count": 1,              // 商品单对应的售后数量
                        "given_sku_details": [
                            {
                            "name": "默认", 
                            "value": "默认" 
                        }]                                       // 赠品信息
                    }
                ]
            },                                              
            "process_info": {
                "after_sale_info": {
                    "after_sale_id": 146501574716378560,          // 售后单ID
                    "after_sale_status": 7,                       // 售后状态：6-售后申请；7-售后退货中；8-【补寄维修返回：售后待商家发货】；11-售后已发货；12-售后成功；13-【换货补寄维修返回：售后商家已发货，待用户收货】； 14-【换货补寄维修返回：售后用户已收货】 ；27-拒绝售后申请；28-售后失败；29-售后退货拒绝；51-订单取消成功；53-逆向交易已完成；
                    "after_sale_status_desc": "待买家退货",        // 售后状态文案
                    "refund_type": 4,                             // 退款方式
                    "refund_type_text": "订单货款",                // 退款方式文案
                    "refund_status": 1,                           // 退款状态;1-待退款;2-退款中;3-退款成功;4退款失败;5追缴成功;
                    "reason": "其他",                              // 申请原因
                    "reason_code": 15,                            // 原因码；通过【afterSale/rejectReasonCodeList】接口获取
                    "apply_time": 1723686010,                     // 售后单申请时间
                    "after_sale_type": 0,                         // 售后类型： 0-售后退货退款；1-售后仅退款；2-发货前退款；3-换货；4-系统取消；5-用户取消；6-价保；7-补寄；8-维修
                    "apply_role": 1,                              // 售后申请角色：1-买家；2-商家；3-客服；4-系统
                    "post_receiver":"xxxxxxxx",                   // 换货、补寄时的收货人名字（只有换货、补寄时，这个字段才会有值），此字段已加密，使用前需要解密
                    "post_tel_sec":"xxxxxxxx",                    // 换货、补寄时的收货人的联系电话（只有换货、补寄时，这个字段才会有值），此字段已加密，使用前需要解密
                    "post_address":{                              // 换货、补寄时的收货四级地址（只有换货、补寄时，这个字段才会有值）
                        "detail":"xxxxxxx"                        // 地址详情，此字段已加密，使用前需要解密
                        "landmark":"xxx"                          // 收件地址标志物
                        "province":{
                            "id":"",
                            "name":"省",
                        },
                        "city":{
                            "id":"",
                            "name":"市",
                        },
                        "town":{
                            "id":"",
                            "name":"县",
                        },
                        "street":{
                            "id":"",
                            "name":"街道",
                        },
                    }
                },
                "logistics_info": {                               // 物流信息
                    "return": {                                   // 买家退货物流信息
                        "tracking_no": "",                        // 物流单号
                        "company_name": "",                       // 物流公司名称
                        "company_code": "",                       // 物流公司编码
                        "logistics_time": "0"                     // 买家填写退货物流时间
                    }
                }
            }
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 查询商品信息

**简要描述：** 根据商品Id查询商品明细

**请求URL：** `/Product/Detail`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| productId | 是 | String | 商品Id |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
                "product_id": 3660207428038974464,               // 商品ID，整型格式
                "product_id_str": "3660207428038974332",         // 商品ID，字符串格式
                "out_product_id": 0,                             // 商品外部ID
                "outer_product_id": "",                          // 商品外部ID
                "name": "办公椅，测试商品，勿拍",                  // 商品名称
                "description": "",
                "market_price": 1,                               // 划线价，单位分
                "discount_price": 1,                             // 售价，单位分
                "status": 0,                                     // 商品上下架状态：0上架 1下架 2已删除
                "spec_id": 1787210656101395,                     // 规格id
                "check_status": 3,                               // 商品审核状态：1未提审 2审核中 3审核通过 4审核驳回 5封禁 7审核通过，待上架状态
                "mobile": "18065583339",                         // 手机号
                "first_cid": 0,                                  // 一级类目
                "second_cid": 0,                                 // 二级类目
                "third_cid": 0,                                  // 三级类目
                "pay_type": 1,                                   // 支持的支付方式：0货到付款 1在线支付 2两者都支持
                "recommend_remark": "",                          // 商家推荐语
                "presell_type": "0",                             // 预售类型，1-全款预售，0-非预售，2-阶梯库存
                "extra": "{"category_detail":{"enable":null,"first_cid":20036,"first_cname":"商业/办公家具","fourth_cid":0,"fourth_cname":"","is_leaf":true,"second_cid":20658,"second_cname":"办公家具","third_cid":24998,"third_cname":"办公椅"},"is_publish":1,"quality_opId":"7386565254094487843","spec_seq_info":{"child_spec_seq":["默认"],"spec_values_seq":[["默认"]]}}",  // 扩展字段
                "create_time": "2024-01-05 09:08:23",            // 创建时间
                "update_time": "2024-07-04T17:23:22+08:00",      // 更新时间
                "pic": [                                         // 商品主图
                    "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_0b9d7c9892e9b1c905015b4ef1f32a07_sx_309394_www1500-1500",
                    "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_9ae21a465dc6a727b4960abd1b82f59c_sx_109842_www747-747",
                    "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_730ad1990a9e416263a1e9d5f37c99d4_sx_101200_www800-800"
                ],
                "product_format": "",                            // 属性名称|属性值之间用|分隔, 多组之间用^分开
                "spec_pics": [],                                 // 规格图片
                "spec_prices": [    
                    {
                        "sku_id": 3393133152982786,              // 规格id；
                        "out_sku_id": 0,                         // 外部商家skui_id编码，商家自定义字段；推荐使用outer_sku_id字段
                        "outer_sku_id": "",                      // 外部商家skui_id编码   
                        "spec_detail_ids": [    
                            1787210656101427    
                        ],  
                        "stock_num": 1,                          // 可售库存；当前现货可售库存；
                        "price": 1,                              // 商品价格；单位：分
                        "code": "D007",                          // 商编码
                        "settlement_price": 0,      
                        "step_stock_num": 0,                     // 阶梯库存，规则详见名称解释：https://op.jinritemai.com/docs/guide-docs/202/170
                        "prom_stock_num": 0,                     // 活动库存，，规则详见名称解释：https://op.jinritemai.com/docs/guide-docs/202/170
                        "prom_step_stock_num": 0,                // 活动阶梯库存，，规则详见名称解释：https://op.jinritemai.com/docs/guide-docs/202/170
                        "spec_detail_id1": 1787210656101427,        
                        "spec_detail_id2": 0,       
                        "spec_detail_id3": 0,       
                        "sku_type": 0,                           // sku类型；0-普通库存 1-区域库存 10-阶梯库存
                        "supplier_id": "",                       // 供应商编码
                        "customs_report_info": {
                            "hs_code": "",      
                            "first_measure_qty": 0,    
                            "second_measure_qty": 0,   
                            "first_measure_unit": "",      
                            "second_measure_unit": "",     
                            "unit": "",     
                            "report_name": "", 
                            "report_brand_name": "",
                            "usage": "",       
                            "g_model": "",     
                            "bar_code": ""     
                        },  
                        "lock_stock_num": 0,                      // 商品ID，整型格式
                        "lock_step_stock_num": 0,                 // 商品ID，整型格式
                        "sell_properties": [                      // sku对应的销售属性信息
                            {
                              "perperty_id": "0",                            // 销售属性id，只有在规格由属性库下发时，这个字段才有值。 默认为0
                              "property_name": "颜色",                       // 规格项名称
                              "remark": "非常黄",                            // 备注
                              "value_id": "12345678910",                     // 销售属性值id，只有在规格由属性库下发时，这个才有值。 默认为0
                              "value_name": "黄色",                          // 规格值名称
                              "value_spec_detail_id": "123123123123"         // 规格值id
                            }
                          ],
                    }
                ],
                "img": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_0b9d7c9892e9b1c905015b4ef1f32a07_sx_309394_www1500-1500",     // 头图，主图第一张
                "category_detail": {                              // 新类目的详情
                    "first_cid": 20036,                           // 一级类目
                    "second_cid": 20658,                          // 二级类目
                    "third_cid": 24998,                           // 三级类目
                    "fourth_cid": 0,                              // 四级类目
                    "first_cname": "商业/办公家具",                // 一级类目名称
                    "second_cname": "办公家具",                    // 二级类目名称
                    "third_cname": "办公椅",                       // 三级类目名称
                    "fourth_cname": ""                            // 四级类目名称
                },
                "maximum_per_order": 0,                            // comment
                "limit_per_buyer": 0,                              // comment
                "minimum_per_order": 1,                            // comment
                "draft_status": 3,                                 // 草稿状态：0 无草稿,1 未提审,2 待审核,3 审核通过,4 审核未通过
                "is_sub_product": false,                           // 是否是组套商品的子商品
                "pickup_method": "0"                               // 提取方式新字段，推荐使用。"0": 普通商品-使用物流发货, "1": 虚拟商品-无需物流与电子交易凭证, "2": 虚拟商品-使用电子交易凭证, "3": 虚拟商品-充值直连
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 查询订单列表

**简要描述：** 查询订单列表

**请求URL：** `/Order/List`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| page | 是 | int | 页码,第几页(从0开始) |
| size | 是 | int | 每页的数量,最多支持100条 |
| startTime | 是 | DateTime | 下单的开始时间 (2024-10-10 或 2024-10-10 00:00:00) |
| endTime | 否 | DateTime | 下单的结束时间 (2024-10-20 或 2024-10-20 23:59:59) |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "page": 1,
            "shop_order_list": [
                {
                    "shop_id": 7784061,                          // 店铺ID
                    "shop_name": "京艺智造",                      // 商户名称
                    "open_id": "",                               // 抖音小程序ID
                    "buyer_words": "",                           // 买家留言
                    "seller_words": "付款后发货失败：调用第三方接口成功，但对方返回失败（）\r
",    // 商家备注
                    "logistics_info": [                              // 物流信息
                        {
                            "tracking_no": "6936476692437472563",    // 物流单号
                            "company": "shenzhenshishun",            // 物流公司
                            "ship_time": 1731916566,                 // 发货时间
                            "delivery_id": "7438525010135810342",    // 包裹id
                            "company_name": "顺丰同城",               // 物流公司名称
                            "product_info": [
                                {
                                    "product_name": "办公椅，测试商品，勿拍",    // 商品名称
                                    "price": 1,                                // 商品价格
                                    "outer_sku_id": "",                        // 商家编码
                                    "sku_id": 3410716076201730,                // 商品skuId
                                    "sku_specs": [
                                        {
                                            "name": "颜色",
                                            "value": "白色"
                                        }
                                    ],
                                    "product_count": 1,                          // 发货商品数量
                                    "product_id": 3660207428038974464,           // 商品ID
                                    "sku_order_id": "6936476692437472563"        // 商品单ID
                                }
                            ]
                        }
                    ],
                    "sku_order_list": [                                  // 商品单信息
                        {
                            "parent_order_id": "6936476692437472563",    // 父订单号（店铺订单号）
                            "send_pay": 0,                               // 流量来源：1-鲁班广告 2-联盟 3-商城 4-自主经营 5-线索通支付表单 6-抖音门店 7-抖+ 8-穿山甲
                            "send_pay_desc": "-",                        // 流量来源描述
                            "author_id": 0,                              // 直播主播id（达人）
                            "author_name": "",                           // 直播主播名称
                            "theme_type": "0",                           // 【下单来源】 0、其他 1、直播间
                            "theme_type_desc": "-",                      // 下单来源描述
                            "room_id": 0,                                // 直播间id
                            "content_id": "0",                           // 内容id
                            "video_id": "",                              // 视频id
                            "origin_id": "0_3660207428038974332",        // 流量来源id
                            "cid": 0,                                    // 广告id
                            "c_biz": 8,                                  // 【C端流量来源】 0、unknown 1、鲁班广告 2、联盟 4、商城 8、自主经营 10、线索/表单收集类广告 12、抖音门店 14、抖+ 15、穿山甲 16、服务市场 18、服务市场外包客服 19、学浪
                            "c_biz_desc": "小店自卖",                     // C端流量来源业务类型描述
                            "page_id": 0,                                // 鲁班广告落地页ID
                            "code": "112233",                            // 商家后台商品编码
                            "logistics_receipt_time": 0,                 // 物流收货时间
                            "confirm_receipt_time": 0,                   // 用户确认收货时间
                            "goods_type": 0,                             // 【商品类型】 0、实体 1、虚拟
                            "sku_id": 3410716076201730,                  //  商品skuId
                            "spec": [                                    //  规格信息
                                {
                                    "name": "颜色",
                                    "value": "白色"
                                }
                            ],
                            "first_cid": 20036,                          //  一级类目
                            "second_cid": 20658,                         //  二级类目
                            "third_cid": 24998,                          //  三级类目
                            "fourth_cid": 0,                             //  四级类目
                            "out_sku_id": "",                            //  外部SkuId
                            "supplier_id": "",                           //  sku外部供应商编码
                            "out_product_id": "0",                       //  商品外部编码
                            "reduce_stock_type": 1,                      //  【库存扣减方式】 1、下单减库存 2、支付减库存
                            "reduce_stock_type_desc": "下单减库存",       //  库存扣减方式名称
                            "origin_amount": 1,                          //  商品现价
                            "has_tax": false,                            //  是否包税
                            "item_num": 1,                               //  订单商品数量
                            "sum_amount": 1,                             //  商品现价*件数
                            "source_platform": "",                       //  商品来源平台
                            "sku_order_tag_ui": [                        //  商品单标签
                                {},
                                {},
                                {},
                                {},
                                {},
                                {},
                                {}
                            ],
                            "product_pic": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/SXJcUUhG_m_0b9d7c9892e9b1c905015b4ef1f32a07_sx_309394_www1500-1500",  //  商品图片
                            "is_comment": 0,                             //  是否评价 :1已评价，0未评价，2 表示追评
                            "product_name": "办公椅，测试商品，勿拍",      //  商品名称
                            "inventory_list": [                          //  仓库信息
                                {}
                            ],
                            "pre_sale_type": 0,                          //  预售类型 ，0 现货类型，1 全款预售 2 阶梯发货
                            "after_sale_info": {                         //  售后信息
                                "after_sale_status": 12,                 //  售后状态，0-售后初始化，27-拒绝售后申请，28-售后失败，11-售后已发货，29-退货后拒绝退款，51-取消成功,这几个状态视为退款中:6-售后申请， 7-售后退货中，12-售后成功，13-售后换货商家发货，14-售后换货用户收货，53-逆向交易完成
                                "after_sale_type": 1,                    //  售后类型:0 售后退货退款:1-售后退款 2-售前退款 3-换货 4-系统取消 5-用户取消
                                "refund_status": 3                       //  退款状态:0-无需退款 1-待退款 2-退款中 3-退款成功 4-退款失败
                            },
                            "receive_type": 0,                           //  1:邮寄，2:自提
                            "given_product_type": "",                    //  绑定类型 MASTER-主品单 FREE-免费赠品
                            "order_id": "6936476692437472563",           //  商品订单号
                            "order_level": 3,                            //  订单层级
                            "biz": 2,                                    //  业务来源
                            "biz_desc": "小店",                          //  业务来源
                            "order_type": 0,                             //  【订单类型】 0、普通订单 1、全款预售订单 2、虚拟商品订单 3、快闪店订单 4、电子券（poi核销） 5、三方核销 6、服务市场
                            "order_type_desc": "普通订单",               //  订单类型描述
                            "trade_type": 0,                             //  【交易类型】 0、普通 1、拼团 2、定金预售 3、订金找贷 4、拍卖 5、0元单 6、回收 7、寄卖
                            "trade_type_desc": "普通",                   //  交易类型描述
                            "order_status": 4,                           //  订单状态1 待确认/待支付（订单创建完毕）105 已支付(风控订单不发货) 2 备货中 101 部分发货 3 已发货（全部发货）4 已取消 5 已完成（已收货）
                            "order_status_desc": "已关闭",               //  订单状态描述
                            "main_status": 22,                           //  主流程状态，1 待确认/待支付（订单创建完毕）103 部分支付105 已支付2 备货中101 部分发货3 已发货（全部发货）4 已取消5 已完成（已收货）21 发货前退款完结22 发货后退款完结39 收货后退款完结
                            "main_status_desc": "发货后退款完成",         //  主流程状态描述
                            "pay_time": 1731916560,                      //  支付时间，时间戳，秒
                            "order_expire_time": 1800,                   //  订单过期时间，时间戳，秒
                            "finish_time": 0,                            //  订单完成时间，时间戳，秒
                            "create_time": 1731916551,                   //  下单时间，时间戳，秒
                            "update_time": 1731986645,                   //  订单更新时间，时间戳，秒
                            "cancel_reason": "",                         //  取消原因
                            "b_type": 2,                                 //  【下单端】 0、站外 1、火山 2、抖音 3、头条 4、西瓜 5、微信 6、值点app 7、头条lite 8、懂车帝 9、皮皮虾 11、抖音极速版 12、TikTok 13、musically 14、穿山甲,15、火山极速版 16、服务市场 26、番茄小说 27、UG教育营销电商平台 28、Jumanji 29、电商SDK
                            "b_type_desc": "抖音",                       //  下单端描述
                            "sub_b_type": 3,                             //  【下单场景】 0、未知 1、app内-原生 2、app内-小程序 3、H5 13、电商SDK-头条 35、电商SDK-头条lite
                            "sub_b_type_desc": "H5",                     //  下单场景描述
                            "app_id": 1128,                              //  具体某个小程序的ID
                            "pay_type": 2,                               //  【支付类型】 0、货到付款 1 、微信 2、支付宝 3、小程序 4、银行卡 5、余额 7、无需支付（0元单） 8、DOU分期（信用支付） 9、新卡支付
                            "channel_payment_no": "2024111822001496911406999482",    //  支付渠道的流水号
                            "order_amount": 1,                           //  订单金额（分）
                            "pay_amount": 1,                             //  支付金额（分）
                            "post_insurance_amount": 0,                  //  运费险金额（分）
                            "modify_amount": 0,                          //  改价金额变化量（分）
                            "modify_post_amount": 0,                     //  改价运费金额变化量（分）
                            "promotion_amount": 0,                       //  单优惠总金额= 店铺优惠金额+ 平台优惠金额+ 达人优惠金额
                            "promotion_shop_amount": 0,                  //  店铺优惠金额（分）
                            "promotion_platform_amount": 0,              //  平台优惠金额（分）
                            "shop_cost_amount": 0,                       //  订单优惠商家承担部分（分）
                            "platform_cost_amount": 0,                   //  订单优惠平台承担部分（分）
                            "promotion_talent_amount": 0,                //  达人优惠金额（分）
                            "promotion_pay_amount": 0,                   //  支付优惠金额（分）
                            "encrypt_post_tel": "$$KlqdO3S6/9vQsJesewp8R2oBlX+I2/UABgHSm9Oy1SuYX6R0pLupUedZkqXVIisqK2anlk+ttMeuBbLI7M286cNfqghVjTy7u2079Lv+6two*CgYIASAHKAESPgo85MWGCFPBcT7U9hVhlqarT/gCf5lFGgE2/QD7kk8RnNtk6ejVOgEhHmWsdLcZVL+ZUhMHYZCE9RmWMuAuGgA=$1$$",   //  收件人电话
                            "encrypt_post_receiver": "##qIOpbLPevlQwA6f+yNJ7HgOqMdCcDttVlAympUYfJk9VrcWMMeMb1JAmpuUKKFpR+5cGN0aBvV4izFUdinLYs+y2h6RBhv3iZShTKqqttg==*CgYIASAHKAESPgo8AezTm/PH44dQuZGevG6eHhvqqq4gTxNsNWaJyhU33eidXUZe8itcPwhIgUU1vWsqpGKbwUJrTtvnXCDyGgA=#1##",  //  收件人姓名
                            "post_addr": {
                                "province": {
                                    "name": "福建省",
                                    "id": "35"
                                },
                                "city": {
                                    "name": "厦门市",
                                    "id": "350200"
                                },
                                "town": {
                                    "name": "思明区",
                                    "id": "350203"
                                },
                                "street": {
                                    "name": "莲前街道",
                                    "id": "350203010"
                                },
                                "encrypt_detail": "##i688Hg7Kf5y7JCzTAYaUWxswmAx8QnTPvGdsCInjgOIZZNGsRNBWUEgKAdgBnlq2QPdz9SEuu1Hx4zdgUDzORVOS3RVAymnPMfuETWjh1rsELUlyvpciCGRh75TrxtdIkm4yr0exFC41EQuw5Sbn*CgYIASAHKAESPgo8VOu2w0Yb+AwqaIo/dDaYUd0Rf7TF/vhnHHKSjNWvj0Wy7ufZtxugca+cTAvyZ9jvnwdRpAZDPK+WwyWxGgA=#1##"  //  详细地址
                            },
                            "exp_ship_time": 1732031999,         //  预计发货时间，时间戳，秒
                            "ship_time": 1731916566,             //  发货时间，时间戳，秒
                            "product_id": 3660207428038974464,   //  商品ID
                            "promotion_detail": {},              //  优惠信息
                            "post_amount": 0,                    //  快递费（分）
                            "promotion_redpack_amount": 0,       //  红包优惠金额（分）
                            "promotion_redpack_platform_amount": 0,  //  平台红包优惠金额（分）
                            "promotion_redpack_talent_amount": 0     //  达人红包优惠金额（分）
                        }
                    ],
                    "seller_remark_stars": 0,                    //  插旗信息：0：灰 1：紫 2: 青 3：绿 4： 橙 5： 红
                    "order_phase_list": [],                      //  定金预售阶段单
                    "doudian_open_id": "1@#VrtJKX59ewuPyvUhIKiAtxNZ0wt2BBDARCd6qdLmaBiz59YmNzPgpz+KC0B+R/RJTQJ3GRv5",    // 加密用户ID串
                    "serial_number_list": [],                    //  商品序列号，15-17位数字
                    "isDdpSource": false,                        //  数据来源（true：数据库、false：api接口）

                     //  以下参数与sku_order_list里的同名属性描述一致
                    "order_id": "6936476692437472563",      
                    "order_level": 2,                       
                    "biz": 2,                               
                    "biz_desc": "小店",                     
                    "order_type": 0,                        
                    "order_type_desc": "普通订单",          
                    "trade_type": 0,                        
                    "trade_type_desc": "普通",              
                    "order_status": 4,                      
                    "order_status_desc": "已关闭",          
                    "main_status": 22,                      
                    "main_status_desc": "发货后退款完成",   
                    "pay_time": 1731916560,                 
                    "order_expire_time": 1800,                  
                    "finish_time": 0,
                    "create_time": 1731916551,
                    "update_time": 1731986645,
                    "cancel_reason": "",
                    "b_type": 2,
                    "b_type_desc": "抖音",
                    "sub_b_type": 3,
                    "sub_b_type_desc": "H5",
                    "app_id": 1128,
                    "pay_type": 2,
                    "channel_payment_no": "2024111822001496911406999482",
                    "order_amount": 1,
                    "pay_amount": 1,
                    "post_insurance_amount": 0,
                    "modify_amount": 0,
                    "modify_post_amount": 0,
                    "promotion_amount": 0,
                    "promotion_shop_amount": 0,
                    "promotion_platform_amount": 0,
                    "shop_cost_amount": 0,
                    "platform_cost_amount": 0,
                    "promotion_talent_amount": 0,
                    "promotion_pay_amount": 0,
                    "encrypt_post_tel": "$$U/qaYiUFjC/1SRShyJN85xYJnWFzy6DTqG/V0m1+UJElKaiasCPEHg1DapycCfIC4JlZoiDjoLcpLZPYMEmuXavArlKWr/U7WIK96FcW3lwm*CgYIASAHKAESPgo8K/kgWUneg1yJPt5GQUiGszzh1HxSnId/jeJpDIAXlRr1AI2Jzh4ga6Ykk0skQQJDOU7MuFaMrMcSdkcYGgA=$1$$",
                    "open_address_id": "#GKTB7s7wOxP/iHoVtQM9LrM0EXj6pJo6xT/cJJ9rjxCl2AYG6dA4c2YIICDozxGcYz9oftzUWK2dx35VWLdWEmFL/q/BVDo0/GHNVYy0ptWC40lWrefDIeXPQelrdzTMg0MtWbygqA==",
                    "encrypt_post_receiver": "##5e4wPfKQCWbYKOTVtch6HxHddNxyvAI7PQXlv354unHilRmbS0TzvT0Pt9aASrVfeLqmpOdCKB94shj+kDE38A89MPVYuJtdF4U9xkbxjQ==*CgYIASAHKAESPgo8A0knInJ6X2/YJbHNB0mu93T5+2Bif3K2F6jMJG14HKgoWWYrnxLiNG0gFLvZMQUQupspgzll7tlHlOtCGgA=#1##",
                    "post_addr": {
                        "province": {
                            "name": "福建省",
                            "id": "35"
                        },
                        "city": {
                            "name": "厦门市",
                            "id": "350200"
                        },
                        "town": {
                            "name": "思明区",
                            "id": "350203"
                        },
                        "street": {
                            "name": "莲前街道",
                            "id": "350203010"
                        },
                        "encrypt_detail": "##9c125pyLUXJAYmZnUhS+4KdQwNGbBXvrJ6w7Lh1v3rBqtATddX+VzI0Pb4cbFdCgSxzjPQ8YPi5ULeEpotLHrtq4dTHkzNZIyZfA8MrYZtpgzOw823/JW5DNOZpV3RtpKca8TL7mF4lwvWs6vioV*CgYIASAHKAESPgo8Cghl0OymTqTQy6+bT3R1dnWOOp0zqpfpBHctTBUI3YCddjXvS3tPDuIfaHJBuINxH0EsJyKlytxP+5y7GgA=#1##"
                    },
                    "exp_ship_time": 1732031999,
                    "ship_time": 1731916566,
                    "product_id": 0,
                    "promotion_detail": {},
                    "post_amount": 0,
                    "promotion_redpack_amount": 0,
                    "promotion_redpack_platform_amount": 0,
                    "promotion_redpack_talent_amount": 0
                }
            ],
            "size": 1,
            "total": 33
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 申请短信模板

**简要描述：** 申请短信模板

**请求URL：** `/Sms/ApplyTemplate`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| name | 是 | String | 短信模板名称 |
| content | 是 | String | 短信模板内容 示例：订单号：${orderId} 买家：${userId} 识别码:${code} 注意： 英文短信：整条短信（包括签名+模板+变量中的内容）最多支持140个英文字符，超出将按140个字符截取为多条短信进行发送，费用按截取的条数收费； 非英文短信：整条短信（包括签名+模板+变量中的内容）最多支持70字符，超出将按70个字符截取为多条短信进行发送，费用按截取的条数收费 |
| smsAccountType | 否 | Int | 所属关联通道: 0普通短信(默认) 1教育类短信 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "platform_shop_id": "7784061",            // 平台门店ID
            "name": "测试短信模板",                    // 模板名称
            "tpl_type": 4,                            // 模板类型
            "tpl_id": "ST_7e0c58aax",                 // 模板Id:对应发送短信接口的参数 templateId
            "tpl_content": "订单号：${orderId} 买家：${user} 识别码:${code}",             // 模板内容
            "platform_tpl_content": "订单号：${orderId} 买家：${user} 识别码:${code}",    // 模板内容 示例：您购买的商品已重新发出，${name}快递运单号：${number}，关注“XXX”公众号刷新订单获取最新物流信息哦~给您造成不便敬请谅解。
            "audit_status": 100,     // 审核状态 =>100 :待审核 200：通过 300：拒绝
            "ext_info": "{"SmsTemplateApplyId":"672448","AuditDefaultUse":false}",  // 扩展信息，SmsTemplateApplyId：模板申请Id
            "modify_time": "2024-07-10 15:48:37",
            "create_time": "2024-07-10 15:48:37"
        },
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 短信结果查询

**简要描述：** 短信结果查询

**请求URL：** `/Sms/SmsResult`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| messageId | 是 | string | 消息Id(对应发送短信接口返回的message_id) |
| smsAccountType | 否 | Int | 所属关联通道: 0普通短信(默认) 1教育类短信 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": {
            "status_code": "0",                       // 状态码,"0"代表成功
            "description": "发送成功",                // 状态描述
            "signature": "阿奇索",                   // 短信签名
            "template_id": "ST_82aba028",             // 模板ID
            "channel_type": "CN_NTC",                 // 短信类型
            "message_id": "226758fc-13e8-4971-a168-98b6beb15447",     // 发送时返回的MessageID
            "msg_count": 2,                           // 计费条数
        },
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
| tid | 是 | String | 店铺订单号 |
| aldsType | 是 | Int | 自动发货类型，具体查看底部备注 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
          {
            "title": "唯一卡别名",
            "oid": "123456789",
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
            "oid": "223456789",
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
| oid | Array | 子订单编号 |
| cardPwdArr | Array | 卡密数组 |
| c | String | 卡号 |
| p | String | 卡券 |

**备注：** aldsType自动发货类型：付款后发货=1，确认收货后赠送=2

---

## 获取短信发货结果

**简要描述：** 获取短信的发货结果

**请求URL：** `/Sms/SendResult`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| fromTime | 是 | dateTime | 开始时间(若超时,请缩小时间范围) |
| toTime | 是 | dateTime | 结束时间(若超时,请缩小时间范围) |
| templateId | 否 | string | 短信模板Id |
| status | 否 | int | 发送状态： 未回执：1 发送失败：2 发送成功：3, 默认是0:查询所有 |
| page | 否 | int | 查询结果页数，从0开始，默认是0 |
| size | 否 | int | 查询结果大小，默认是10 |
| messageId | 否 | string | 消息Id(对应发送短信接口返回的message_id) |
| smsAccountType | 否 | Int | 所属关联通道: 0普通短信(默认) 1教育类短信 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
            "sms_send_result_list": [
                {
                  "code": "0",                       // 错误码
                  "count": "1",                      // 计费条数，如果短信过长，会分多次计费
                  "message": "abc",                  // 错误说明
                  "message_id": "MessageID1",        // 消息ID
                  "send_time": "1618652575",         // 发送时间-时间戳，单位秒
                  "sms_content": "测试的短信内容",    // 短信内容
                  "status": "1",                     // 未回执：1 发送失败：2 发送成功：3
                  "tag": "12345"                     // 透传字段，回执的时候原样返回给调用方。
                }
              ],
              "total": "100"                 // 总数量
        ],
        "error_Code": 0,
        "error_Msg": ""
    }
```

---

## 获取短信模板

**简要描述：** 获取短信模板

**请求URL：** `/Sms/GetSmsTemplates`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| tplIds | 否 | List<string> | 短信模板Id列表，不传默认查询所有  注意：对于列表类型传多个值的情况，可以添加多个相同键(tplIds),不同值来传递。          多个模板Id请求示例：         param1:tplIds = xxxxx1         param2:tplIds = xxxxx2 |

**返回示例：**

```json
{
        "isSuccess": true,
        "data": [
            {
            "platform_shop_id": "7784061",            // 平台门店ID
            "tpl_type": 4,                            // 模板类型：0 发提取网站,1 发卡号, 2 发卡号和密码,3 发货声明,4 开放平台
            "name": "测试短信模板",                    // 模板名称
            "tpl_id": "ST_7e0c58aax",                 // 模板Id:对应发送短信接口的参数 templateId
            "tpl_content": "订单号：${orderId} 买家：${user} 识别码:${code}",             // 模板内容
            "platform_tpl_content": "订单号：${orderId} 买家：${user} 识别码:${code}",    // 模板内容 可忽略该字段
            "audit_status": 100,                                                           // 审核状态 =>100 :待审核 200：通过 300：拒绝
            "ext_info": "{"SmsTemplateApplyId":"672448","AuditDefaultUse":false}",   // 扩展信息，SmsTemplateApplyId：模板申请Id
            "modify_time": "2024-07-10 15:48:37",
            "create_time": "2024-07-10 15:48:37"
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
| shop_order_id | 是 | String | 店铺订单号 |

**返回示例：**

```json
{
          "IsSuccess": true,
          "Data": {
            "order_id":"4907538423936588900",      // 店铺订单号（父订单号）
            "order_level":2,                       // 订单层级，主订单是2级
            "order_type":0,                        // 【订单类型】 0、普通订单 2、虚拟商品订单 4、电子券（poi核销） 5、三方核销
            "order_type_desc":"普通订单",          // 订单类型描述
            "order_status":4,                      // 订单状态1 待确认/待支付（订单创建完毕）105 已支付 2 备货中 101 部分发货 3 已发货（全部发货）4 已取消5 已完成（已收货）
            "order_status_desc":"已关闭",          // 订单状态描述
            "main_status":21,                      // 主流程状态，1 待确认/待支付（订单创建完毕）103 部分支付105 已支付2 备货中101 部分发货3 已发货（全部发货）4 已取消5 已完成（已收货）21 发货前退款完结22 发货后退款完结39 收货后退款完结
            "main_status_desc":"发货前退款完成",    // 主流程状态描述
            "pay_time":1646720740,                //  支付时间，时间戳，秒述
            "order_expire_time":1800,              // 订单过期时间，时间戳，秒
            "finish_time":0,                      // 订单完成时间，时间戳，秒
            "create_time":1646720547,             // 下单时间，时间戳，秒
            "update_time":1646892779,             // 订单更新时间，时间戳，秒
            "cancel_reason":"",                   // 取消原因
            "order_amount":1,                     // 订单金额（单位：分）
            "pay_amount":1,                       // 支付金额（单位：分）
            "ship_time":0,                        // 发货时间，时间戳，秒
            "shop_id":7784061,                    // 店铺ID
            "shop_name":"茶具礼品",               // 商户名称
            "doudian_open_id":"aaxxxxssss",      // 加密用户ID串
            "buyer_words":"",                    // 买家留言
            "seller_words":"",                   // 商家备注
            "sku_order_list":[                   // 商品单信息
              {
                  "order_id":"6931411066952816166",          // 子订单
                  "order_status":"2",                        订单状态1 待确认/待支付（订单创建完毕）105 已支付(风控订单不发货) 2 备货中 101 部分发货 3 已发货（全部发货）4 已取消 5 已完成（已收货）
                  "pay_amount":1,                            // 支付金额（分）
                  "parent_order_id":"4907538423936588900",   // 父订单号（店铺订单号）
                  "code":"333",                              // 商家后台商品编码
                  "logistics_receipt_time":0,                // 物流收货时间
                  "confirm_receipt_time":0,                  // 用户确认收货时间
                  "goods_type":0,                            // 【商品类型】 0、实体 1、虚拟
                  "product_id":1721288561899563,             // 商品id
                  "sku_id":1721288561899566,                 // 商品skuId
                  "spec":[                                   // 规格信息
                      {
                          "name":"包装",
                          "value":"定制（单拍不发）"
                      }
                  ],
                  "out_sku_id":"",                           // 外部Skuid
                  "supplier_id":"",                          // sku外部供应商编码
                  "out_product_id":"0",                      // 商品外部编码
                  "origin_amount":1,                         // 商品现价（单位：分）
                  "item_num":1,                              // 订单商品数量
                  "sum_amount":1,                            // 商品现价*件数
                  "sku_order_tag_ui":[{}],                     // 商品单标签
                  "product_pic":"https://p9-aio.ecombdimg.com/obj/temai/d42f1583f37761dc27758607abb9f8f6www935-935", // 商品现价*件数
                  "is_comment":0,                              // 是否评价 :1已评价，0未评价，2 表示追评
                  "product_name":"一次性保鲜膜套家用防尘保鲜罩一次性保鲜套",   // 商品名称
                  "after_sale_info":{                          // 售后信息
                      "after_sale_status":12,                  // 售后状态，0-售后初始化， 6-售后申请， 7-售后退货中， 27-拒绝售后申请， 12-售后成功， 28-售后失败， 11-售后已发货， 29-退货后拒绝退款， 13-售后换货商家发货， 14-售后换货用户收货， 51-取消成功， 53-逆向交易完成
                      "after_sale_type":2,                     // 售后类型:0 售后退货退款:1-售后退款 2-售前退款 3-换货 4-系统取消 5-用户取消    
                      "refund_status":3                        // 退款状态:0-无需退款 1-待退款 2-退款中 3-退款成功 4-退款失败 
                  },
                  "relation_order":{                           // 关联订单 
                    "write_off_no":"",                         // 核销券码 
                    "relation_order_id":""                     // 关联店铺单订单id 
                  },
                  "given_product_type":""                      // 绑定类型 MASTER-主品单 FREE-免费赠品 
                  "pre_sale_type": 0                           // 预售类型 ，0 现货类型，1 全款预售 2 阶梯发货 
                  "exp_ship_time": 1732118399,                 // 预计发货时间，时间戳，秒
                  "author_id": 0,                              // 直播主播id（达人）
                  "author_name": "",                           // 直播主播名称 
                  "room_id": 0,                                // 直播间id
              }
            ],
            "exp_ship_time": 1732118399,                       // 预计发货时间，时间戳，秒 
            "encrypt_post_tel": "$$xP8HUyAQGaXOEO4tHAv2ZoeEQxAn4wWXun7FRA7T5MYnDnjEUxEUqb3eh2Aek2WjEPjE8GO1ad+LiLkPI+TODD56u6+UpIJ71K4t1iXfVJB1*CgYIASAHKAESPgo8vnQ9ylXbuqO4LV7chHWhFqnePSSbBGDC0bL9YieT6xX5sf13zEgR8rDafzkWWFYlyjqJPDbc7vJmybF3GgA=$1$$",                             // 收件人电话(密文) 
            "encrypt_post_receiver": "##RA8Drz4ZwOh3iv9o3QRM6TRTP4BvjMMLyoptIU/y6X4JVx41GEq2V9rGLdP3J3A+Cg8Y9gZEAnsAG4mIGEPOWqtVvNxBhDmAy44plxiIfQ==*CgYIASAHKAESPgo8qv+sT66jxoWJ4ljJSHa+zfyYxd49Pt1wh+UceqTZiAw2HLbs/ih24wtDPnZVi4Slb7A6LLDXbm5/i9xEGgA=#1##",                        // 收件人姓名(密文) 
            "post_addr": {
              "province": {
                "id": "110000",
                "name": "北京市"  
              },
              "city": {
                "id": "110000",
                "name": "市辖区"
              },
              "town": {
                "id": "110000",
                "name": "海淀区"
              },
              "street": {
                "id": "110000",
                "name": "中关村街道"
              },
              "encrypt_detail": "##Av2EYuW9rDSeF5TUObGZV314xS0a7lvefIIW5weE+dITrp1fSxFUkF7w2bVzW+62eLkqHN16Jz/17o7wFB78A0P6LuLxvR58PZptanTuzyoDQbEOGGkL+gcb2B0p0jAK68XkI4ZD*CgYIASAHKAESPgo8zi1miJ8Znc1mlEAH3RlK8LGz9o4hMOAfmcSRxXKr3kg9YHHggudKhfRmy/cAaZg+/6QoJM/3LDt5qXGIGgA=#1##"  // 详细地址(密文) 
            },

          },
          "Error_Code": 0,
          "Error_Msg": ""
          "AllowRetry": null,
          "RequestId": "20220322142251106"
        }
```

---
