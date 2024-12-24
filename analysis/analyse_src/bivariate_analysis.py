from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#abstarct base class for Bivariate Analysis strategy
#---------------------------------------------------
#this class defines a common interface for bivariate analysis strategies
#subclasses must implement the analyze method

class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self,df:pd.DataFrame,feature1:str,feature2:str):
        '''perform bivariate analysis on two features of the dataframe

           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature1(Str):the name of the first feature/column to be analyzed
           feature2(Str):the name of the second feature/column to be analyzed

           returns:
           None:this method visualizes the relationship between the features
           '''
        pass


#concrete strategy for numerical features
#-----------------------------------------
#this strategy analyzes numerical features by plotting their distribution

class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self,df:pd.DataFrame,feature1:str,feature2:str):
        '''plotd the relationship between two numerical features using a scatter plot

           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature1(Str):the name of the first numerical feature/column to be analyzed
           feature2(Str):the name of the second numerical feature/column to be analyzed
           
           returns:
           None:Displays a scatter plot showing the realtionship between
           '''
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=feature1,y=feature2,data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

#concrete strategy for categorical vs numerical features
#-----------------------------------------
#this strategy analyzes the relationship between a categorical and numerical features by plotting their distribution

class CategoricalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self,df:pd.DataFrame,feature1:str,feature2:str):
        '''plotd the relationship between a categorical and numerical features using a box plot

           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature1(Str):the name of the categorical feature/column to be analyzed
           feature2(Str):the name of the numerical feature/column to be analyzed
           
           returns:
           None:Displays a box plot showing the realtionship between
           '''
        plt.figure(figsize=(10,6))
        sns.boxplot(x=feature1,y=feature2,data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()

#context class that uses a BivariateAnalysisStrategy
#--------------------------------------------------------
#this class allows you to switch between different bivariate an
class BivariateAnalyzer:
    def __init__(self,strategy:BivariateAnalysisStrategy):
        '''Initializes the BivariateAnalyzer with a specific analysis strategy

           parameters:
           strategy(BivariateAnalysisStrategy):the strategy to be analysed
           
           returns:
           None
        '''
        self._strategy=strategy

    def set_strategy(self,strategy:BivariateAnalysisStrategy):
        '''
           sets a new strategy fpr the bivarirateAnalyzer

           parameters:
           strategy(BivariateAnalysisStrategy):the strategy to be analysed

           returns:
           None
           '''
        self._strategy=strategy

    def execute_analysis(self,df:pd.DataFrame,feature1:str,feature2:str):
        '''executes the bivariate analysis using the curretn strategy

           
           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature1(Str):the name of the first feature/column to be analyzed
           feature2(Str):the name of the second feature/column to be analyzed
           
           returns:
           None:Executes the strategy's analysis and visual
           '''
        self._strategy.analyze(df,feature1,feature2)

#example usage
if __name__=="__main__":
    #example usage of the bivariate with differnet strategy

    #load the data
    df = pd.read_csv('C:/Users/Keerthi/Downloads/prices-predictor-system/prices-predictor-system/extracted_data/AmesHousing.csv')


    #analyzing realtionship between two numerical features
    analyzer=BivariateAnalyzer(NumericalVsNumericalAnalysis())
    analyzer.execute_analysis(df,'Gr Liv Area','SalePrice')

    #analyzig the relationship bewtween a categorical and a numerical features
    analyzer.set_strategy(CategoricalVsNumericalAnalysis())
    analyzer.execute_analysis(df,'Overall Qual','SalePrice')

    pass










































        
