import folium
import pandas
import statistics

map = folium.Map(location=[30.553757,-97.834881],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

dataframe = pandas.read_csv("U.S._Chronic_Disease_Indicators__CDI_.csv",dtype="object")
#we can use the below loop, however the number of questions is 202, unless its a web based interaction
#No point in showing all 202
#for the purpose of demonstrating interactive capability, limiting the question list to two questions
#question_list=list(set(dataframe["Question"]))
#print(len(question_list))
#for q in question_list:
#    print(q)
question_list=['Q1:Alcohol use among youth','Q2:Current cigarette smoking among youth']
#list of questions is what we want user to iterate through
#so we will set that as an index of the dataframe, so filtering through it is faster
dataframe=dataframe.set_index(['Question'])#sets this as the index
#to make it interactive, we need to display distinct list of questions. so we will create a list and display that to user
for q in question_list:
    print(q)


question_selection=input("Select a question from above to plot states. enter Q1 or Q2: ").lower()
if question_selection=='q1':
    question_input='Alcohol use among youth'
elif question_selection=='q2':
    question_input='Current cigarette smoking among youth'
else:
    question_input='None'

#dataframe=dataframe.loc['Alcohol use among youth']
if question_input!='None':
    dataframe=dataframe.loc[question_input]

    cutoff_input=float(input("Any threshold you wish to supply. Enter 0 if none: "))
    #dataframe=dataframe.loc[(dataframe['DataValue'].astype(float)>32) & (dataframe['YearStart'].astype(int)==2015)]
    dataframe=dataframe.loc[(dataframe['DataValue'].astype(float)>=cutoff_input) & (dataframe['YearStart'].astype(int)==2015)]

    geo_location_list=list(dataframe["GeoLocation"])
    data_value_list=list(dataframe["DataValue"])
    state_value_list=list(dataframe["LocationDesc"])
    latitude_list=[]
    longitude_list=[]

    #the below block will help us change the color of marker
    dv_min=min(float(s) for s in data_value_list)
    dv_max=max(float(s) for s in data_value_list)
    dv_mean=statistics.mean(float(s) for s in data_value_list)

    print(dv_min)
    print(dv_max)
    print(dv_mean)

    def markup_color_generator(value):
        if value>=dv_min and value<=dv_mean:
            return 'orange'
        elif value>dv_mean and value<=dv_max:
            return 'red'

    for location in geo_location_list:
        if type(location)==str:
            latitude=float(location.replace("(","").replace(")","").split(",")[0])
            longitude=float(location.replace("(","").replace(")","").split(",")[1])
            latitude_list.append(latitude)
            longitude_list.append(longitude)

    #latitude_list_top=latitude_list[:104]
    #longitude_list_top=longitude_list[:104]
    for lt,ln,st,dv in zip(latitude_list,longitude_list,state_value_list,data_value_list):
        fg.add_child(folium.Marker(location=[lt,ln],popup=st+" "+str(dv),icon=folium.Icon(color=markup_color_generator(float(dv)))))

    print(len(latitude_list),"States")
    #print(len(longitude_list))
    map.add_child(fg)
    map.save("Map1.html")
else:
    print("select valid input next time")
