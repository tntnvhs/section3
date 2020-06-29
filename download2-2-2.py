
import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://cafefiles.naver.net/20130807_299/ado6958_13758512900137n9W8_JPEG/896600176.jpg"
htmlURL = "http://google.com"
savePath = "/Users/usang-in/Dropbox/study/section2/test.jpg"
savePath2 = "/Users/usang-in/Dropbox/study/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()


saveFile1 = open(savePath,'wb') # w:write, r:read, a:add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2 :
    saveFile2.write(f2)

print("다운로드 완료!")
