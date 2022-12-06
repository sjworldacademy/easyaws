# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from template_email import *

def crawling():

    print('Crawling Start...')
    
    res = requests.get('https://www.suto.co.kr/bbs/today_close.php')
    #print(res.text)
    
    parse_class_name = 'div.tbl_wrap'
    soup = BeautifulSoup(res.text, "html.parser")
    
    html = []
    html.append('<table>')
    html.append('<colgroup><col width="5%"/><col width="5%"/><col width="*"/><col width="20%"/><col width="5%"/><col width="5%"/><col width="5%"/></colgroup>')
    html.append('<thead><tr><th>번호</th><th>분류</th><th>제목</th><th>경품태그</th><th>발표</th><th>조회</th><th>추천</th></tr></thead>')
    html.append('<tbody>')
    
    trs = soup.select(parse_class_name + ' table tbody tr')
    for tr in trs:
        #print(tr)
        if str(tr).find("background:#fffdf5") < 0:
            td = BeautifulSoup(str(tr), "html.parser").select('td')
            tdstr = "<tr><td>%s</td><td>%s</td>%s<td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                td[0].text,
                td[1].text,
                td[2],
                td[3].text,
                td[5].text,
                td[6].text,
                td[7].text,
            )
            html.append(tdstr.replace('"/', '"https://www.suto.co.kr/').replace('<a ', '<a target="_blank" ').replace('</a>', '</a><br>'))

    html.append('</tbody>\n</table>')
    data = '\n'.join(html)
    print('Crawling Complete!')
    return data

if __name__ == "__main__":
    cr = crawling()
    print(cr)