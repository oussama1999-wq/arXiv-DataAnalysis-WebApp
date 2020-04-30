from flask import Flask,render_template,request
from collections import OrderedDict
import requests
import xmltodict
import pandas as pd
import time
app = Flask(__name__)


@app.route('/send',methods=['GET','POST'])
def send():
    if request.method =='POST':
        age = request.form['age']
        r20=""
        for i in age:
            if i == ' ':
                r20 = r20 +'%20'
            else:
                r20 = r20 + i 
        r = requests.get('http://export.arxiv.org/api/query?search_query=all:'+r20+'&start=0&max_results=10')
        xml = r.text
        doc=xmltodict.parse(xml)
        data = pd.DataFrame(doc)
        df=pd.DataFrame(data['feed']['entry'])
        return render_template('view.html',tables=[df.to_html()], titles = ['na', 'Dataframe'])
    #time.sleep(20)
    return render_template('index.html')

if __name__ =='__main__':
    app.debug = True
    app.run()