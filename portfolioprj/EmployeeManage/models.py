from django.db import models

# 従業員データ
class Employee(models.Model):
    #①models.py に以下フィールド設定し、以下コマンド実行でDBとテーブル作成される
    #  manage.py makemigrations
    #  python3 manage.py migrate EmployeeManage
    #②管理ユーザ作成
    #  python3 manage.py createsuperuser
    #③アプリadmin.py　を以下のように編集でadminページからデータ操作できる
    #  from django.contrib import admin
    #  from EmployeeManage.models import Employee
    #  admin.site.register(Employee)
    
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=10)
    salary = models.IntegerField()

# ログインユーザとパスワード
class LoginUser(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=10)
    auth_num = models.IntegerField()


