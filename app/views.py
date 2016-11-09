from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import sys

from app import hfs

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
        title = 'Home')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        hfs.account = form.username.data
        hfs.password = form.password.data

        hfs.login()
        #flash('登录成功')
        #return redirect('/index')
        if hfs.isLogin():
            flash('登录成功')
            return redirect('/score')
        else:
            return redirect('/login')

    return render_template('login.html',
        title = 'Sign In',
        form = form)

@app.route('/score')
def score():
    hfs.getScore()
    loginResult = hfs.loginResult
    queryResult = hfs.queryResult
    strResult = hfs.strResult
    loginMsg = loginResult['msg']
    queryMsg = queryResult['msg']
    recentTest = queryResult['data'][0]['name']
    gradeStudentNum = str(queryResult['data'][0]['gradeStudentNum'])
    classStudentNum = str(queryResult['data'][0]['classStudentNum'])
    allScore = str(queryResult['data'][0]['details'][0]['score'])
    yourScore = str(queryResult['data'][0]['details'][0]['realScore'])
    classAvg = str(queryResult['data'][0]['details'][0]['classAvg'])
    classRank = str(queryResult['data'][0]['details'][0]['classRank'])
    gradeAvg = str(queryResult['data'][0]['details'][0]['gradeAvg'])
    gradeRank = str(queryResult['data'][0]['details'][0]['gradeRank'])
    complexSubject = str(queryResult['data'][0]['details'][1]['detailName'])
    allScore_complexSubject = str(queryResult['data'][0]['details'][1]['score'])
    yourScore_complexSubject = str(queryResult['data'][0]['details'][1]['realScore'])
    classAvg_complexSubject = str(queryResult['data'][0]['details'][1]['classAvg'])
    classRank_complexSubject = str(queryResult['data'][0]['details'][1]['classRank'])
    gradeAvg_complexSubject = str(queryResult['data'][0]['details'][1]['gradeAvg'])
    gradeRank_complexSubject = str(queryResult['data'][0]['details'][1]['gradeRank'])

    return render_template('score.html', loginMsg = loginMsg, strResult = strResult,
        queryMsg = queryMsg, recentTest = recentTest,
        gradeStudentNum = gradeStudentNum, classStudentNum = classStudentNum,
        allScore = allScore, yourScore = yourScore,
        classAvg = classAvg, classRank = classRank,
        gradeAvg = gradeAvg, gradeRank = gradeRank,
        complexSubject = complexSubject, allScore_complexSubject = allScore_complexSubject,
        yourScore_complexSubject = yourScore_complexSubject, classAvg_complexSubject = classAvg_complexSubject,
        classRank_complexSubject = classRank_complexSubject, gradeAvg_complexSubject = gradeAvg_complexSubject,
        gradeRank_complexSubject = gradeRank_complexSubject)
