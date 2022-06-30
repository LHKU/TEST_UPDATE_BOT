import telegram
from cgitb import text
from tkinter import N
import requests
from bs4 import BeautifulSoup

import datetime

import urllib.request

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')


my_token = '5337479883:AAFi4A8Qimb67JVdiFuaDjbp5JRpMCn0OIM'
Room_ID = "5007202751"
bot = telegram.Bot(token=my_token)


url = 'https://docs.microsoft.com/en-us/windows-insider/flight-hub/#windows-10-may-2021-update-21h1'


response = requests.get(url)


first_date = datetime.datetime.today().strftime("%#m/%#d/%Y")
# 아래 주석 코드는 날짜 비교 테스트용 (업데이트 날짜)
# first_date = datetime.datetime(2022, 6, 2).strftime("%#m/%#d/%Y")


try:
    response.status_code == 200
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    div = soup.select_one('.content > :nth-child(14)')
    titles = div.select(
        'table > tbody > tr:nth-child(1) > td:nth-child(2) > a')

    for title in titles:
        # href로 링크가져오기 https://wikidocs.net/142389 참조
        href = title.attrs['href']

        if first_date == title.get_text():
            text_msg = title.get_text() + '\n' + "- 업데이트가 있습니다." + '\n' + \
                "- URL을 확인해주세요." + '\n''\n' + href
            print(text_msg)
            bot.sendMessage(chat_id=Room_ID, text=text_msg)

        else:
            text_msg = "업데이트가 없습니다."
            print(text_msg)
            bot.sendMessage(chat_id=Room_ID, text=text_msg)

except:
    text_msg = "오류발생! 내부소스코드나 URL을 점검해주세요."
    print(text_msg)
    bot.sendMessage(chat_id=Room_ID, text=text_msg)
