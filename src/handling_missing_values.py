import logging
from abc import ABC,abstractmethod

import pandas as pd

#setup logging configuration-print,ln bcoz in zenml some dont have
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")



#abstract base class for missing value handling strategy
class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        abstarct method to handle mssing values in the dataframe

        parameters;
        df(pd.DataFrame):The input dataframe containing missing values

        returns:
        pd.DataFrame:the dataframe with missing values handled
        '''
        pass

#cocrete strategy for dropping missing values
class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self,axis=0,thresh=None):#to drop rows
        '''
        intializes the DropMissingValuesStrategy with specific parameters

        parameters:
        axis(int):0 to drop rows with missing values,1 to drop cols
        thresh(int):the threshold for non-NA values,rows/columns
        '''

        self.axis=axis
        self.thresh=thresh
        
    def handle(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        drops rows or cols with missing values based on the 
        parameters;
        df(pd.DataFrame):The input dataframe containing missing values

        returns:
        pd.DataFrame:the dataframe with missing values handled
        '''
        logging.info(f"Dropping missing values with axis={self.axis} and thresh={self.thresh}")
        df_cleaned=df.dropna(axis=self.axis,thresh=self.thresh)
        logging.info("missing values dropped")
        return df_cleaned


#concrete strategy for filling missing values
class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self,method="mean",fill_value=None):
        '''
        intializes the FillMissingValuesStrategy with a specific method

        parameters:
        method(Str):the method to fill missing values('mean','median,mode)
        fill_value(any):the constant value to fill missing values 
        '''
        self.method=method
        self.fill_value=fill_value

    def handle(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        fills missing vlaues using the specified method or constr

        paramters:
        df(pd.DataFrame):the input dataframe containing missing values
        
        returns:
        pd.DataFrame:the dataframe with missing values handled
        '''
        logging.info(f"Dropping missing values with axis={self.method}")
        df_cleaned=df.copy()
        if self.method=="mean":
            numeric_columns=df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns]=df_cleaned[numeric_columns].fillna(
                df[numeric_columns].mean()
            )

        elif self.method=="median":
            numeric_columns=df_cleaned.select_dtypes(include="number").col
            df_cleaned[numeric_columns]=df_cleaned[numeric_columns].fillna(
                df[numeric_columns].median()
            )
        elif self.method=="mode":
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df[column].mode().iloc[0],inplace=True)
        elif self.method=="constant":
            df_cleaned[column].fillna(self.fill_value)
        else:
            logging.warning(f"Unknown method '{self.method}'.No missing values handled")

        logging.info("Missing values filled.")
        return df_cleaned

#context class for handling missing vlaues
class MissingValueHandler:
    def __init__(self,strategy:MissingValueHandlingStrategy):
        '''
        intializes the MissingValueHandler witha a sepcific missing values
        
        parameters;
        strategy(MissingValueHandlingStrategy):The type of startegy to handle missing values
        '''
        self.strategy=strategy
    def set_strategy(self,strategy:MissingValueHandlingStrategy):
        '''
        sets a new strategy for the MissingValueHandler

        strategy(MissingValueHandlingStrategy):The type of startegy to handle missing values
        '''

        logging.info("switching missing values handling strategies")
        self._strategy=strategy

    def handle_missing_values(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        executes the missing value handling using the cureent strategy

        paramters:
        df(pd.DataFrame):the input dataframe containing missing values
        
        returns:
        pd.DataFrame:the dataframe with missing values handled
        '''
        logging.info(f"executing missing value handling stategy")
        return self.strategy.handle(df)

#example usage
if __name__=="__main__":
    #load the data
    df=pd.read_csv("C:/Users/Keerthi/Documents/AiMlasingh/extracted_data/AmesHousing.csv")
    

    #initialize missing value handler with a specific strategy
    missing_value_handler=MissingValueHandler(DropMissingValuesStrategy(axis=0,thresh=None))
    df_cleaned=missing_value_handler.handle_missing_values(df)

    #swtich to filling missing values with mean
    missing_value_handler.set_strategy(FillMissingValuesStrategy(method='mean'))
    df_filled=missing_value_handler.handle_missing_values(df)












    
        
