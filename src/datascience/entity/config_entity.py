from dataclasses import dataclass
from pathlib import Path



## config for data ingestion
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
## config for data validation
@dataclass 
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict    
    
    
## config for data transformation

@dataclass 
class DataTransformationConfig:
    root_dir: Path
    data_path: Path  
    
    
    
## cinfig for model trainer

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path : Path
    test_data_path : Path
    model_name: str
    
    alpha: float     ## these 3 parameter use for elasticnet regularization towards using elasticnet in this have 2 parameter 
    l1_ratio: float
    target_column: str
          