import os
import sys
from pathlib import Path
import logging


while True:
    preoject_name = input('Enter your project name')
    if preoject_name != '':
        break

logging.baseConfig(
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s] %(message)s"
)

list_of_files = [
    f"{preoject_name}/__init__.py",
    f"{preoject_name}/components/__init__.py",
    f"{preoject_name}/config/__init__.py",
    f"{preoject_name}/constant/__init__.py",
    f"{preoject_name}/entity/__init__.py",
    f"{preoject_name}/exception/__init__.py",
    f"{preoject_name}/logger/__init__.py",
    f"{preoject_name}/pipline/__init__.py",
    f"{preoject_name}/utils/__init__.py",
    "config/config.yaml",
    "setup.py",
    "main.py"
    "requirement.txt"
    "demo.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir !='':
        os.mkdir(filedir,exist_ok=True)
        logging.info(f"creating new directoy at :{filedir} for file: {filename}")
    if( not os.path.exists(file_path)) or (os.path.getsize(filename) == 0):
        with open(file_path, w) as f:
            pass
            logging.info(f"creating new file {filename} at :{filedir}")
    else:
        logging.info(f"file {filename} already present at :{filedir}")
        
 
