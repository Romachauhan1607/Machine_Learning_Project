from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup functions
def get_requirements_list()->List[str]:
    pass
PROJECT_NAME= "housing-predictor"
VERSION= "0.0.3"
AUTHOR= "RomaChauhan"
packages=["Housing"]
DESCRIPTION= "This is the fsds nov batch Machine Learning Project"
REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description= This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return  a list which contain name of libraries mentioned in the requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    
setup(
name=PROJECT_NAME,
version=VERSION,
author= AUTHOR,
packages=find_packages(),
description=DESCRIPTION,
install_requires=get_requirements_list()

)


