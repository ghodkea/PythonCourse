import folium
import pandas

map = folium.Map(location=[30.553757,-97.834881],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("U.S._Chronic_Disease_Indicators__CDI_.csv",dtype="object")
#print(data)
#print(data.columns)
geo_location=list(data["GeoLocation"])
latitude_list=[]
longitude_list=[]
for location in geo_location:
    if type(location)==str:
        latitude=float(location.replace("(","").replace(")","").split(",")[0])
        longitude=float(location.replace("(","").replace(")","").split(",")[1])
        latitude_list.append(latitude)
        longitude_list.append(longitude)
        #fg.add_child(folium.Marker(location=[latitude,longitude],popup="Hi I am a marker",icon=folium.Icon(color='green')))
latitude_list_top10=latitude_list[:100]
longitude_list_top10=longitude_list[:100]
for lt,ln in zip(latitude_list_top10,longitude_list_top10):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Hi I am a marker",icon=folium.Icon(color='green')))

#print(len(latitude_list))
#print(len(longitude_list))
map.add_child(fg)
map.save("Map1.html")
