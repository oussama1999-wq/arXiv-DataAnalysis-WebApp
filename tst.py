def send():
    if request.method =='POST':
        age = request.form['age'] 
        r = requests.get('http://export.arxiv.org/api/query?search_query=all:'+age+'&start=0&max_results=10')
        xml = r.text
        doc=xmltodict.parse(xml)
        data = pd.DataFrame(doc)
        df=pd.DataFrame(data['feed']['entry'])
        dfa=df['author']
        dfs=df['summary']
        dft=df['title']
        dfc=df['category']
        dfp=df['published']
        dfu=df['updated']
        #dfk=df[['id','title']]
        names=[]
        for i in range (0,dfa.count()):
            if(type(dfa[i])==list):
                for j in range(0,len(dfa[i])):
                    names.append(dfa[i][j]['name'])
            else:
                names.append(dfa[i]['name'])
        def top10(var):
            dca={}
            for k in var:
                dca[k]=var.count(k)
                d2a = OrderedDict(sorted(dca.items(), key=lambda t: t[1],reverse=True))
                outa = json.loads(json.dumps(d2a))
            if(var ==names):
                dg=pd.DataFrame(outa.items(), columns=['Name', 'Nb of articles'])
            elif(var == catc):
                dg=pd.DataFrame(outa.items(), columns=['Category', 'Nb of occurence'])
            return dg.loc[ 0 : 9 ,:]
        #return render_template('age.html',age=doc)
        #time.sleep(10)
        return render_template('view.html',tables=[top10(names).to_html()], titles = ['na', 'Top'])
    #time.sleep(20)
    return render_template('index.html')
