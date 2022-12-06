from crawling import *
from send_email import *
from template_email import *
import json
import datetime

def handler(event=None, context=None):
    data = crawling()
    nowDate = datetime.datetime.now() + datetime.timedelta(hours=9)
    report_date = nowDate.strftime('%Y-%m-%d %H:%M:%S')
    email_body = template_email % (report_date, data)
    
    sendNaver(to=[], subject='슈퍼투데이 오늘마감 리포트 (' + report_date + ')', body=email_body)
    return {
        'statusCode': 200,
        'body': json.dumps('SuperToday Crawling and sending email OK!')
    }

handler()