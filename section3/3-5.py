import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#요청  url

URL = 'https://www.wishket.com/accounts/login/'


#fake user-agent 생성
ua = UserAgent()
#print(ua.ie)
#print(ua.chrome)
#print(ua.random)


with requests.Session() as s :
    s.get(URL)
    LOGIN_INFO = {
        'identification' : 'tntndhrsu',
        'password' : 'dntkddls',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }
    print('token', s.cookies['csrftoken'])
    #요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})

    #html 결과 확인
    #print('response', response.text )

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text , 'html.parser')
        projectList = soup.select("div.user-project > div.body-3")
        print(projectList)
        for i in projectList:
            print(i.find('div.body-3').string, i.find('p.body-3-medium').text)
