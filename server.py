from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)
api_key = "013ebb50b7a6ead82cd07ae120b5b96f

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return " Antonio Enciso ".

@app.route('/api/weather',methods=['POST'])
def weather():
    #get data from js request 
    lat = request.json['lat']
    lon = request.json['lon']
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (
        lat, lon, api_key)


    #call openweather api
    response = requests.get(url)
    print(response)
    data = json.loads(response.text)
    return data 

if __name__== '__main__':
    app.run(debug = True)