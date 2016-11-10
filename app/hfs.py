import requests
import urllib
import json

from app import EncPwd

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
    strResult = str(queryResult)
    a = strResult.replace('msg', '信息')
    b = a.replace('name', '考试名称')
    c = b.replace('gradeStudentNum', '全级人数')
    d = c.replace('classStudentNum', '全班人数')
    e = d.replace('score', '全科总分')
    f = e.replace('realScore', '你的总分')
    g = f.replace('classAvg', '全班平均')
    h = g.replace('classRank', '全班排名')
    i = h.replace('gradeAvg', '全级平均')
    strResult = i.replace('gradeRank', '全级排名')

def isLogin():
    if loginResult is not None:
        if loginResult['msg'] == "创建用户登录Session成功":
            return True
        else:
            return False
    else:
        return False
