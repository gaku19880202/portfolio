# Request
from django.http import HttpResponse
# DB接続
from .models import Employee
import MySQLdb
from .connectDb import ConnectDB
# Log出力
import logging
# Error処理
from .errorList import SessinoTimeOutError
from .errorList import DbError
from .errorList import ValidationError
# Form
from .forms import EmployeeFrom
from .forms import CreateEmployeeFrom
from django.shortcuts import render, get_object_or_404, redirect
# 共通関数
from .commonDef import registerSession
from .commonDef import checkSession
from .commonDef import doValidation

#Log設定取得
logger = logging.getLogger("file")
    
def index(request):
    """ Login画面に遷移 """
    return render(request, 'EmployeeManage/EmployeeManage.html')

def doLogin(request):
    """ Login時のパスワードチェック """
    #画面の値受け取り
    strName = request.POST['User']
    strPassword = request.POST['Password']
    #Userに紐づいたPassword取得
    strGetPassword = ConnectDB.getLoginUserPw(strName)
    if strGetPassword == strPassword:
        #ログ出力
        logger.info("login")
        #Session登録
        registerSession(request,strName)
        # Form 取得
        form = EmployeeFrom(request.POST or None)
        #models.py を使用した値取得
        # infodata = Employee.objects.all() #こちらでも全て取得できるが設定によって挙動が異なる
        empData = Employee.objects.values()
        empDict = {'emplist':empData,'form': form}
        return render(request, 'EmployeeManage/Top.html',empDict)
    else:
        empDict = {'Err':'ログインユーザ、パスワードが間違っています。'}
        return render(request, 'EmployeeManage/EmployeeManage.html',empDict)

def Top(request):
    """ Top画面 """
    try:
        #Session 確認
        checkSession(request)
        # Form 取得
        form = EmployeeFrom(request.POST or None)
        # Employee データ取得
        empData = Employee.objects.values()
        empDict = {'emplist':empData,'form': form}
        return render(request, 'EmployeeManage/Top.html',empDict)
    except (SessinoTimeOutError,DbError) as e:
        #画面に渡すディクショナリ作成
        params = {'strErrMsg':e,}
        return render(request, 'EmployeeManage/Error.html',params)

def doSearch(request):
    """ データ検索 """
    try:
        #Session 確認
        checkSession(request)
    
        # Form 取得
        form = EmployeeFrom(request.POST or None)
        # Form バリデーションチェック
        dictError = {}
        dictError = doValidation(form,'doSearch')
        if len(dictError)>0:
            raise ValidationError('Validationでエラーが発生しました。')
        #画面の値受け取り
        strId = request.POST['id_num']
        strName = request.POST['name']
        strDept = request.POST['dept']
        intSalary = request.POST['salary']
        intRadio = request.POST['radio'] # 1 →Higher　2 →Lower

        # データ探索
        empDict = {}
        empDict=ConnectDB.doSearch(strId,strName,strDept,intSalary,intRadio)
        # ディクショナリに From 追加
        empDict['form'] = form
        return render(request, 'EmployeeManage/Top.html',empDict)
    except (SessinoTimeOutError,DbError) as e:
        #画面に渡すディクショナリ作成
        params = {'strErrMsg':e,}
        return render(request, 'EmployeeManage/Error.html',params)
    except ValidationError as e:
        params = {'strErrMsg':dictError,'form':form}
        return render(request, 'EmployeeManage/Top.html',params)

def UserEdit(request):
    """ UserEdit画面に遷移 """
    try:
        #Session 確認
        checkSession(request)
        # Form 取得
        form = EmployeeFrom(request.POST or None)
        #models.py を使用した値取得
        empData = Employee.objects.values()
        empDict = {'emplist':empData,'form': form}
        return render(request, 'EmployeeManage/UserEdit.html',empDict)
    except (SessinoTimeOutError,DbError) as e:
        #画面に渡すディクショナリ作成
        params = {'strErrMsg':e,}
        return render(request, 'EmployeeManage/Error.html',params)

def doUserCreate(request):
    """ User作成処理 """
    try:
        #Session 確認
        checkSession(request)
        # Form 取得
        form = CreateEmployeeFrom(request.POST or None)
        # Form バリデーションチェック
        dictError = {}
        dictError = doValidation(form,'doUserCreate')
        if len(dictError)>0:
            raise ValidationError('Validationでエラーが発生しました。')
        #画面の値受け取り
        strName = request.POST['name']
        strDept = request.POST['dept']
        intSalary = request.POST['salary']
        #Create実行
        strErr = ConnectDB.doCreate(strName,strDept,intSalary)
        empData = Employee.objects.values()
        empDict = {'emplist':empData,'form': form}
        return render(request, 'EmployeeManage/Top.html',empDict)
    except (SessinoTimeOutError,DbError) as e:
        #画面に渡すディクショナリ作成
        params = {'strErrMsg':e,}
        return render(request, 'EmployeeManage/Error.html',params)
    except ValidationError as e:
        params = {'strErrMsg':dictError,'form':form}
        return render(request, 'EmployeeManage/UserEdit.html',params)

def doUserUpdate(request):
    """ User更新処理 """
    try:
        #Session 確認
        checkSession(request)
        # Form 取得
        form = EmployeeFrom(request.POST or None)
        # Form バリデーションチェック
        dictError = {}
        dictError = doValidation(form,'doUserUpdate')
        if len(dictError)>0:
            raise ValidationError('Validationでエラーが発生しました。')
        #画面の値受け取り
        strId = request.POST['Id']
        strName = request.POST['Name']
        strDept = request.POST['Dept']
        intSalary = request.POST['Salary']
        #Update実行
        strErr = ConnectDB.doUpdate(strId,strName,strDept,intSalary)
        empData = Employee.objects.values()
        empDict = {'emplist':empData,'form': form}
        return render(request, 'EmployeeManage/Top.html',empDict)
    except (SessinoTimeOutError,DbError) as e:
        #画面に渡すディクショナリ作成
        params = {'strErrMsg':e,}
        return render(request, 'EmployeeManage/Error.html',params)
    except ValidationError as e:
        params = {'strErrMsg':dictError,'form':form}
        return render(request, 'EmployeeManage/UserEdit.html',params)

def doUserEdit(request):
    """ ユーザ更新、ユーザ削除処理 """
    try:
        #Session 確認
        checkSession(request)
        #どのボタンが押されたか調べる為、POSTをループする
        for p in request.POST:
            # Updateがクリックされた場合の処理
            if 'btnUpdate' in p:
                getTarget = p
                #何番目のボタンが押されたか判定
                pList = getTarget.split('_')
                strTargetId = pList[1]
                #Id に紐づいた値を取得
                strName = ConnectDB.getName(strTargetId)
                strDept = ConnectDB.getDept(strTargetId)
                strSalary = ConnectDB.getSalary(strTargetId)
                # Form 取得(初期値設定）
                initial_dict = {
                    'id_num': strTargetId,
                    'name': strName,
                    'dept': strDept,
                    'salary': strSalary,
                }
                form = EmployeeFrom(initial = initial_dict)
                #画面に渡すディクショナリ作成
                params = {
                    'form': form,
                }
                return render(request, 'EmployeeManage/UserUpdate.html',params)
            # Deleteがクリックされた場合の処理
            if 'btnDelete' in p:
                getTarget = p
                # Form 取得
                form = EmployeeFrom(request.POST or None)
                #何番目のボタンが押されたか判定
                pList = getTarget.split('_')
                strTargetId = pList[1]
                #models.py を使用したデータ削除
                Employee.objects.filter(id=strTargetId).delete()
                #models.py を使用した値取得
                empData = Employee.objects.values()
                empDict = {'emplist':empData,'form': form}
                return render(request, 'EmployeeManage/UserEdit.html',empDict)
    
    except (SessinoTimeOutError,DbError) as e:
        #画面に渡すディクショナリ作成
        params = {'strErrMsg':e,}
        return render(request, 'EmployeeManage/Error.html',params)
