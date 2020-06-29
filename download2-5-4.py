from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html ="""
    <html><body>
    <div id="main">
        <h1>강의목록</h1>
        <ul class="lecs">
            <li>java</li>
            <li>파이썬</li>
            <li>머신러닝</li>
            <li>안드로이드</li>
        </ul>
    </div>
    </body></html>

"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one("div#main>h1")

print("h1", h1.string)

list_li = soup.select("div#main > ul.lecs>li")

for li in list_li:

    print("li>>>", li.string)
