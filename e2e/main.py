# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:55:05 2022

@author: dorge
"""
# IMPORT DEPENDECIES:
from flask import Flask, request, render_template
from flask import Response
from flask_cors import CORS, cross_origin
from wsgiref.simple_server import make_server

# IMPORT INTERNAL LIBS
from apps.core.config import Config
from apps.training.train_model import TrainModel


app = Flask(__name__)
CORS(app)


@app.route('/training', methods=['POST'])
@cross_origin()
def training_route_client():
    config=Config()
    run_id=config.get_run_id()
    data_path=config.training_data_path
    # trainModel init
    train_model=TrainModel()
    
    try:
        return Response("Training succesfully!")
    except ValueError:
        return Response("Error Occured! %s" % ValueError)
    except KeyError:
        return Response("Error Occured! %s" % KeyError)
    except Exception as e:
        return Response("Error Occured! %s" % e)
        
        
        
if __name__=="__main__":
    # app.run()
    host='0.0.0.0'
    port=5000
    httd=make_server(host,port,app)
    httd.serve_forever()
    
        