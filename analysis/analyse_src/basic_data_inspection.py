from abc import ABC,abstractmethod
import pandas as pd

#abstract base class for data inspection strategies
#This classs defines a common interface for data inspcetion strategies
#subclasses must implement the
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self,df:pd.DataFrame):
        ''' Perform a specific type of data inspection

            Parameters:
            df(pd.DataFrame):The datafrae on which the inspection is to be performed.

            Returns:
            None:This method prints the inspection directly
            '''
        pass


#concrete strategy for data types inspection
#this strategy inspects the data types of each column and count
    
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        '''Inspects and prints the data types and noon-null counts
        parameters:s
        df(pd.DataFrame):The dataframe to be inspected.

        Returns:
        None:Prints the data types and non null counts to the
        '''
        print("\n Data Types and Non-null Counts:")
        print(df.info())

#concrete strategy for summary statistics inpsection
#this strategy provides summary statistics for both numerical and categorical
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        '''prints summary statistics for numerical and categorical

           Parameters:
           df(pd.DataFrame):The dataframe to be inspected

           Returns:
           None:Prints summary statistcs to the console.'''

        print("\n Summary statistics (Numerical Features):")
        print(df.describe())
        print("\n Summary statistics (Categorical Features):")
        print(df.describe(include=["0"]))



#context class that uses a DataInspectionStrategy
#This class allows you to switch between different data inspect
class DataInspector:
    def __init__(self,strategy:DataInspectionStrategy):
        '''Initializes the DataInspector with a specific inspection strategy

           parameters:
           strategy(DataInspectionStrategy):The strategy to be used for data inspection

           returns:
           None'''

        self._strategy=strategy

    def set_strategy(self,strategy:DataInspectionStrategy):
        '''sets a new strategy for the DataInspcetor

           parameters:
           strategy(DataInspectionStrategy):The strategy to be used for data inspection

           returns:
           None'''

        self._strategy=strategy

    def execute_inspection(self,df:pd.DataFrame):
        '''executes the inspection using the current strategy

           parameters:
           df(pd.DataFrame):The dataframe to be inspected.

           Returns:
           None:Executes the strategy's inspection method
           '''
        self._strategy.inspect(df)
        
#example usage
if __name__=="__main__":
    #example usage of the DataInspector with different strategies

    #load the data
    df=pd.read_csv('C:/Users/Keerthi/Downloads/prices-predictor-system/prices-predictor-system/extracted_data/AmesHousing.csv')

    
    #intialize the data inspector with a specific strategy
    '''inspector=DataInspector(DataTypesInspectionStrategy())
    inspector.execute_inspection(df)'''

    
    #change strategy to summary statistics and execute
    inspector=DataInspector(DataTypesInspectionStrategy())
    inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    inspector.execute_inspection(df)

    pass













        
