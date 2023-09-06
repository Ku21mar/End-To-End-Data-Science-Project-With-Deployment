#  here we are going to write the complete script 

# importing important library
import os
from pathlib import Path 
# logging ko bhi import krlete ho agar inbetween agar error hota h agar aapp log store krna chahte to
# to aap usko bhi store kr skte hai 
import logging  


while True:
    project_name =input("enter your project name ")
    if project_name != "":
        break

#  list of file and list of folder ko define krege
# thik h ki aapko apne project keliye kaun kaun sa file chahiye adn kaun kaun sa floder chahiye 


# src/__init_.py
#  src/component/__init_.py
list_of_files = [
    f"{project_name}/__init_.py",
    f"{project_name}/component/__init_.py",
    f"{project_name}/config/__init_.py",
    f"{project_name}/entity/__init_.py",
    f"{project_name}/exception/__init_.py",
    f"{project_name}/logger/__init_.py",
    f"{project_name}/pipeline/__init_.py",
    f"{project_name}/utlis/__init_.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"

]

# ab humlog FOR LOPP define karege so that for loop ke help se humlog kya krege
# apne file lo split karege and split karne ke bad humlog complete folder and file lo humlog generate karege


# why we are spliting the file?
# hum log yaha split esliye krte ha jo bhu es SRC file ke andar jo bhi compnonet file associate ha wo 
# alag split ho jayeg agar foler me hai toh  
  
#    f"{project_name}/__init_.py",
    # f"{project_name}/component/__init_.py",
    # f"{project_name}/config/__init_.py",
    # f"{project_name}/entity/__init_.py",


for filepth in list_of_files:
    filepath =Path(filepth)
    # define the two variable file directory and file name
    filedir ,filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass

    else:
        logging.info("file is already present at :{filepath}")






