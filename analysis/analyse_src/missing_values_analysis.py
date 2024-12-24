from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#abstract base class for missing values analysis
#-----------------------------------------------
#this class defines a template for missing values anaysis
#subclasses must implement the mthods to identify and visualize
class MissingValuesAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):
        ''' Performs a complete missing values analysis by identifying

        parameters:
        df(pd.DataFrame):The dataframe to be analyzed

        returns:
        None:this method performs the analysis and visualizes'''
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self,df:pd.DataFrame):
        '''Identifies missing values in the data frame

        parameters:
        df(pd.DataFrame):The dataframe to be analyzed

        returns:
        None:this method should print the count of missing values'''
        pass
    
    @abstractmethod
    def visualize_missing_values(self,df:pd.DataFrame):
        '''visualizes missing values in the data frame

        parameters:
        df(pd.DataFrame):The dataframe to be visualized

        returns:
        None:this method should create a visualization(e.g.,'''
        pass


#concrete class for missing values identification
#--------------------------------------------------
#This class implements methods to identify and visualize missing values
class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
        
    def identify_missing_values(self,df:pd.DataFrame):
        '''prints the count of missing values for each column in the

        parameters:
        df(pd.DataFrame):The dataframe to be analyzed

        returns:
        None:prints the missing values count to the console'''
        print("\nMissing values count by column:")
        missing_values=df.isnull().sum()
        print(missing_values[missing_values>0])


    def visualize_missing_values(self,df:pd.DataFrame):
        '''Creates a heatmap to visualize the missing values in the data frame

        parameters:
        df(pd.DataFrame):The dataframe to be visualized

        returns:
        None:Displays a heatmap of missing values'''
        print("\nVisualizing missing values...")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cbar=False,cmap="viridis")
        plt.title("Missing vlaues Heatmap")
        plt.show()


#example usage
if __name__=="__main__":
    #example usage of the SimpleMissingValuesAnalysis class

    #load the data
    df=pd.read_csv('C:/Users/Keerthi/Downloads/prices-predictor-system/prices-predictor-system/extracted_data/AmesHousing.csv')

    #perform missingvlaues analysis
    missing_values_analyzer=SimpleMissingValuesAnalysis()
    missing_values_analyzer.analyze(df)

    











    
    
