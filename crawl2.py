import requests
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')


url = 'https://docs.microsoft.com/en-us/windows-insider/flight-hub/#windows-10-may-2021-update-21h1'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    div = soup.select_one('.content > :nth-child(14)')
    titles = div.select('table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    
    for title in titles:
        print(title.get_text())
else : 
    print(response.status_code)