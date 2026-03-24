# 开放平台 (Open) - API 接口文档

**请求域名：** `https://gw-api.agiso.com/open/`

---

## 删除托管电商业务应用

**简要描述：** 删除托管电商业务应用

**请求URL：** `/AppManage/DeleteManagedApp`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null,
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---

## 取消禁用应用

**简要描述：** 取消禁用应用

**请求URL：** `/AppManage/CancelDisableManagedApp`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null,
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---

## 更新托管电商业务应用的信息

**简要描述：** 更新托管电商业务应用的信息

**请求URL：** `/AppManage/UpdateManagedApp`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| appName | 是 | String | 应用名称 |
| appId | 是 | Long | 应用id |
| description | 否 | String | 应用描述 |
| callBackUrl | 否 | String | 回调地址 |
| website | 否 | String | 应用网址（官网） |
| notifyUrl | 否 | String | 通知推送地址 |
| ips | 否 | String | IP白名单，多个IP之间用逗号“,”分隔 |
| allowHandAuth | 否 | Boolean | 是否允许自动发货后台进行手动授权。 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null,
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

**备注：** 更新时是全量更新，所以哪怕不打算更新的字段，也要把原来的值传入进来

---

## 查询开放平台余额

**简要描述：** 查询开放平台余额

**请求URL：** `/Bankroll/QueryDeposit`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": 9610.737, // 余额
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---

## 申请托管电商业务应用

**简要描述：** 申请托管电商业务应用

**请求URL：** `/AppManage/ApplyManagedApp`

**请求方式：** POST

**请求参数：**

| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| appName | 是 | String | 应用名称 |
| description | 否 | String | 应用描述 |
| callBackUrl | 否 | String | 授权回调地址 |
| website | 否 | String | 应用网址（官网） |
| ips | 否 | String | IP白名单，多个IP之间用逗号“,”分隔 |
| notifyUrl | 否 | String | 通知推送地址（订单付款等消息推送） |
| allowHandAuth | 否 | Boolean | 是否允许自动发货后台进行手动授权。 |

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data":// 应用信息
      {
        "AppName": "应用名称",
        "AppId": 123456789,// 应用ID
        "AppSecret": "xxxxxxxxx",// secret
        "Description": "应用描述",
        "CallBackUrl": "http://xxx.com/yy",//授权回调地址
        "Website": "http://xxx.com", // 应用网址（官网）
        "Ips": "192.168.0.1,192.168.0.2", // IP白名单，多个IP之间用逗号“,”分隔
        "NotifyUrl": "http://xxx.com/noti",//通知推送地址（订单付款等消息推送）
        "AllowHandAuth": true // 是否允许自动发货后台进行手动授权
      },
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---

## 禁用应用

**简要描述：** 禁用应用

**请求URL：** `/AppManage/DisableManagedApp`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": null,
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---

## 读取托管电商业务应用的信息

**简要描述：** 读取托管电商业务应用的信息

**请求URL：** `/AppManage/GetManagedApp`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": // 应用信息
      {
        "AppName": "应用名称",
        "AppId": 123456789,// 应用ID
        "AppSecret": "xxxxxxxxx",// secret
        "Description": "应用描述",
        "CallBackUrl": "http://xxx.com/yy",//回调地址
        "Website": "http://xxx.com", // 应用网址（官网）
        "Ips": "192.168.0.1,192.168.0.2", // IP白名单，多个IP之间用逗号“,”分隔
        "NotifyUrl": "http://xxx.com/noti",//通知推送地址
        "AllowHandAuth": true // 是否允许自动发货后台进行手动授权
      },
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---

## 重置托管电商业务应用的Secret

**简要描述：** 重置托管电商业务应用的Secret

**请求URL：** `/AppManage/ResetManagedAppSecret`

**请求方式：** POST

**返回示例：**

```json
{
      "IsSuccess": true,
      "Data": { // 应用信息
            "AppId": 123456789,// 应用ID
            "AppSecret": "xxxxx",//重置后的secret
          },
      "Error_Code": 0,
      "Error_Msg": "",
      "AllowRetry": null,
      "RequestId": "2023022717413855"
    }
```

---
