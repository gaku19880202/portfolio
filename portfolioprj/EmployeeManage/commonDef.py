# Request
from django.http import HttpResponse
# Log出力
import logging
# Error処理
from .errorList import SessinoTimeOutError
from .errorList import DbError
from .errorList import ValidationError

#Log設定取得
logger = logging.getLogger("file")
    
def registerSession(request,strName):
    """ セッションに登録する"""
    logger.info("Sessionにログインユーザを登録しました。")
    request.session['User'] = strName
    return None
 
def checkSession(request):
    """ セッションをチェックする"""
    try:
        #Session 確認　エラーの場合、SessionTimeOutと判定
        strName = request.session['User']
    except Exception as e:
        logger.error('SessionTimeOutです。ログアウトして下さい。')
        raise SessinoTimeOutError('SessionTimeOutです。ログアウトして下さい。')
    return None

def doValidation(form,strGamenName,request):
    """ FormのValidationチェック """
    # Form バリデーションチェック
    if form.is_valid():
        logger.info("validation OK " + strGamenName)
        #form.save() # DBにFormの値を格納できる(Forms.formの場合)
    else:
        #なぜかradioのエラーが常時発生してしまうため、エラーを削除する
        #エラーはディクショナリで返される
        try:
            del form.errors['radio']
        except Exception as e:
            #エラー発生の場合、ディクショナリにエラーがない為
            logger.info("validation OK " + strGamenName)
            
        if len(form.errors)>0:
           logger.info("validation NG " + strGamenName)
        else:
            logger.info("validation OK " + strGamenName)

    return form.errors
