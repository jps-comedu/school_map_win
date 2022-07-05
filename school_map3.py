import pandas as pd
import requests
from openpyxl import load_workbook
from openpyxl import Workbook
import re

# 엑셀 파일 불러오기 및 정리 / school_map.py
filePath = r'고등학교 하반기 주소록(2021).xlsx'
df_from_excel = pd.read_excel(filePath, engine='openpyxl')
df_from_excel.columns = df_from_excel.loc[2].tolist()
df_from_excel = df_from_excel.drop(index=list(range(0,3)))

# API 접속 관련 내용 / school_map2.py
url= 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&vision=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD' #도로명 주소
road_type2 = 'PARCEL' #지번 주소
address = '&address='
keys = '&key='
primary_key = 'D09B6606-FC2D-369B-97B3-11EC2A2D30B8' # 발급 받은 인증키 입력

# 주소를 x, y좌표로 반환해주는 함수 -> API에 접속하여 x, y 부분만 분리하여 반환 / school_map2.py
def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        x = 0
        y = 0
        return x, y

# 주소를 좌표로 변경 -> 고등학교_주소_좌표.xlsx 파일에 저장
highschool_list = df_from_excel['학교명'].to_list()
address_list = df_from_excel['도로명주소'].to_list()

wb = Workbook()
sheet = wb.active
     
for num, value in enumerate(address_list):
    addr = value
    print(addr)
    x, y = request_geo(addr) # API를 활용하여 주소를 좌표로 변환
    sheet.append([highschool_list[num], addr, x, y]) # 학교명, 주소, x, y의 순서대로 엑셀에 저장
    
wb.save(r"고등학교_주소_좌표.xlsx")