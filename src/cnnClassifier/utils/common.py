import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file.
    
        Args: path_to_yaml (str): path to yaml file
        
        Raises: 
            ValueError: if file is empy
            e: empty file
            
        Returns:
            ConfigBox: ConfigBox type
    """
    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories.

    Args:
        path_to_directories (list): list of paths to directories
        ignore_log (bool, optional): ignore if multiple dirs are to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """Saves json data.

        Args:
            path_to_json (Path): path to json file
            data (dict): data to be saved in json file
    """ 
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f'json file saved at: {path_to_json}')

@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """Load data from json file.

        Args:
            path_to_json (Path): path to json file

        Returns:
            ConfigBox: data as class attributes
    """
    with open(path_to_json) as f:
        content = json.load(f)

    logger.info(f'json file loaded successfully from: {path_to_json}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary file.

        Args:
            data (Any): data to be saved as binary file
            path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)

    logger.info(f'binary file saved at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file.

        Args:
            path (Path): path to binary file

        Returns:
            Any: object stored in file
    """
    data = joblib.load(path)

    logger.info(f'binar file loaded from: {path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB.
    
        Args:
            path (Path): path to file
            
        Returns:
            str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'

def decode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encode_image_base64(imgpath):
    with open(imgpath, 'rb') as f:
        return base64.b64encode(f.read())