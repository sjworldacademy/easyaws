# 크롤링소스
from crawling import *  
# 이메일발송소스
from send_email import *
# 메일내용 템플릿 소스
from template_email import *
import json
import datetime

def handler(event=None, context=None):
    # 1. 크롤링 정보를 가져오고
    data = crawling()
    # 2. 현재날짜를 만들고
    # hours=9는 추후에 Lambda에 올라갈 예정으로 Lambda 시스템은 기본 UTC를 사용합니다. 
    # 따라서 한국시간은 9시간을 더합니다.
    nowDate = datetime.datetime.now() + datetime.timedelta(hours=9)
    report_date = nowDate.strftime('%Y-%m-%d %H:%M:%S')
    # 3. 메일내용 템플릿 소스에 2개의 데이터로 치환합니다.
    email_body = template_email % (report_date, data)
    
    # 4. 실제 메일을 발송합니다.
    rtn = sendNaver(to=[], subject='슈퍼투데이 오늘마감 리포트 (' + report_date + ')', body=email_body)
    if rtn == 'OK':
        return {
            'statusCode': 200,
            'body': 'SuperToday Crawling and sending email OK!'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'Error ' + rtn
        }
    
# handler()