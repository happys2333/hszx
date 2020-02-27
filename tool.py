#衡中内部专用，开源程序，欢迎交流
#@qq:1013214271
#@author:开心
#coding=utf-8
#感谢卢志远学弟提供的账号密码，以便我抓包
import requests
import re
import os
print("本程序用于自动下载网课文件")
print("由开心设计完成，衡中内部交流讨论专用")
s=requests.Session()
s.headers.clear()
headers={#浏览器伪装
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.1.2.3000 Chrome/55.0.2883.75 Safari/537.36'
}
s.headers=headers
r=s.get("http://home.xinkaoyun.com/login.html")
#print(r.status_code)
print("鑫考打开成功")
def findall_chinese(s):
    return re.compile('[\u4e00-\u9fff]+').findall(s)
#print(r.text)
#下面这部分是废弃设计，因为我后面直接抓的cookie所以不需要输入账号密码了
# data={
#     "userName":id ,#用户名
#     "passWord":password , #密码
#     "IP": ip #ip地址
# }
# nre=s.post("http://usr.xinkaoyun.com/api/HSCPC/Login",data=data,headers=headers)
# s.get("http://user-analysis.7moor.com/service?action=page.unload&data=%7B%22pageId%22%3A%221a8d11b0-5906-11ea-8af0-8b6e5c979a65%22%2C%22userId%22%3A%22d0e77ea1-58f7-11ea-92a9-d1938fed967f%22%2C%22sessionId%22%3A%22d0e77ea2-58f7-11ea-92a9-d1938fed967f%22%2C%22account%22%3A%22N00000034824%22%2C%22platform%22%3A%7B%22browserName%22%3A%22Chrome%22%2C%22browserVersion%22%3A%2270.0.3538.25%22%2C%22osInfo%22%3A%22Windows%2010%2064-bit%22%2C%22platformDescription%22%3A%22Chrome%2070.0.3538.25%2032-bit%20on%20Windows%2010%2064-bit%22%2C%22seosource%22%3A%22%E7%AB%99%E5%86%85%22%2C%22seokeywords%22%3A%22%22%7D%2C%22page%22%3A%7B%22title%22%3A%22%E9%91%AB%E8%80%83%E4%BA%91%E6%A0%A1%E5%9B%AD%E7%B3%BB%E7%BB%9F%22%2C%22prevUrl%22%3A%22http%3A%2F%2Fhome.xinkaoyun.com%2F%22%2C%22currentUrl%22%3A%22http%3A%2F%2Fhome.xinkaoyun.com%2Flogin.html%22%2C%22id%22%3A%221a8d11b0-5906-11ea-8af0-8b6e5c979a65%22%2C%22stayTime%22%3A38875%7D%2C%22type%22%3A%22unload%22%2C%22isOpenChat%22%3Afalse%2C%22uvpvSwitch%22%3A%22false%22%7D&callback=ubaGetCallback")
# test=nre.text
# if test.__contains__("StuSex") and (test.__contains__("男")or test.__contains__("女")):
#     print("登录成功")
# else:
#     print("账号密码错误")
#     exit(1)
# #print(nre.status_code)
data2={
"schoolId": "311",
"onlyCode": "21900346"
}
nre=s.get("http://home.xinkaoyun.com/public.html#/")
nre=s.get("http://home.xinkaoyun.com/HCtransfer.html")
nre=s.post("http://usr.xinkaoyun.com/api/b2b/Getxxjjschoolid",data=data2)
data2={
"schoolId": "311",
"userId": "211331",
"action": "湖城云课",
"remark": "",
"type": "PC",
"IP": ""
}
nre=s.post("http://usr.xinkaoyun.com/api/sco/ScoActionLog",data=data2)
nre=s.get("http://mv.xinkaoyun.xyz:8080/?a=yxyLogin&schoolId=311&onlyCode=21900346")
urlnew=input("请输入你课程的网址,按回车确认")
newr=s.get(urlnew)
ft=newr.text
if ft.__contains__("movie")and ft.__contains__("value"):
    chinese= findall_chinese(ft)
    p=chinese.index("当前位置")
else:
    print("未知错误，请联系作者修BUG")
    exit(1)
if(chinese[p+5]=="视频播放不够流畅"):
    print(chinese[p+3]+chinese[p+4]+"的视频网址为：")
else:
    print(chinese[p+3]+chinese[p+4]+chinese[p+5]+"的视频网址为：")
first=ft.index("https://p.bokecc.com")
last=ft.index(".swf")
newstr=ft[first:last]+".swf"
nre=s.get(newstr)
print(nre.url)
def text_create(msg):
    name="web"
    desktop_path = os.path.abspath('.').replace("\\","\\\\")+"\\\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
text_create(nre.url+"\n")
input("网址已经保存在本程序目录下的web.txt，按回车退出")