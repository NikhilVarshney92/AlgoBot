import os
from flask import Flask,request,render_template
import pandas as pd


app=Flask(__name__)
## Route for a home page

@app.route('/')
def index():
    return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0", debug = True)        

