# 供应商 (Supplier) - 接入指南

### 外部供应商接入指南

#### 一、提供供应商信息

暂时没有开放申请入口，供应商把资料发给客服agiso，申请成功后，获取到supplierId

#### 二、引导授权

供应商引导商家在浏览器浏览自动发货平台授权url

传入参数

GET方式提交参数

#### 三、302跳转到供应商授权页

商家在自动发货上点击“获取授权”后，跳转到商家授权页

#### 四、302跳转到自动发货网站

商家在供应商授权页，身份验证通过后，由供应商跳转到自动发货网站，附带随机生成的code

#### 五、请求token（自动发货平台发起获取token请求）

自动发货的LoginCardPwdSupplier页面，会用接收到的code的去请求token，供应商需要提供code换token的接口。

POST方式提交参数

#### 六、获取卡种列表接口

返回数据

格式：JSON

#### 七、获取卡券接口

授权链接：（自动发货平台授权URL）

https://alds.agiso.com/supplier/authorize?supplierId=123456

授权链接：（供应商授权URL）

http://test.xxx.com/oauth/authorize?response_type=code&client_id=aadoage9w8pfpe&redirect_uri=http://alds.agiso.com/LoginCardPwdSupplier&state=1212

跳转链接：

http://alds.agiso.com/LoginCardPwdSupplier?code=f33138910d14106fc91b015c9fe16def&state=1212

请求token链接（获取TokenUrl）

http://test.xxx.com/oauth/token?code=f33138910d14106fc91b015c9fe16def&grant_type=authorization_code

返回数据，格式：JSON

Token具有一定有效期，时长由供应商定。注意：如果太短则商家要频繁授权，太长有一定风险。建议供应商管理后台保证token只有最近一个授权的有效。
只有IsError=false时，才会返回token，否则返回的数据只有错误码Code和错误Msg。

http://test.xxx.com/api/categoryList

http://test.xxx.com/api/purchase
