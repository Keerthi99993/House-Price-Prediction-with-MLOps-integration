from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#abstarct base class for Univariate Analysis strategy
#---------------------------------------------------
#this class defines a common interface for univariate analysis strategies
#subclasses must implement the analyze method

class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self,df:pd.DataFrame,feature:str):
        '''perform univariate analysis on a specific feature of the dataframe

           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature(Str):the name of the feature/column to be analyzed

           returns:
           None:this method visualizes the distribution of the feature
           '''
        pass


#concrete strategy for numerical features
#-----------------------------------------
#this strategy analyzes numerical features by plotting their distribution

class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self,df:pd.DataFrame,feature:str):
        '''plotd the distribution of a numerical feature using a histogram and KDE

           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature(Str):the name of the numerical feature/column to be analyzed

           returns:
           None:Displays a histogram with a KDE plot
           '''
        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)#kernel density estimate
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


#concrete strategy for categorical features
#-----------------------------------------
#this strategy analyzes categorical features by plotting their distribution
class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self,df:pd.DataFrame,feature:str):
        '''plotd the distribution of a categorical feature using a bar plot

           parameters:
           df(pd.DataFrame):The dataframe containing the data
           feature(Str):the name of the categorical feature/column to be analyzed

           returns:
           None:Displays a barplot showing the frequency of each category
           '''
        plt.figure(figsize=(10,6))
        sns.countplot(x=feature,data=df,palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()


# Context Class that uses a UnivariateAnalysisStrategy
# ----------------------------------------------------
# This class allows you to switch between different univariate analysis strategies.
class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        """
        Initializes the UnivariateAnalyzer with a specific analysis strategy.

        Parameters:
        strategy (UnivariateAnalysisStrategy): The strategy to be used for univariate analysis.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        """
        Sets a new strategy for the UnivariateAnalyzer.

        Parameters:
        strategy (UnivariateAnalysisStrategy): The new strategy to be used for univariate analysis.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Executes the univariate analysis using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature (str): The name of the feature/column to be analyzed.

        Returns:
        None: Executes the strategy's analysis method and visualizes the results.
        """
        self._strategy.analyze(df, feature)


# Example usage
if __name__ == "__main__":
    # Example usage of the UnivariateAnalyzer with different strategies.

    # Load the data
    df = pd.read_csv('C:/Users/Keerthi/Downloads/prices-predictor-system/prices-predictor-system/extracted_data/AmesHousing.csv')

    # Analyzing a numerical feature
    analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
    analyzer.execute_analysis(df, 'SalePrice')

    # Analyzing a categorical feature
    analyzer.set_strategy(CategoricalUnivariateAnalysis())
    analyzer.execute_analysis(df, 'Neighborhood')
    
    pass











        