#다음 실시간 뉴스 기사 수집기
# 다음 실시간 뉴스 목록(list: 15개)에서 URL을 추출
# -> 15개 URL
# -> 각 URL별로 기사 제목, 본문, 날짜 수집

import requests                 # 전체 소스코드
from bs4 import BeautifulSoup   # 원하는 정보 SELECT
from service.service_news import get_news

count = 0 # 전체 기사 수
url = "http://news.daum.net/breakingnews/digital"
result = requests.get(url)

if result.status_code == 200:
    print(result, "접속 성공 -> 데이터를 수집합니다.") # 200(성공)

    doc = BeautifulSoup(result.text, "html.parser")
    url_list = doc.select("ul.list_news2 a.link_txt")
    for url in url_list:
        print(f"{count+1} ", "="*100)
        get_news(url["href"])
        count += 1
else:
    print("URL 경로가 잘못됐습니다. 확인부탁드립니다.")


