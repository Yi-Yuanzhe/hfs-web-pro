import requests
import urllib
import json

from app import EncPwd

#account = 'yicorleone'
#password = '31e56aaab8b80e5ca2d1a8e4d55f0519'
url_login = "http://hfs-be.yunxiao.com/v1/user/user-session"
url_score = "http://hfs-be.yunxiao.com/v1/score"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

account = ''
password = ''
loginResult = ''
queryResult = ''

s = requests.Session()

def login():
    pwd_md5 = EncPwd.md5(password)
    values = {"account" : account, "pass" : pwd_md5, "rememberMe":2, "roleType":1}
    resp = s.post(url_login, values, headers = headers).text
    global loginResult
    loginResult = json.loads(resp)

def getScore():
    resp = s.get(url_score, headers = headers)
    global queryResult
    queryResult = json.loads(resp.text)

def isLogin():
    if loginResult is not None:
        if loginResult['msg'] == "创建用户登录Session成功":
            return True
        else:
            return False
    else:
        return False
