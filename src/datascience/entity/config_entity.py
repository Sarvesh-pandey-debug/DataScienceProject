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