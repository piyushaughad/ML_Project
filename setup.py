from setuptools import find_packages,setup
from typing import List

Hypen_E_DOT = '-e .'

def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readline()
        [req.replace("\n","") for req in requirments]

        if Hypen_E_DOT in requirments:
            requirments.remove(Hypen_E_DOT)

    return requirments

setup(
name='ML_project',
version='0.0.1',
author='Piyush',
author_email='piyushaghadgmail.com',
packages=find_packages(),
install_requires=get_requirments('requirments.txt')

)