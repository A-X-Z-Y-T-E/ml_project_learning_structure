from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr , _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_array=train_arr, test_array=test_arr))