from bs4 import BeautifulSoup
import io
import sys
import urllib.request as req
import urllib.parse as rep
import os



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("연애인")
url = base + quote


res = req.urlopen(url)
savepath = "/Users/usang-in/Dropbox/lion"

try:
    if not (os.path.isdir(savepath)):
        os.makedirs(os.path.join(savepath))

except OSError as e:
        if e.error != errno.EEXIST:
            print("폴더 만들기 실패")
            raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_list in enumerate(img_list, 1):
    print(img_list)

    fullFileName = os.path.join(savepath, savepath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")
