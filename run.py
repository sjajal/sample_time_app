from flask import Flask
from datetime import datetime
import pytz
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    return datetime_NY.strftime("%H:%M:%S")
    


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
