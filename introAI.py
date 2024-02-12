from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    name = request.args.get("name", default="None")
    return name

