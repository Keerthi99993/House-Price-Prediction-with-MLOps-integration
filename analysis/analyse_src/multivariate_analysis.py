from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#abstarct base class for Multivariate Analysis 
#---------------------------------------------------
#this class defines a template for Multivariate analysis strategies
#subclasses must implement specific steps like correlation heatmap

class MultivariateAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):
        '''perform comprehensive multivariate analysis on two features of the dataframe

           parameters:
           df(pd.DataFrame):The dataframe containing the data to be analyzed

           returns:
           None:this method orchestrates the multivariate analysis relationship 
           '''
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)
    @abstractmethod
    def generate_correlation_heatmap(self,df:pd.DataFrame):
        '''
           generate and display a heatmap of the correaltions betweeen

           parameters:
           df(pd.DataFrame):The dataframe containing the data to be analyzed

           returns:
           None:this method should generate and display a correaltion
           '''
        pass
    
    @abstractmethod
    def generate_pairplot(self,df:pd.DataFrame):
        '''
           generate and display a pair plot of the correaltions betweeen

           parameters:
           df(pd.DataFrame):The dataframe containing the data to be analyzed

           returns:
           None:this method should generate and display a correaltion
           '''
        pass
            

#concrete strategy for Multivariate analysis with correaltion heatmap
#---------------------------------------------------------------------
#this class implements the methods to generate a correlation heatmap

class SimpleMultiVariateAnalyzer(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self,df:pd.DataFrame):
        '''Generates and displays a correaltion heatmap for the numerical

           parameters:
           df(pd.DataFrame):The dataframe containing the data to be analyzed
           
           returns:
           None:Displays a heatmap showing correaltions between num
           '''
        plt.figure(figsize=(12,10))
        sns.heatmap(df.corr(),annot=True,fmt=".2f",cmap="coolwarm",linewidth=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    def generate_pairplot(self,df:pd.DataFrame):
        '''
           generates and displays a pair plot for the selected feature

           
           parameters:
           df(pd.DataFrame):The dataframe containing the data to be analyzed
           
           returns:
           None:Displays a pair plot for the selected features
           '''
        sns.pairplot(df)
        plt.subtitle("Pair plot of selelcted features",y=1.02)
        plt.show()

#example usage
if __name__=="__main__":
    #example usage of the SimpleMultivariateAnalysis class

    #load the data
    df = pd.read_csv('C:/Users/Keerthi/Downloads/prices-predictor-system/prices-predictor-system/extracted_data/AmesHousing.csv')

    # Perform Multivariate Analysis
    multivariate_analyzer = SimpleMultivariateAnalysis()

    # Select important features for pair plot
    selected_features = df[['SalePrice', 'Gr Liv Area', 'Overall Qual', 'Total Bsmt SF', 'Year Built']]

    # Execute the analysis
    multivariate_analyzer.analyze(selected_features)
    
    pass
















        
        
