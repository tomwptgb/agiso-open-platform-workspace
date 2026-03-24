# 淘宝自动发货 (ALDS) - 数据类型

## AldsTradesResult

执行自动发货返回的信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| Tid | Number |  | 交易编号 |
| ResultMsg | String |  | 结果信息 |
| ResultCode | Number |  | 结果代码      -90:授权失败      -85:交易不存在      -110:参数错误      -81:Taobao Api 请求时错误 |

---

## DummySendErrorInfo

虚拟发货错误信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| Tid | Number |  | 交易编号 |
| AllowRetry | Boolean |  | 是否充许重试 |
| ErrorCode | Number |  | 错误代码              -85:可重试的错误              -50:重复发货              -86:不可重试的错误;不支持该种发货方式。这个错误，提示目前的订单是不能用虚拟发货方式发货，请用非虚拟发货接口发货。              -90:授权失败 |
| ErrorMsg | String |  | 错误描述 |

---

## ItemUpdateAdditionalErrorInfo

修改宝贝附言错误信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| NumIid | Long |  | 宝贝ID |
| SkuId | Long |  | SKU ID |
| ErrorMsg | String |  | 错误描述 |

---

## ItemUpdateQuantityErrorInfo

修改库存数量错误信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| NumIid | Long |  | 宝贝ID |
| SkuId | Long |  | SKU ID |
| OuterId | String |  | 商家编码 |
| Quantity | Long |  | 库存数量 |
| Type | Long |  | 更新方式（增量更新或全量更新） |
| ErrorMsg | String |  | 错误描述 |

---

## Order

订单信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| Num | Number |  | 购买数量 |
| NumIid | Number |  | 宝贝ID |
| Oid | Number |  | 子订单编号 |
| OuterIid | String |  | 商家编码 |
| Payment | String |  | 实付金额 |
| Price | String |  | 价格（原价） |
| SkuPropertiesName | String |  | SKU属性名 |
| Title | String |  | 宝贝标题 |
| TotalFee | String |  | 商品金额 |
| ExpandCardExpandPriceUsedSuborder | String |  | 购物金核销子订单权益金分摊金额（单位为元） |

**备注：** 推送参数详细说明可参考淘宝API文档[淘宝API文档](https://open.taobao.com/api.htm?docId=121&docType=2)

---

## Trace

订单信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| StatusTime | String |  | 状态发生的时间 |
| StatusDesc | String |  | 状态描述 |
| Action | String |  | 节点说明 ，指明当前节点揽收、派送，签收。 |

---

## TradesCloseErrorInfo

关闭订单错误信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| Tid | Number |  | 交易编号 |
| ErrorMsg | String |  | 错误描述 |

---

## TradesUpdateMemoErrorInfo

修改备注错误信息

| 字段名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| Tid | Number |  | 交易编号 |
| ErrorMsg | String |  | 错误描述 |

---
