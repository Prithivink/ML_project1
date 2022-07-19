from setuptools import setup,find_packages


#declaring the setup functions
NAME = "Housing price prediction"
VERSION = "0.0.2"
AUTHOR = "Prithivi"
DESCRIPTION = "this is first CICD included project"
PACKAGE = "housing"
REQUIREMENT_FILE = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements():
    """"
    This function will return all the requirement libraries
    needed for setup
    """
    with open(REQUIREMENT_FILE)  as req:
        requirement_list = req.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        requirement_list.remove(HYPHEN_E_DOT)

setup(
name = NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements())