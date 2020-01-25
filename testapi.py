# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:49:10 2020

@author: vismujum
"""

from flask import Flask,request,jsonify
#import joblib

app = Flask(__name__)

# This is example of Boot Strap API , where API is invoked at Root level
@app.route('/',methods=['GET'])
def root_method():
    result = {}
    result['status'] = 'This is example of Boot Strap API , API Is invoked at Root Level.'
    return jsonify(result)

# This is example of API, where API is invoked with Query Parameters
@app.route('/mclearning',methods=['GET'])
def query_param():
    firstParameter = request.args.get('firstName')
    print("Query Parameter , first parameter : ", firstParameter)
    secondParameter = request.args.get('secondName')
    print("Query Parameter , second Parameter : ", secondParameter)
    result = 'API is invoked with Query Parameters'
    result = {}
    result['status'] = 'API Is invoked with Query Parameters '
    result['first parameter'] = str(firstParameter) 
    result['second parameter'] = str(secondParameter)
    return jsonify(result)

# This is example of API ,where API is invoked with URI Parameters
#@app.route('/mclearning/param1/<int:param1>',methods=['GET'])
@app.route('/mclearning/firstName/<string:firstName>/secondName/<string:secondName>',methods=['GET'])
def url_param(firstName,secondName):
    print("URI Parameters , first parameter : ", firstName)
    print("URI Parameters , second parameter : ", secondName)
    firstParameter = firstName
    secondParameter = secondName
    result = {}
    result['status'] = 'API is invoked with URI Parameters.'
    result['first parameter'] = str(firstParameter) 
    result['second parameter'] = str(secondParameter) 
    return jsonify(result)

# This is example of API , where API is invoked with POST Request
@app.route('/mclearning' , methods=['POST'])
def post_data():
    data = request.get_json(force=True)
    print(data)
    firstParameter = data['first_parameter']
    secondParameter = data['second_parameter']
    print('First Parameter : <',firstParameter , '> , Second Parameter : <', secondParameter ,'>' )
    result = {}
    result['response'] = 'API Is invoked with POST Parameters '
    result['firstParameter'] = str(firstParameter) 
    result['secondParameter'] = str(secondParameter)
    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True,port=9000)