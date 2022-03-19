from cProfile import label
from configparser import ConfigParser
from turtle import bgcolor 
import requests 
from tkinter import *
from tkinter import messagebox 
  
config_file = "config.ini"
config = ConfigParser() 
config.read(config_file) 
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'+"&lang="+"sp"
  
  
def getweather(city): 
    result = requests.get(url.format(city, api_key)) 
      
    if result: 
        json = result.json() 
        city = json['name'] 
        country = json['sys'] 
        temp_kelvin = json['main']['temp'] 
        temp_celsius = int(temp_kelvin-273.15)
        weather1 = json['weather'][0]['main'] 
        final = [city, country, temp_kelvin,  
                 temp_celsius, weather1] 
        return final 
    else: 
        print("Contenido no encontrado") 
  
  
def search(): 
    city = city_text.get() 
    weather = getweather(city) 
    if weather: 
        location_lbl['text'] = f'{weather[0]} '
        temperature_label['text'] = str(weather[3])+"  C°"
        weather_l['text'] = weather[4] 
    else: 
        messagebox.showerror('Error', "No encontrado {}".format(city)) 
  
  
app = Tk() 
app.title("Weather App") 
app.geometry("300x300" )
app.config(bg="#00FDFF")




city_text = StringVar() 
label_Relleno =Label(app,text="",bg="#00FDFF")
label_Relleno.pack() 
city_entry = Entry(app, textvariable=city_text) 
city_entry.pack() 
label_Relleno =Label(app,text="",bg="#00FDFF")
label_Relleno.pack() 
Search_btn = Button(app, text="Buscar",  
                    width=12, command=search) 
Search_btn.pack() 
label_Relleno =Label(app,text="-------------------" ,bg="#00FDFF")
label_Relleno.pack() 
location_lbl = Label(app, text="Localizacion", font={'bold', 30} ,bg="#00FDFF")
location_lbl.pack() 

label_Relleno =Label(app,text="-------------------",bg="#00FDFF")
label_Relleno.pack() 

temperature_label = Label(app, text="Temperatura",bg="#00FDFF",font={'bold', 30, }) 
temperature_label.pack() 

label_Relleno =Label(app,text="-------------------",bg="#00FDFF")
label_Relleno.pack() 

weather_l = Label(app, text="Clima", bg="#00FDFF",font={'bold', 30}) 
weather_l.pack() 
app.mainloop() 
