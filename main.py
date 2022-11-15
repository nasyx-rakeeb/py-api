from flask import Flask, jsonify, request 
import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

today = datetime.date.today()

year = today.year
month = today.month
day = today.day

solar = Solar(year, month, day)
lunar = Converter.Solar2Lunar(solar)

lunarYear = lunar.year 
lunarMonth = lunar.month
lunarDay = lunar.day

app = Flask(__name__) 

@app.route('/', methods=['GET']) 

def helloworld(): 

    if(request.method == 'GET'): 

        data = {"lunar_year": lunarYear, "lunar_month": lunarMonth, "lunar_day": lunarDay} 

        return jsonify(data) 

if __name__ == '__main__': 

    app.run(debug=false) 
