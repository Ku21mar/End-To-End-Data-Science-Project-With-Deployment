from setuptools import setup,find_packages
from typing import List 


#define the varaibale 

PROJECT_NAME = "Machine Learning Projects"
VERSION ="0.0.1"
DESCRIPTION = "This is our machine learning project in modular coding"
AUTHOR_NAME ='Kuamr Abhishek'
AUTHOR_EMAIL ="dummy@successanalytics.ai"


REQUIREMENT_FILE_NAME ="requirements.txt"

HYPEN_E_DOT = "-e ."
# 1. open Requirement.txt file 
# 2. read the Requirement file inside
# 3.(pandas\n )replace the \n with empty " "

def get_requirements_list()->List[str]: 
    #ye list of sring define krega
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list =[requirement_name.replace("\n", "") for requirement_name in requirement_list]


        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)

        return requirement_list

# abhi jo setup fle jo create kiye hain es ab install karna hai
#  @ toh installl krne keliye humare passs command hota hai 
# [ -e . ] hum log add kre es command ko ane reuirement.txt file ke andar 
# aone setup file ko install krne keliye 


#!/usr/bin/env python

# from distutils.core import setup


setup(name= PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages= find_packages(),
      install_requires = get_requirements_list()
     )


# setup(name='Distutils',
#       version='1.0',
#       description='Python Distribution Utilities',
#       author='Greg Ward',
#       author_email='gward@python.net',
#       url='https://www.python.org/sigs/distutils-sig/',
#       packages=['distutils', 'distutils.command'],
#      )




