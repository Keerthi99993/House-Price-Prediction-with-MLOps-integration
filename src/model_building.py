import logging
from abc import ABC,abstractmethod
from typing import Any

import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#setup logging configuration
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

#abstract base class for model builfing strategy
class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self,X_train:pd.DataFrame,y_train:pd.Series)->RegressorMixin:
        '''
        Abstract method to build and train a model.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        RegressorMixin: A trained scikit-learn model instance.
        '''
        pass

#concrete strategy for linear regression using scikit-learn
class LinearRegressionStrategy(ModelBuildingStrategy):
    def build_and_train_model(self,X_train:pd.DataFrame,y_train:pd.Series)->Pipeline:
        '''
        Builds and trains a linear regression model using scikit-learn.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        Pipeline: A scikit-learn pipeline with a trained Linear Regression model.
        '''
        #ensure the inputs are of the correct type
        if not isinstance(X_train,pd.DataFrame):
            raise TypeError("X_train must be a pandas dataframe")
        if not isinstance(y_train,pd.DataFrame):
            raise TypeError("y_train must be a pandas Series")
        logging.info("initializing Linear Regression model with scaling")

        #creating a pipeline with stranard scaling and linear regression
        Pipeline=Pipeline(
            [
                ("scaler",StandardScaler()),#feature scaling
                ("model", LinearRegression()),  # Linear regression model
            ]
        )
        logging.info("training Linear Regression model")
        pipeline.fit(X_train,y_train)#fit the pipeline to the training model

        logging.info("model training complete")
        return pipeline
    
#context class for model building
class ModelBuilder:
    def __init__(self,strategy:ModelBuildingStrategy):
        '''
        initalizes the ModelBuilder with a specific model building strategy

        parameters:
        strategy (ModelBuildingStrategy): The strategy to use for model building
        '''
        self._strategy=strategy
    def set_strategy(self,strategy:ModelBuildingStrategy):
        '''
        Sets a new strategy for the ModelBuilder.

        Parameters:
        strategy (ModelBuildingStrategy): The new strategy to be used for model building.
        '''
        logging.info("switching model building strategy")
        self._strategy=strategy
    def build_model(self,X_train:pd.DataFrame,y_train:pd.Series)->RegressorMixin:
        """
        Executes the model building and training using the current strategy.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        RegressorMixin: A trained scikit-learn model instance.
        """
        logging.info("building and training the model using the selected strategy")
        return self._strategy.build_and_train_model(X_train,y_train)

#example usage
if __name__ == "__main__":
    # Example DataFrame (replace with actual data loading)
    df = pd.read_csv("extracted_data/AmesHousing.csv")
    x_train=df.drop(columns=['target_column'])
    y_train=df['target_column']

    #example usage of Linear Regression Strategy
    model_builder = ModelBuilder(LinearRegressionStrategy())
    trained_model = model_builder.build_model(X_train, y_train)
    print(trained_model.named_steps['model'].coef_)  
    # Print model coefficients

    pass


