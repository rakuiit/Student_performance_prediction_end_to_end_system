from flask import Flask,request,render_template
import pandas as pd
import numpy as pd 

app=Flask(__name__)


## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',method=['GET','POST'])
def predict_datapoint():
    


# if __name__ == '__main__':
#     app.run(debug=True)




