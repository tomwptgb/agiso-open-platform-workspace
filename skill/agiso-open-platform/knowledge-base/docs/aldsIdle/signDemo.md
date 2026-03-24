# 闲鱼自动发货 (AldsIdle) - 签名算法

## 签名说明

将所有API输入参数（除了sign参数），按参数名的字典序排序，将参数名和参数值依次拼接成一个字符串，在字符串的头部和尾部分别拼接上AppSecret，然后对整个字符串进行MD5加密（32位），即为sign的值。

**步骤：**
1. 将请求参数按参数名的字典序排序
2. 将参数名和参数值拼接成一个字符串
3. 在字符串前后添加AppSecret
4. 对拼接后的字符串进行MD5加密（32位，不区分大小写）

**示例：**
- 参数: appId=xxx, timestamp=1468476350, token=yyy
- 排序后拼接: AppSecret + appIdxxx + timestamp1468476350 + tokenyyy + AppSecret
- 对结果进行MD5加密得到sign值

## 示例代码

### Java

```java
/*
    * aopic：推送类型
    */
  @RequestMapping("/push/receiveMsg")
  public String receivedMsg(@RequestParam("timestamp") long timestamp, @RequestParam("json") String json, @RequestParam("aopic") long aopic, @RequestParam("sign") String sign) {  	
    Map<String, String> map = new HashMap<String, String>();
    map.put("json", json);
    map.put("timestamp", String.valueOf(timestamp));
    String appSecret = "777****9999";
    //参考签名算法
    String checkSign = getSign(map, appSecret);
    if(!checkSign.equals(sign)) {
      return "验签失败";
    }
    //业务处理模块
    
    return "";
  }
```

### C#

```c#
[Route('~/push/receivedMsg')]
  public ActionResult ReceivedMsg()
  {
      string appSecret = "******************";
      long timestamp = Util.ToLong(Request.QueryString["timestamp"]);
      long aopic = Util.ToLong(Request.QueryString["aopic"]); // 根据aopic判断推送类型
      string sign = Request.QueryString["sign"];
      string json = Request.Form["json"];
      var dictParams = new Dictionary<string, string>();
      dictParams.Add("timestamp", timestamp.ToString());
      dictParams.Add("json", json);
      //参考签名算法
      var checkSign = Sign(dictParams, appSecret);
      if (!string.Equals(checkSign, sign))
      {
          return Content("验签失败");
      }
      // 验签通过进行相关的业务

      return Content("");
  }
```

### PHP

```php
public function ReceivedMsg() {
    $appsecret = '******************';
    $timestamp = $_GET['timestamp'];
    $aopic = $_GET['aopic'];
    $sign = $_GET['sign'];
    $json = $_POST['json'];
    $str = $appsecret.'json'.$json.'timestamp'.$timestamp.$appsecret;
    $create_sign = md5($str);
    if(strcasecmp($sign, $create_sign) == 0) {
      // 验签通过
      return "";
    }else{
      // 验签通过
      die('验签失败');
    }
  }
```

### php

```php

  public function ReceivedMsg() {
    $appsecret = '******************';
    $timestamp = $_GET['timestamp'];
    $aopic = $_GET['aopic'];
    $sign = $_GET['sign'];
    $json = $_POST['json'];
    $str = $appsecret.'json'.$json.'timestamp'.$timestamp.$appsecret;
    $create_sign = md5($str);
    if(strcasecmp($sign, $create_sign) == 0) {
      // 验签通过
      return "";
    }else{
      // 验签通过
      die('验签失败');
    }
  }
  
        
```
