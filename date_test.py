import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')


import datetime

# strftime으로 날짜형식 변경하여 맞췄다. "월,일,년 형식"
first_date = datetime.datetime.today().strftime("%#m/%#d/%y")
second_date = datetime.datetime(2022, 6, 20).strftime("%#m/%#d/%y")

# first_date와 second_date 출력
print(first_date)
print(second_date)

# true, false로 출력
print(first_date == second_date)


# if, else 문으로 확인, import sys와 io로 인코딩처리 후 한글로 실행 됨
if first_date == second_date:
    print("같습니다")

else :
    print("다릅니다")
    
    