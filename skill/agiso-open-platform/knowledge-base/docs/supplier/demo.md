# 供应商 (Supplier) - 示例代码

## Java

```java
@RequestMapping("/oauth/authorize")
    public String authorize(HttpServletRequest req, HttpServletResponse rsp) throws IOException{
        String response_type = req.getParameter("response_type");
        String client_id = req.getParameter("client_id");
        String redirect_uri = req.getParameter("redirect_uri");
        String state = req.getParameter("state");
        if (isNullOrEmpty(response_type) || isNullOrEmpty(client_id) || isNullOrEmpty(redirect_uri))
        {
            return "参数不能为空";
        }
        if(!response_type.equals("code"))
        {
            return "无效response_type";
        }
        //供应商提供的clientId
        String clientId = "5645b******a454";
        if (!client_id.equals(clientId))
        {
            return "无效的client_id";
        }
        if (!redirect_uri.startsWith("http://alds.agiso.com/LoginCardPwdSupplier"))
        {
            return "无效的跳转链接";
        }

        //相应的业务
        //if (!IsLogin)
        //{
        //    Redirect("/login");
        //}

        //随机生成code
        String code = getRadomString(32);
        saveCode(code);
        if (redirect_uri.contains("?"))
        {
            rsp.sendRedirect(redirect_uri + "&state=" + state+ "&code=" + code);
            return "";
        }
        else
        {
            rsp.sendRedirect(redirect_uri + "?state=" + state + "&code=" + code);
            return "";
        }
    }

    /*
     * 请求token
     */
    @RequestMapping("/oauth/token")
    @ResponseBody
    public SupplierOAuthTokenResponse token(HttpServletRequest req){
        String code = req.getParameter("code");
        String grant_type = req.getParameter("grant_type");
        if (isNullOrEmpty(code) || isNullOrEmpty(grant_type))
        {
            SupplierOAuthTokenResponse otRsp = new SupplierOAuthTokenResponse();
            otRsp.setError(true);
            otRsp.setMsg("参数不能为空");
            return otRsp;
        }
        if (!grant_type.equals("token"))
        {
            SupplierOAuthTokenResponse otRsp = new SupplierOAuthTokenResponse();
            otRsp.setError(true);
            otRsp.setMsg("grant_type类型不对");
            return otRsp;
        }
        if (!validCode(code))
        {
            SupplierOAuthTokenResponse otRsp = new SupplierOAuthTokenResponse();
            otRsp.setError(true);
            otRsp.setMsg("code已失效");
            return otRsp;
        }
        SupplierOAuthTokenResponse rsp = getToken(code);
        clearCode(code);
        return rsp;
    }

    /*
     * 获取卡种列表
     */
    @RequestMapping("/api/categoryList")
    @ResponseBody
    public SupplierCardCategoryListPageGetResponse categoryList(HttpServletRequest req){
        String access_token = req.getParameter("access_token");
        String key_word = req.getParameter("key_word");
        int page_no = toInt(req.getParameter("page_no"));
        int page_size = toInt(req.getParameter("page_size"));
        long timestamp = toLong(req.getParameter("timestamp"));
        String sign = req.getParameter("sign");
        if (isNullOrEmpty(access_token))
        {
            SupplierCardCategoryListPageGetResponse scclpgRsp =  new SupplierCardCategoryListPageGetResponse();
            scclpgRsp.setError(true);
            scclpgRsp.setMsg("token不能为空");
            return scclpgRsp;
        }

        Map<String, String> map = new HashMap<String, String>();
        map.put("access_token", access_token);
        map.put("key_word", key_word);
        map.put("page_no", String.valueOf(page_no));
        map.put("page_size", String.valueOf(page_size));
        map.put("timestamp", String.valueOf(timestamp));

        //供应商提供的clientSecret
        String clientSecret = "a3******234";
        //参考签名算法
        String checkSign = getSign(map, clientSecret); 
        if (!sign.equals(checkSign))
        {
            SupplierCardCategoryListPageGetResponse scclpgRsp =  new SupplierCardCategoryListPageGetResponse();
            scclpgRsp.setError(true);
            scclpgRsp.setMsg("验签失败");
            return scclpgRsp;
        }

        if (!validToken(access_token))
        {
            SupplierCardCategoryListPageGetResponse scclpgRsp =  new SupplierCardCategoryListPageGetResponse();
            scclpgRsp.setError(true);
            scclpgRsp.setMsg("token不存在或已过期");
            return scclpgRsp;
        }

        int totalRecord = getCategoryCount(page_no, page_size, key_word);
        List<CardCategory> list = getCategory(page_no, page_size, key_word);
        SupplierCardCategoryListPageGetResponse scclpgRsp =  new SupplierCardCategoryListPageGetResponse();
        scclpgRsp.setError(false);
        scclpgRsp.setTotalRecord(totalRecord);
        scclpgRsp.setCardCategoryList(list);
        return scclpgRsp;
    }

    /*
     * 获取卡券
     */
    @RequestMapping("/api/purchase")
    @ResponseBody
    public SupplierCardPurchaseResponse purchase(HttpServletRequest req){
        String access_token = req.getParameter("access_token");
        long tid = toLong(req.getParameter("tid"));
        long oid = toLong(req.getParameter("oid"));
        long cpc_id = toLong(req.getParameter("cpc_id"));
        int num = toInt(req.getParameter("num"));
        String type = req.getParameter("type");
        long timestamp = toLong(req.getParameter("timestamp"));
        String sign = req.getParameter("sign");
        
        Map<String, String> map = new HashMap<String, String>();
        map.put("access_token", access_token);
        map.put("tid", String.valueOf(tid));
        map.put("oid", String.valueOf(oid));
        map.put("cpc_id", String.valueOf(cpc_id));
        map.put("num", String.valueOf(num));
        map.put("type", type);
        map.put("timestamp", String.valueOf(timestamp));
        
        //供应商提供的clientSecret
        String clientSecret = "a3******234";
        //参考签名算法
        String checkSign = getSign(map, clientSecret);

        if (!sign.equals(checkSign))
        {
            SupplierCardPurchaseResponse scpRsp =  new SupplierCardPurchaseResponse();
            scpRsp.setError(true);
            scpRsp.setMsg("验签失败");
            return scpRsp;
        }

        if (!validToken(access_token))
        {
            SupplierCardPurchaseResponse scpRsp =  new SupplierCardPurchaseResponse();
            scpRsp.setError(true);
            scpRsp.setMsg("token不存在或已过期");
            return scpRsp;
        }

        //避免重复推送，以tid，oid，type为唯一值滤重
        if(hasHandle(tid, oid, type))
        {
            SupplierCardPurchaseResponse scpRsp =  new SupplierCardPurchaseResponse();
            scpRsp.setError(true);
            scpRsp.setMsg("订单号：" + tid + "-" + oid + "，已处理了");
            return scpRsp;
        }

        SupplierCardPurchaseResponse scpRsp =  new SupplierCardPurchaseResponse();
    	scpRsp.setError(false);
    	scpRsp.setCardPwdList(getCardPwd(tid, oid, cpc_id, num));
    	scpRsp.setAmount(200);
    	scpRsp.setOrderSn("2343543543");
    	return scpRsp;
    }
```

## C#

```c#
public class AuthorizeController : Controller
    {
        /// <summary>
        /// 引导授权
        /// </summary>
        [Route("~/oauth/authorize")]
        public ActionResult Index()
        {
            string response_type = Request.QueryString["response_type"];
            string client_id = Request.QueryString["client_id"];
            string redirect_uri = Request.QueryString["redirect_uri"];
            string state = Request.QueryString["state"];
            if (string.IsNullOrEmpty(response_type) || string.IsNullOrEmpty(client_id) || string.IsNullOrEmpty(redirect_uri))
            {
                return Content("参数不能为空");
            }
            if (response_type != "code")
            {
                return Content("无效response_type");
            }
            //供应商提供的clientId
            string clientId = "5645b******a454";
            if (client_id != clientId)
            {
                return Content("无效的client_id");
            }
            if (!redirect_uri.StartsWith("http://alds.agiso.com/LoginCardPwdSupplier"))
            {
                return Content("无效的跳转链接");
            }

            #region 相应的业务
            //if (!IsLogin)
            //{
            //    Redirect("/login");
            //}
            #endregion

            //随机生成code
            var code = Util.GetRadomString(32);
            SaveCode(code);
            if (redirect_uri.Contains("?"))
            {
                return Redirect(redirect_uri + "&state=" + HttpUtility.UrlEncode(state) + "&code=" + code);
            }
            else
            {
                return Redirect(redirect_uri + "?state=" + HttpUtility.UrlEncode(state) + "&code=" + code);
            }
        }

        /// <summary>
        /// 请求token
        /// </summary>
        /// <returns>返回json格式</returns>
        [Route("~/oauth/token")]
        public JsonResult Token()
        {
            string code = Request.QueryString["code"];
            string grant_type = Request.QueryString["grant_type"];
            if (string.IsNullOrEmpty(code) || string.IsNullOrEmpty(grant_type))
            {
                return Json(new SupplierOAuthTokenResponse()
                {
                    IsError = true,
                    Msg = "参数不能为空"
                });
            }
            if (grant_type != "token")
            {
                return Json(new SupplierOAuthTokenResponse()
                {
                    IsError = true,
                    Msg = "grant_type类型不对"
                });
            }
            if (!ValidCode(code))
            {
                return Json(new SupplierOAuthTokenResponse()
                {
                    IsError = true,
                    Msg = "code已失效"
                });
            }
            SupplierOAuthTokenResponse rsp = GetToken(code);
            ClearCode(code);
            return Json(rsp);
        }

        /// <summary>获取卡种列表</summary>
        /// <returns></returns>
        [Route("~/api/categoryList")]
        public JsonResult CategoryList()
        {
            string access_token = Request.Form["access_token"];
            string key_word = Request.Form["key_word"];
            int page_no = Util.ToInt(Request.Form["page_no"]);
            int page_size = Util.ToInt(Request.Form["page_size"]);
            long timestamp = Util.ToLong(Request.Form["timestamp"]);
            string sign = Request.Form["sign"];
            if (string.IsNullOrEmpty(access_token))
            {
                return Json(new SupplierCardCategoryListPageGetResponse()
                {
                    IsError = true,
                    Msg = "token不能为空"
                });
            }

            var dict = new Dictionary<string, string>()
            {
                { "access_token",  access_token},
                { "key_word",  key_word},
                { "page_no",  page_no.ToString()},
                { "page_size",  page_size.ToString()},
                { "timestamp", timestamp.ToString()}
            };

            //供应商提供的clientSecret
            string clientSecret = "a3******234";
            //参考签名算法
            string checkSign = Util.GetSign(dict, clientSecret); 
            if (sign != checkSign)
            {
                return Json(new SupplierCardCategoryListPageGetResponse()
                {
                    IsError = true,
                    Msg = "验签失败"
                });
            }

            if (!ValidToken(access_token))
            {
                return Json(new SupplierCardCategoryListPageGetResponse()
                {
                    IsError = true,
                    Msg = "token不存在或已过期"
                });
            }

            var list = GetCategory(page_no, page_size, key_word, out int totalRecord);
            return Json(new SupplierCardCategoryListPageGetResponse()
            {
                IsError = false,
                TotalRecord = totalRecord,
                CardCategoryList = list
            });
        }

        /// <summary>获取卡券</summary>
        /// <returns></returns>
        [Route("~/api/purchase")]
        public JsonResult Purchase()
        {
            string access_token = Request.Form["access_token"];
            long tid = Util.ToLong(Request.Form["tid"]);
            long oid = Util.ToInt(Request.Form["oid"]);
            long cpc_id = Util.ToLong(Request.Form["cpc_id"]);
            int num = Util.ToInt(Request.Form["num"]);
            string type = Request.Form["type"];
            long timestamp = Util.ToLong(Request.Form["timestamp"]);
            string sign = Request.Form["sign"];

            var dict = new Dictionary<string, string>()
            {
                { "access_token",  access_token},
                { "tid",  tid.ToString()},
                { "oid",  oid.ToString()},
                { "cpc_id",  cpc_id.ToString()},
                { "num", num.ToString()},
                { "type", type },
                {  "timestamp", timestamp.ToString() }
            };
            
            //供应商提供的clientSecret
            string clientSecret = "a3******234";
            //参考签名算法
            string checkSign = Util.GetSign(dict, clientSecret);

            if (sign != checkSign)
            {
                return Json(new SupplierCardCategoryListPageGetResponse()
                {
                    IsError = true,
                    Msg = "验签失败"
                });
            }

            if (!ValidToken(access_token))
            {
                return Json(new SupplierCardCategoryListPageGetResponse()
                {
                    IsError = true,
                    Msg = "token不存在或已过期"
                });
            }

            //避免重复推送，以tid，oid，type滤重
            if(HasHandle(tid, oid, type))
            {
                return Json(new SupplierCardCategoryListPageGetResponse()
                {
                    IsError = true,
                    Msg = $"订单号：{tid}-{oid}，已处理了"
                });
            }

            return Json(new SupplierCardPurchaseResponse()
            {
                IsError = false,
                CardPwdList = GetCardPwd(tid, oid, cpc_id, num)
            });
        }
    }
```
