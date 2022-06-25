import requests
from bs4 import BeautifulSoup

import datetime

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')


url = 'https://docs.microsoft.com/en-us/windows-insider/flight-hub/#windows-10-may-2021-update-21h1'

response = requests.get(url)


first_date = datetime.datetime.today().strftime("%#m/%#d/%Y")
# 아래 주석 코드는 날짜비교 테스트용
# first_date = datetime.datetime(2022, 6, 2).strftime("%#m/%#d/%Y")


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    div = soup.select_one('.content > :nth-child(14)')
    titles = div.select('table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    
    for title in titles:
        
        if first_date == title.get_text() :
            print(title.get_text() + " 날짜로 업데이트가 있습니다.")
        else :
            print("업데이트가 없습니다.")    
        
else : 
    # URL에서 200(정상)을 반환하지 않으면 해당 에러코드를 반환하도록 함
    print("response.status_code" + " 에러")
    

