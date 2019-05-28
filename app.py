import requests, json,request
from requests import *
from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/results', methods= ['GET','POST'])
def results():

    if request.method == 'POST':
        api_key = 'AIzaSyDjtomKygWFv6WcCnkPaSXEoQOI4L7JtZw'

        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        query = request.form['loc']
        loc= query
        r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)
        x = r.json()
        y = x['results']

        for i in range(len(y)):
            res = y[i]['name']

        return render_template("res.html",li=y, l=len(y),s='name',loc=loc)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug='True')
