import yaml
from Housing.Exception import HousingException
import os,sys

def get_yaml_file(file_path):

    try:
        with open(file_path,"r") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HousingException(e,sys) from e