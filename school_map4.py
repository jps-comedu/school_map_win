import folium

map = folium.Map(location=[37, 127], zoom_start=7)

marker = folium.Marker([37.572428376, 127.017221997], popup='종로산업정보학교', icon = folium.Icon(color='blue'))

marker.add_to(map)

map.save(r'hs_map.html')