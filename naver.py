import io

import sys

import urllib.request as req

from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://nv.veta.naver.com/fxshow"

value1 = {

'su' : 'SU10079'

}


value3 = {

'nrefreshx' : '0'

}

param1 = urlencode(value1)


param3 = urlencode(value3)

url = API+"?"+param1+'&'+param3

print(url)

reqData = req.urlopen(url).read()

savePath = "/Users/usang-in/Dropbox/test1.jpg"


with open(savePath,'wb') as saveFile:

saveFile.write(reqData)

print("다운로드 완료.")
