# 2019-01-28 수정
# 기존 daum 주식 사이트 : ajax 방식으로 변경으로 인해 이를 반영한 코드를 수정.
# pip install fake-useragent 설치 후 실행 가능
from bs4 import BeautifulSoup
import io
import sys
import urllib.request as req



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url ="https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949')
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#popularItemList > li > a")

print('네이버 주식 인기검색 종목 10위')
for i, e in enumerate(top10, 1):
    print('순위 : {}, 이름 : {}'.format(i, e.string))
