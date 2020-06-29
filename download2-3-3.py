
import sys
import io
import urllib.request as req
from urllib.parse import urlencode#

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd' : '1001' #제이슨으로 받는다
}
print('before',values)
params = urlencode(values) #위에서 선언한 values
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
