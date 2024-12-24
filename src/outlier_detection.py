import logging
from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#setup logging configuration
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

#abstract base clss for Outlier Detection strategy
class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def detect_outliers(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        anstract method to detect outliers in the given dataframe

        parameters:
        df(pd.DataFrame):the dataframe containing features for outlier detection

        returns:
        pd.DataFrame:a boolean dataframe indicating where outliers are located
        '''
        pass

    #concrete strategy for Z-Score based outlier detection
class ZScoreOutlierDetection(OutlierDetectionStrategy):
        def __init__(self, threshold=3):
            self.threshold = threshold

        def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
            logging.info("Detecting outliers using the Z-Score method")
            z_scores=np.abs((df-df.mean())/df.std())
            outliers=z_scores>self.threshold
            logging.info(f"Outliers detected with z-score threshold:{self.threshold}")
            return outliers
        
    #concrete strategy for IQR bsed outlier detection
class IQROutlierDetection(OutlierDetectionStrategy):
        def detect_outliers(self,df:pd.DataFrame)->pd.DataFrame:
            logging.info("Detecting outliers using the IQR method")
            Q1=df.quantile(0.25)
            Q3=df.quantile(0.75)
            IQR=Q3-Q1
            outliers=(df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))
            logging.info("Outliers detected using the IQR method")
            return outliers
        
#context class for Outlier Detection and Handling
class OutlierDetector:
    def __init__(self,strategy:OutlierDetectionStrategy):
        self._strategy=strategy

    def set_strategy(self,strategy:OutlierDetectionStrategy):
        logging.info("switching outlier detection strategy")
        self._strategy=strategy
    
    def detect_outliers(self,df:pd.DataFrame)->pd.DataFrame:
        logging.info("executing outlier detection strategy")
        return self._strategy.detect_outliers(df)

    def handle_outliers(self,df:pd.DataFrame,method="remove",**kwargs)->pd.DataFrame:
        outliers=self.detect_outliers(df)
        if method=="remove":
            logging.info("removing outliers from the dataset")
            df_cleaned=df[(~outliers).all(axis=1)]
        elif method=="cap":
            logging.info("capping outliers in the dataset")
            df_cleaned=df.clip(lower=df.quantile(0.01),upper=df.quantile(0.99),axis=1)
        else:
            logging.warning(f"unknown method'{method}'.No oulier handling performed")
            return df
        logging.info("outlier handling ocmpleted")
        return df_cleaned

    def visualize_outliers(self,df:pd.DataFrame,features:list):
        logging.info(f"visualizing outlires for features:{features}")
        for feature in features:
            plt.figure(figsize=(10,6))
            sns.boxplot(x=df[feature])
            plt.title(f"Boxplot off {feature}")
            plt.show()
        logging.info("Outlier visualization completed")

#example usage
if __name__ == "__main__":
    # # Example dataframe
    df = pd.read_csv("C:/Users/Keerthi/Documents/AiMlasingh/extracted_data/AmesHousing.csv")
    df_numeric=df.select_dtypes(include=[np.number]).dropna()

    # Initialize the OutlierDetector with the Z-Score based Outlier Detection Strategy
    outlier_detector=OutlierDetector(ZScoreOutlierDetection(threshold=3))

    #detect and handle outliers
    outliers=outlier_detector.detect_outliers(df_numeric)
    df_cleaned=outlier_detector.handle_outliers(df_numeric,method="remove")

    print(df_cleaned.shape)
    #visualize outlires in specific features
    outlier_detector.visualize_outliers(df_cleaned,features=["SalePrice", "Gr Liv Area"])
    pass


#    SalePrice  Gr Liv Area
# 0     200000        1500
# 1     300000        2000
# 2     400000        2500
# 3     500000        3000
# 4    1000000        4000
# 5    2000000       10000


#    SalePrice  Gr Liv Area
# 0     200000        1500
# 1     300000        2000
# 2     400000        2500
# 3     500000        3000
# 4    1000000        4000
# 5    1000000        4000