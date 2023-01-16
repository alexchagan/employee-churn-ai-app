from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
import pickle
import sklearn
import joblib
import os
from os.path import dirname as up
import sys;print(sys.version)


app = Flask(__name__)
CORS(app, support_credentials=True)

def json_to_numpy(json_req):
    '''Turns a dict reperesnting a json into a numpy array.
    
    Parameters
    ----------
    json_req : dict
        A dict representing a json from client side response  
    
    Returns
    ----------
    values_np : numpy_array
        A converted numpy array
    '''
    values_arr = [0]
    (_ ,values_dict), = json_req.items()
    for key ,value in values_dict.items():
        values_arr.append(transform_value(key,value))   
    values_np = np.array(values_arr)
    print ('values_np', values_np)
    values_np = np.reshape(values_np, (1,len(values_np)))
    return values_np

def transform_value(key, value):
    '''Turns a value from the client response and transforms it to a new value 
    fitting for the model's use.
    
    Parameters
    ----------
    key : string
        A dict representing a json from client side input
    value : int   
    
    Returns
    ----------
    A transformed value 
    '''
    match key:
        case 'satisfaction_level':
            return value/100
        case 'last_evaluation':
            return value/100
        case 'number_project':
            return float(value)
        case 'average_monthly_hours':
            return float(value)
        case 'time_spend_company':
            return float(value)
        case 'work_accident':
            return float(value)
        case 'promotion_last_5year':
            return float(value)
        case 'salary':
            return float(value)
       

def predict(np_array):
    dir = up(up(up(__file__)))
    model_path = os.path.join(dir, 'save_dicts/xgb.pkl')
    model = joblib.load(model_path , mmap_mode=None)
    pred = model.predict(np_array)
    print(pred)
    pred = pred[0]  
    if pred == 0:
        test_result = "not leave"
    else:
        test_result = "leave"
    return test_result



@app.route("/api/", methods=['POST', 'GET'])
def get_answers():
    if request.method == 'POST':
        print('post app')
        req = request.json
        values_np = json_to_numpy(req)
        
        result = predict(values_np)

        return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)