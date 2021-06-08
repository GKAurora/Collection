# 第一周接口

## 沙箱使用

xxxxxxx


HOST: `https://baidu.com`
## 鉴权与注销

url: `/controller/v2/tokens`  
methods: `post`  
参数: ```
authCredit: {
    userName: "admin"
    password: "admin"
}
```

响应
```
{
	"data" : {
		"token_id" : "x-iqbw3xjy5hiqs5nyakddgbc6piti4a7vheqmnzdfaqvvemfs2k04vxc6k95e4ampk7hdvzkbnvupk77zvs89vs5grs1cfvk77ts4fv05herx7v9j06lilcapg5vy3w09",
		"expiredDate" : "2018-10-30 10:09:23"
	},
	"errcode" : "0x11aa22bb",
	"errmsg" : "The userName or password is incorrect."
}
```
描述: 
提供账号密码，获取token.
token在data的token_id中  


## 在线AP设备数量

