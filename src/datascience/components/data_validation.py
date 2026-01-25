import os
import pandas as pd
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            error_messages = []

            # 1️⃣ Read data
            data = pd.read_csv(self.config.unzip_data_dir)

            # 2️⃣ Column lists
            data_cols = set(data.columns)
            schema_cols = set(self.config.all_schema.keys())

            # 3️⃣ Missing columns
            missing_cols = schema_cols - data_cols
            if missing_cols:
                validation_status = False
                error_messages.append(f"Missing columns: {missing_cols}")

            # 4️⃣ Extra columns
            extra_cols = data_cols - schema_cols
            if extra_cols:
                validation_status = False
                error_messages.append(f"Extra columns: {extra_cols}")

            # 5️⃣ Data type validation
            for col, dtype in self.config.all_schema.items():
                if col in data.columns:
                    if str(data[col].dtype) != dtype:
                        validation_status = False
                        error_messages.append(
                            f"Datatype mismatch in column '{col}': expected {dtype}, got {data[col].dtype}"
                        )

            # 6️⃣ Null value check
            null_cols = data.columns[data.isnull().any()].tolist()
            if null_cols:
                validation_status = False
                error_messages.append(f"Null values found in columns: {null_cols}")

            # 7️⃣ Duplicate rows check
            if data.duplicated().sum() > 0:
                validation_status = False
                error_messages.append("Duplicate rows found")

            # 8️⃣ Empty dataset check
            if data.shape[0] == 0:
                validation_status = False
                error_messages.append("Dataset is empty")

            # 9️⃣ Write validation status
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validation_status: {validation_status}\n")
                for msg in error_messages:
                    f.write(msg + "\n")

            logger.info(f"Data validation completed with status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e
