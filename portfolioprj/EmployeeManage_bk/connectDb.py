import MySQLdb
from MySQLdb.cursors import DictCursor
import logging
from .errorList import DbError

logger = logging.getLogger("file")

class ConnectDB:
    #クラス変数定義
    strDbUser = 'root'
    strHostName = 'localhost'
    strDbName = 'Employee'
    strTblNameEmp = 'EmployeeManage_employee'
    strTblNameLogin = 'EmployeeManage_loginuser'
    strCharSet = "utf8"
    strMsgErrDb = 'DB関連のエラーが発生しました。ログアウトして下さい。'

    def getLoginUserPw(strName):
        pw=''
        strSql = "SELECT password FROM " + ConnectDB.strTblNameLogin + " WHERE name = '" + strName +"';"
        try:
            #DB接続
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor()
            #SQL実行
            cur.execute(strSql)
            pw = cur.fetchall()
            #tuple 2つに囲まれて出てくるので整形
            pw=pw[0]
            pw=pw[0]
            return pw
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)

    def doSearch(strId,strName,strDept,intSalary,intRadio):
        empDict = {}
        empList = []
        flgWhere =False
        try:
            #DB接続
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor(DictCursor)
            strSql = "SELECT * FROM " + ConnectDB.strTblNameEmp
            #条件文作成
            if len(strId) != 0:
                strSql = strSql + " WHERE id = " + strId 
                flgWhere = True
            
            if len(strName) != 0:
                if flgWhere:
                    strSql = strSql + " AND name = '" + strName + "'"
                else:
                    strSql = strSql + " Where name = '" + strId + "'"
                    flgWhere = True

            if len(strDept) != 0:
                if flgWhere:
                    strSql = strSql + " AND dept = '" + strDept + "'"
                else:
                    strSql = strSql + " Where dept = '" + strDept + "'"  
                    flgWhere = True

            if len(intSalary) != 0:
                # radioButton → Higher
                if intRadio=='1':
                    if flgWhere:
                        strSql = strSql + " AND salary >= " + intSalary 
                    else:
                        strSql = strSql + " Where salary >= " + intSalary
                # radioButton → Lower
                if intRadio=='2':
                    if flgWhere:
                        strSql = strSql + " AND salary <= " + intSalary 
                    else:
                        strSql = strSql + " Where salary <= " + intSalary 

            #SQL実行
            cur.execute(strSql)
            rows = cur.fetchall()
            #引数として渡すためにディクショナリに入れる
            for row in rows:
                empList.append(row)

            empDict = {'emplist':empList,}
            return empDict
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)

    def doCreate(strName,strDept,intSalary):
        strErr = ''
        strSql = "INSERT INTO " + ConnectDB.strTblNameEmp + \
                 "(name,dept,salary) VALUES ('" + strName + "','" + \
                 strDept + "'," + intSalary + ");" 
        try:
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor(DictCursor)
            #SQL実行
            cur.execute(strSql)
            connect.commit()
            return None
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)

    def doUpdate(strId,strName,strDept,intSalary):
        strSql = "UPDATE " + ConnectDB.strTblNameEmp + \
                 " SET name ='" + strName + "', dept = '" + strDept + "', salary =" \
                  + intSalary + " WHERE id = " + strId + ";"
        try:
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor(DictCursor)
            #SQL実行
            cur.execute(strSql)
            connect.commit()
            return None
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)

    def getName(strId):
        strSql = "SELECT name from " + ConnectDB.strTblNameEmp + " WHERE id ='" + strId + "';"
        try:
            #DB接続
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor()
            #SQL実行
            cur.execute(strSql)
            name = cur.fetchall()
            #tuple 2つに囲まれて出てくるので整形
            name = name[0]
            name = name[0]
            return name
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)

    def getDept(strId):
        dept=''
        strSql = "SELECT dept from " + ConnectDB.strTblNameEmp + " WHERE id ='" + strId + "';"
        try:
            #DB接続
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor()
            #SQL実行
            cur.execute(strSql)
            dept = cur.fetchall()
            #tuple 2つに囲まれて出てくるので整形
            dept = dept[0]
            dept = dept[0]
            return dept
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)

    def getSalary(strId):
        salary=''
        strSql = "SELECT salary from " + ConnectDB.strTblNameEmp + " WHERE id ='" + strId + "';"
        try:
            #DB接続
            connect = MySQLdb.connect(db=ConnectDB.strDbName, host=ConnectDB.strHostName, port=3306, user=ConnectDB.strDbUser, charset=ConnectDB.strCharSet)
            cur = connect.cursor()
            #SQL実行
            cur.execute(strSql)
            salary = cur.fetchall()
            #tuple 2つに囲まれて出てくるので整形
            salary = salary[0]
            salary = salary[0]
            return salary
        except Exception as e:
            logger.error(e)
            raise DbError(ConnectDB.strMsgErrDb)