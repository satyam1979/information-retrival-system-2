import os
from pathlib  import Path
import logging 
logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')

list_of_files=[
                f"src/__init__.py",
                f"src/helper.py",
                ".env",
                "setup.py",
                "requirements.txt",
                "app.py",
                "research/trails.ipynb"

        ]


for filepath  in list_of_files:
    
    filepath =Path(filepath)
    
    filedir, filename =os.path.split(filepath)
    if filedir!="":
        
        os.makedirs(filedir, exist_ok=True)
        
        logging.info(f"Creating Directory, {filedir} for the file name : {filename}")
    
    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        
        with open(filepath,'w') as f:
            
            pass
            logging.info(f" {filename} is already exits.") 
        
        
