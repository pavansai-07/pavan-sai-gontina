from flask import Flask, render_template
app = Flask(__name__)
import psutil
import ctypes
from turtle import *
from geopy.geocoders import Nominatim
import folium
from branca.element import Figure

@app.route('/')
def index():
  return render_template('app.component.html')

@app.route('/time/')
def time():
    import datetime
    x=str(datetime.datetime.now())
    return x
@app.route('/battery/')   
def battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    return percent
@app.route('/cd/')    

def cd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    ctypes.windll.WINMM.mciSendStringW(u"open D: type cdaudio alias d_drive", None, 0, None)
    ctypes.windll.WINMM.mciSendStringW(u"set d_drive door open", None, 0, None)
    return "done"
@app.route('/heart/')
def heart():
    def curvemove():
        for i in range(200):
            right(1)
            forward(1)
    color('black','pink')       
    begin_fill()
    left(140)
    forward(111.65)
    curvemove()
    left(120)
    curvemove()
    forward(111.65)
    end_fill()
    done()
    return "0"
@app.route('/speak/')    
def speech():
    import pyttsx3
    e=pyttsx3.init()
    def audio(output):
        e.say(output)
        e.runAndWait()
    audio("Hello pavan sai")  

@app.route('/location/')
def map():
    address=input()
    geolocator = Nominatim(user_agent="Pavan Sai")
    location = geolocator.geocode(address)
    a=location.latitude
    b=location.longitude
    print(a,b)
    m=folium.Map(location=[a,b],tiles='cartodbdark_matter',zoom_start=16)
    fig=Figure(width=550,height=350).add_child(m)
    folium.Marker(location=[a,b],popup='Nakkapalli city',tooltip='Click here to see Popup').add_to(m)
    m

if __name__ == '__main__':
  app.run(debug=True)