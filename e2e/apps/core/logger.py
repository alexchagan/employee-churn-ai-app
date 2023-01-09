# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:03:02 2022

@author: dorge
"""


# =============================================================================
# Logger file 
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
#   description: this class used to generate logs in logs files.
# =============================================================================

import logging

class Logger:
    def __init__(self, run_id, module, log_file_name):
        """
        Generate logs.
        Parameters
        ----------
        run_id : string
            unique process ID.
        module : string
            name of module which sends a log.
        logfile_name : string
            'training' or 'predicting'.
        Returns
        -------
        None.
        """
        
        # get relevent logger instant and set the level to debug.
        self.logger=logging.getLogger(str(module)+'_' + str(run_id))
        self.logger.setLevel(logging.DEBUG)
        
        # check if it a log of training or predicting procedure.
        if log_file_name=='training':
            file_handler = logging.FileHandler('logs/training_logs/train_log_' + str(run_id) + '.log')
        
        else:
            file_handler = logging.FileHandler('logs/prediction_logs/predict_log_' + str(run_id) + '.log')
        
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def info(self,message):
        # write information log
        self.logger.info(message)
    
    def exception(self,message):
        # write exception log
        self.logger.exception(message)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    