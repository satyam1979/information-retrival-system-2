import os
from pathlib import Path
import logging

#logging.basicConfig(Level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files=[
"src/__int__.py",
"src/helper.py",
".env",
"requirements.txt",
"setup.py",
"app.py",
"research/trails.ipynb",
]

for filepath in list_of_files:
    filepath =Path(filepath)
    filedir, filename =os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directy ;{filedir} for the file name  {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath , "w") as f:
            pass
            logging.info(f"Create Emplty file: {filepath}")

    else :
        logging.info(f"File name {filename}  is already exist")

