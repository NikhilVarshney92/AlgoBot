import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject"

list_of_files=[
    f"src/common/__init__.py",
    f"src/common/exception.py",
    f"src/common/logger.py",
    f"src/common/utils.py",
    f"src/components/__init__.py",
    f"src/components/data_cleaning.py",
    f"src/components/data_preprocessing.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/pipelines/__init__.py",
    f"src/pipelines/training_pipeline.py",
    f"src/pipelines/prediction_pipeline.py",
    f"templates/style/home.css",
    f"templates/pages/home.html",
    f"logs/_.log",
    f"artifacts/data/_.csv",
    f"artifacts/images/_.jpg",
    "app.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")