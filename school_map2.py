import requests

# API 접속 관련 내용
url= 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&vision=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD' #도로명 주소
road_type2 = 'PARCEL' #지번 주소
address = '&address='
keys = '&key='
primary_key = 'D09B6606-FC2D-369B-97B3-11EC2A2D30B8' # 발급 받은 인증키 입력

# 주소를 x, y좌표로 반환해주는 함수 -> API에 접속하여 x, y 부분만 분리하여 반환
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

# 주소 입력 -> x, y값 출력
x, y = request_geo("서울 종로구 종로58길 28 (숭인동, 종로산업정보학교)")

print(f'x값: {x}')
print(f'y값: {y}')