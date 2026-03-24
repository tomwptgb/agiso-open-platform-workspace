# 打印 (Print) - 接入指南

### 接入指南

#### 1、接入流程

【开发者操作】登录后台申请AppIds。

https://open.agiso.com/#/my/application/app-list

【开发者操作】申请到AppId后，开发者可以登录后台管理AppId，这里可以查看和更换AppSecret、更改推送url、更改授权回调url等。

【商家操作】授权，方法有二：

1、输入开发者提供的AppId（相当于告诉Agiso，允许这个AppId通过Agiso开放平台获取或操作商家自己的订单数据），勾选相应要授权的权限。授权后会显示一个Token，将Token复制给开发者。

2、开发者如果有开发自动授权，则商家可以通过访问以下页面进行授权：

【开发者操作】开发者得到各个商家授权给的Token，并使用Token调用接口。调用接口时，需要使用AppSecret进行签名，具体签名方法参见下文。

注意：开发者与商家，也可以是同一个人。

#### 2、获取AccessToken详解

AccessToken的有效期和您的用户购买Agiso软件的使用时间一致。如果您的用户续费，那么AccessToken的有效期也会延长。

2、引导用户登录授权

引导用户通过浏览器访问以上授权url

3、获取code

用户点“授权”按钮后，Agiso自动发货会将授权码code、自定义参数state返回到了回调地址上，应用可以获取并使用该code去换取AccessToken

4、换取AccessToken

换取AccessToken返回值示例

换取AccessToken返回参数说明

#### 3、调用接口详解

注意：接口调用配额，20次/秒。

#### 4、签名算法

#### 5、Header设置示例代码

#### 6、签名算法示例代码

#### 7、完整调用API示例代码

以下代码以调用LogisticsDummySend(更新发货状态)为例

【对所有API请求参数（包括公共参数和业务参数，但除去sign参数和byte[]类型的参数），根据参数名称的ASCII码表的顺序排序。如：foo=1, bar=2, foo_bar=3,
        foobar=4排序后的顺序是bar=2, foo=1, foo_bar=3, foobar=4。

将排序好的参数名和参数值拼装在一起，根据上面的示例得到的结果为：bar2foo1foo_bar3foobar4。

把拼装好的字符串采用utf-8编码，在拼装的字符串前后加上app的secret后，使用MD5算法进行摘要，如：md5({$开发者应用的AppSecret}bar2foo1foo_bar3foobar4{$开发者应用的AppSecret})

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| appId | 是 | long | 应用的appId |
| state | 否 | string | 开发者自定义参数，授权回调会把该参数回传回去 |
