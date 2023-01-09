# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:12:13 2022

@author: dorge
"""

# =============================================================================
# This script will hold the configuration class
# =============================================================================
#     filname:        config.py
#     version:        1.0
#     author:         dorge
#     creation_date:  06-12-2022
#     
#     change history:
#     
#     who       when      version     changes
#     ----      -----     -------     --------
#     dorge      6-12-22   1.0         INIT
# =============================================================================
    
import random
from datetime import datetime
class Config:
    
    def __init__(self):
        self.training_data_path='data/training_data'
        self.training_database = 'training'
        self.prediction_data_path = 'data/prediction_data'
        self.prediction_database = 'prediction'
        
    def get_run_id(self):
        """
        gives a unique key value "run_id" for logging purposes.
        Returns
        -------
        string: unique run id for request.
        """
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H%M%S%N")
        return str(self.date)+"_"+str(self.current_time)+"_"+str(random.randint(1000000, 9999999))
        
    
    
