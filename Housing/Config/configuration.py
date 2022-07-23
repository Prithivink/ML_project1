from Housing.util import get_yaml_file
import os
from Housing.Constant import *




class housingConfig:

    def __int__(self, config_file_path: CONFIG_FILE_PATH,current_time_stamp : CURRENT_TIME_STAMP ):
        self.config_info = get_yaml_file(config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp


    def get_data_ingestion_config(self):
        pass

    def get_data_validation_config(self):
        pass

    def get_data_transforamtion_config(self):
        pass

    def get_data_model_trainer_config(self):
        pass

    def get_data_model_evaluation_config(self):
        pass

    def get_data_model_pusher_config(self):
        pass

    def get_training_pipeline_config(self):
        pass