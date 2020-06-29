from bs4 import BeautifulSoup
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("car.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_func("#gr")
car_func("li#gr")
car_func("ul>li#gr")
car_func("#cars>#gr")
car_func("li[id='gr']")


print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)
