# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:59:48 2021

@author: jglob
"""
import server
from flask import Flask, request, jsonify
import warnings 
warnings.filterwarnings('ignore')

app = Flask(__name__)
    
@app.route('/classify_image',methods = ['GET','POST'])
def classify_image():
    print(request.form)
    image_data = request.form['image_data']
    champion = server.make_prediction(image_data)
    response = jsonify(champion)  
    response.headers.add('Access-Control-Allow-Origin','*')
    
    print(champion)
    return  response
    
    
if __name__ =='__main__':
    print('starting server')
    app.run(port=5000)