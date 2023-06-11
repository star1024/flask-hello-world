from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '楊馥禎趕快睡覺'
