import logging
from abc import ABC,abstractmethod
import pandas as pd

from sklearn.model_selection import train_test_split

#setup logging configuration
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

#abstract base class for data splitting strategy
#------------------------------------
#this class defines a common interface for different data splitting strategies
#subclasses must implement the split_data method
class DataSplittingStrategy(ABC):
    @abstractmethod
    def split_data(self,df:pd.DataFrame,target_column:str):
        '''
        abstract method to split the data training and testing sets

        parameters:
        df(pd.DataFrame):the input dataframe to be split 
        target_column(str):the name of the target column

        returns:
        X_train,X_test,y_train,y_test :the training and testing splits for features and target
        '''
        pass

#concrete strategy for single Train-Test splt 
#-------------------------
#this class implements a simple train-test split strategy
class SimpleTrainTestSplitStrategy(DataSplittingStrategy):
    def __init__(self,test_size=0.2,random_state=42):
        """
        Initializes the SimpleTrainTestSplitStrategy with specific parameters.

        Parameters:
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): The seed used by the random number generator.
        """
        self.test_size=test_size
        self.random_state=random_state
    
    def split_data(self,df:pd.DataFrame,target_column:str):   
        """
        Splits the data into training and testing sets using a simple train-test split.

        Parameters:
        df (pd.DataFrame): The input DataFrame to be split.
        target_column (str): The name of the target column.

        Returns:
        X_train, X_test, y_train, y_test: The training and testing splits for features and target.
        """
        logging.info("performing simple train-test split")
        X=df.drop(columns=[target_column])
        y=df[target_column]
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=self.test_size,random_state=self.random_state)
        logging.info("Train-test split completed")
        return X_train,X_test,y_train,y_test

#context class for Data splitting
#-------------------------------
#this class uses a DataSplittingStrategy to split the data
class DataSplitter:
    def __init__(self,strategy:DataSplittingStrategy):
        '''
        Initializes the DataSplitter with a specific data splitting strategy.

        Parameters:
        strategy (DataSplittingStrategy): The strategy to be used for data splitting.
        '''
        self._strategy=strategy

    def set_strategy(self,strategy:DataSplittingStrategy):
        '''
        Sets a new strategy for the DataSplitter.

        Parameters:
        strategy (DataSplittingStrategy): The new strategy to be used for data splitting.
        '''
        logging.info("switching data splitting strategy")
        self._strategy=strategy

    def split(self,df:pd.DataFrame,target_column:str):
        """
        Executes the data splitting using the current strategy.

        Parameters:
        df (pd.DataFrame): The input DataFrame to be split.
        target_column (str): The name of the target column.

        Returns:
        X_train, X_test, y_train, y_test: The training and testing splits for features and target.
        """
        logging.info("splitting data using the selected strategy")
        return self._strategy.split_data(df,target_column)
# Example usage
if __name__ == "__main__":
    # Example dataframe (replace with actual data loading)
    df=pd.read_csv('extracted_data/AmesHousing.csv')

    #initalize data splitter with a specific strategy
    data_splitter=DataSplitter(SimpleTrainTestSplitStrategy(test_size=0.2,random_state=42))

    X_train,X_test,y_train,y_test=data_splitter.split(df,target_column='SalePrice')