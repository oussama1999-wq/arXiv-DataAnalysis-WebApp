from flask import Flask,render_template,request
from collections import OrderedDict
from pandas import DataFrame
import requests
import xmltodict    
import pandas as pd
import time
import json


app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('123.html')
@app.route('/hello')
def hello():
    return render_template('123.html')

#@app.route('/',methods=['POST'])
#def my_form_post():
 #   text = request.form['u']
 #   processed_text = text.upper()
 #   return processed_text
#print(my_form_post())
if __name__ =='__main__':
    app.debug = False
    app.run(port=5002)
