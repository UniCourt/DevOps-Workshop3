import sys
from datetime import datetime
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    user_ip = request.headers.get('X-Real-IP')
    data_message = "Welcome to the FindMyIP!"
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current datetime


    return render_template('welcome.html', user_ip=user_ip, data_message=data_message, current_datetime=current_datetime)


if __name__ == '__main__':
    app.run("0.0.0.0", int(sys.argv[1]))
