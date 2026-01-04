import os
import yaml
import json
import joblib

from src.datascience import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        FileNotFoundError: if file not found

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml}loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")

    except Exception as e:
        raise e
    
    
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}") 
    
    
    
@ensure_annotations
def load_json(path: Path) -> dict:
    """
    Load json data

    Args:
        path (Path): path to json file

    Returns:
        dict: data loaded from json file
    """
    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return content

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: loaded binary object
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data        
                   
