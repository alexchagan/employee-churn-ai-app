# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:26:57 2022

@author: dorge
"""

# =============================================================================
# file operations lib 
# =============================================================================
#     filname:        logger.py
#     version:        1.0
#     author:         dorge
#     creation_date:  06-12-2022
#     
#     change history:
#     
#     who       when      version     changes
#     ----      -----     -------     --------
#     dorge      6-12-22   1.0         INIT
#
#   description: used to provide all file related functionality.
# =============================================================================
import os
import shutil
import pickle
from apps.core.logger import Logger

class FileOperations:
    
    
    
    def __init__(self,run_id,data_path,mode):
        self.run_id = run_id
        self.data_path = data_path
        self.logger = Logger(self.run_id, 'FileOperation', mode)
     
    def save_model(self,model,file_name):
        try:
            self.logger.info('Start of Save Models')
            path = os.path.join('apps/models/',file_name) #create seperate directory for each cluster
            if os.path.isdir(path): #remove previously existing models for each clusters
                shutil.rmtree('apps/models')
                os.makedirs(path)
            else:
                os.makedirs(path) #
            with open(path +'/' + file_name+'.sav','wb') as f:
                pickle.dump(model, f) # save the model to file
            self.logger.info('Model File '+file_name+' saved')
            self.logger.info('End of Save Models')
            return 'success'
        except Exception as e:
            self.logger.exception('Exception raised while Save Models: %s' % e)
            raise Exception()

    def load_model(self,file_name):
        """
        * method: load_model
        * description: method to load the model file
        * return: File gets saved
        *
        * who             when           version  change (include bug# if apply)
        * ----------      -----------    -------  ------------------------------
        * bcheekati       05-MAY-2020    1.0      initial creation
        *
        * Parameters
        *   file_name:
        """
        try:
            self.logger.info('Start of Load Model')
            with open('apps/models/' + file_name + '/' + file_name + '.sav','rb') as f:
                self.logger.info('Model File ' + file_name + ' loaded')
                self.logger.info('End of Load Model')
                return pickle.load(f)
        except Exception as e:
            self.logger.exception('Exception raised while Loading Model: %s' % e)
            raise Exception()

    def correct_model(self,cluster_number):
        """
        * method: correct_model
        * description: method to find best model
        * return:  The Model file
        *
        * who             when           version  change (include bug# if apply)
        * ----------      -----------    -------  ------------------------------
        * bcheekati       05-MAY-2020    1.0      initial creation
        *
        * Parameters
        *   cluster_number:
        """
        try:
            self.logger.info('Start of finding correct model')
            self.cluster_number= cluster_number
            self.folder_name='apps/models'
            self.list_of_model_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if (self.file.index(str( self.cluster_number))!=-1):
                        self.model_name=self.file
                except:
                    continue
            self.model_name=self.model_name.split('.')[0]
            self.logger.info('End of finding correct model')
            return self.model_name
        except Exception as e:
            self.logger.info('Exception raised while finding correct model' + str(e))
            raise Exception()