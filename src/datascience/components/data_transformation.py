import os
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

from sklearn.model_selection import train_test_split
import logging

logger = logging.getLogger(__name__)

class DataTransformation:
    def __init__(self, config):
        self.config = config

        """ Nite : You can add data transformation technique such as scaler , PCA and all
         you can perform all kind of EDA in ML cycle here beppore passing this data to model 
        
         I am only adding train_test_split coz this data is already cleanup
        """

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split data into train and test (75%, 25%)
        train, test = train_test_split(
            data,
            test_size=0.25,
            random_state=42
        )

        train.to_csv(
            os.path.join(self.config.root_dir, "train.csv"),
            index=False
        )
        test.to_csv(
            os.path.join(self.config.root_dir, "test.csv"),
            index=False
        )

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
