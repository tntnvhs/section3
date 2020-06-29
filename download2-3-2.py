
import sys
import io
import urllib.request as req
from urllib.parse import urlencode#
#브라우저를 열지 않고 정보 가져올 수 있음
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


API = "https://api.ipify.org"

values = {
    'format' : 'json' #제이슨으로 받는다
}
print('before',values)
params = urlencode(values) #위에서 선언한 values
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
