import folium
import pandas

data = pandas.read_csv("Volcanoes.txt") #calls data from txt file
lon =list(data["LON"]) #adds lon column from txt file to list
lat =list(data["LAT"]) #adds lat column from txt file to list
loca =list(data["LOCATION"]) #set list of location info from txt file
elev =list(data["ELEV"]) #set list of elevation info from txt file

def get_color(elevation): #set elevation color based on elev list
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#funtcion used to return color as an alternative to using a lambda expression "lamda x: {'fillColor':'green' if x['properties']..."
def style_function(x):
     return {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}

map =folium.Map(location=[55.856973, -4.221154], zoom_start=6, tiles="Mapbox Bright") #start up location
fgv =folium.FeatureGroup(name="Volcanoes") #creates FeatureGroup

for lt, ln, el in zip(lat, lon, elev): #looping through 3 lists lat, lon, elev setting them to lt, ln, el
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius =6, popup="This Marker is located in " + "elevation numbers are " + str(el) + "m ",
    fill_color=get_color(el), color= 'grey', fill_opacity=0.7, fill=True)) #child class to create marker

fgp =folium.FeatureGroup(name="Population") #creates FeatureGroup

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=style_function))

map.add_child(fgv) #calls FeatureGroup - Volcanoes
map.add_child(fgp) #calls FeatureGroup - Population
map.add_child(folium.LayerControl()) #LayerControl box turn fg on and off **My Map FeatureGroup
map.save("Map1.html") #run once to save/update
