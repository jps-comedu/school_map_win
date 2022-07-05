import pandas as pd
import folium

filePath=r'고등학교_주소_좌표.xlsx'
df_from_excel = pd.read_excel(filePath, engine='openpyxl', header=None)
# 판다스로 엑셀 파일 읽어오기 / 우리가 만든 엑셀 파일은 헤더 파일이 없음 -> header=None

df_from_excel.columns = ['학교이름', '주소', 'x', 'y'] # columns 이름

# '학교이름', '주소', 'x', 'y' 값을 각각 리스트 형태로 가져옴
name_list = df_from_excel['학교이름'].to_list() # 학교이름
addr_list = df_from_excel['주소'].to_list() # 주소
position_x_list = df_from_excel['x'].to_list() # 경도
position_y_list = df_from_excel['y'].to_list() # 위도

map = folium.Map(location=[37, 127], zoom_start=7) # 기본맵 설정

for i in range(len(name_list)):
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i], position_x_list[i]], 
                               popup=name_list[i], 
                               icon = folium.Icon(color='blue'))
        # 마커 지정 -> 위도, 경도 / 팝업 -> 학교명 / 아이콘 지정
        marker.add_to(map) # 마커 추가

map.save(r'hs_map_all.html') # html 파일로 저장