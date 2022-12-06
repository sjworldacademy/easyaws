# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup

def crawling():

    print('Crawling Start...')
    
    # 1. URL로 요청
    res = requests.get('https://www.suto.co.kr/bbs/today_close.php')
    #print(res.text)
    
    # 2. 해당 Dom Element를 잡아낸다.
    parse_class_name = 'div.tbl_wrap'
    soup = BeautifulSoup(res.text, "html.parser")
    
    # 3. 리턴할 html 배열을 생성
    html = []
    html.append('<table>')
    html.append('<colgroup><col width="5%"/><col width="5%"/><col width="*"/><col width="20%"/><col width="5%"/><col width="5%"/><col width="5%"/></colgroup>')
    html.append('<thead><tr><th>번호</th><th>분류</th><th>제목</th><th>경품태그</th><th>발표</th><th>조회</th><th>추천</th></tr></thead>')
    html.append('<tbody>')
    
    # 4. 가져올 데이터의 tr 부분을 select해서
    trs = soup.select(parse_class_name + ' table tbody tr')
    
    # 5. 반복해서 데이터를 가져온다.
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
            # 6. 실제 url로 이미지와 링크를 변경한다.
            html.append(tdstr.replace('"/', '"https://www.suto.co.kr/').replace('<a ', '<a target="_blank" ').replace('</a>', '</a><br>'))

    html.append('</tbody>\n</table>')
    
    # 7. 가져온 html 배열을 문자열로 합쳐낸다.
    data = '\n'.join(html)
    print('Crawling Complete!')
    return data

if __name__ == "__main__":
    cr = crawling()
    print(cr)