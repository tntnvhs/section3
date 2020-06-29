from bs4 import BeautifulSoup
import io
import sys
import urllib.request as req
import urllib.parse as rep



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base ="https://www.inflearn.com/"
#quote = rep.quote_plus("추천-강좌")

url = base


res = req.urlopen(url).read()


soup = BeautifulSoup(res, "html.parser")

recommand = soup.select(".course_title")


for e in recommand:
    print(e.select_one(".course_card_front>.course_title").string)
