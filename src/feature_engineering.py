import logging
from abc import ABC,abstractmethod

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder,StandardScaler

#setup logging configuration
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

#abstract base class for feature engineering strategy
#-----------------------------------------------------
#this class defines a common interface for different feature engineering strategies
#subclasses must implement the apply_transformation method
class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        Abstract method to apply feature engineering transmation strategy

        Parameters:
        df(pd.DataFrame):The dataframe containing features to transform

        returns:
        pd.DataFrame:A dataframe with the applied transformations
        '''
        pass

#concrete strategy for Log Transformation
#---------------------------------------------
#This strategy applies a logarithmic transformation to skewed features to normalize the distribution.
class LogTransformation(FeatureEngineeringStrategy):
    def __init__(self,features):
        '''
        Initializes the LogTransforamtion with the specific features to transform

        Parameters:
        features(list):the list of features to apply the log transformation to. 
        '''
        self.features=features
    
    def apply_transformation(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        applies a log transformation to the specified features in the dataframe

        Parameters:
        df(pd.DataFrame):The dataframe containing featurs to transform

        Returns:
        pd.DataFrame:the dataframe with log-transformed feature
        '''
        logging.info(f"Applying log transformed feature:{self.features}")
        df_transformed=df.copy()
        for feature in self.features:
            df_transformed[feature]=np.log1p(
                df[feature]
            )#log1p handles log{0} by calculating log(1+x)
        logging.info("Log transformation completed")
        return df_transformed

#concrete strategy for Standard Scaling
#--------------------------------------
#This strategy applies standard scaling(z-score normalization)
class StandardScaling(FeatureEngineeringStrategy):
    def __init__(self,features):
        '''
        Initializes the StandardScaling with the specific features to scale

        Parameters:
        features(list):The list of features to apply the Standard Scaling to.
        '''
        self.features=features
        self.scaler=StandardScaler()
        
    def apply_transformation(self, df:pd.DataFrame)->pd.DataFrame:
        '''
        Applies standard scaling to the specified features in the DataFrame

        Parameters:
        df(pd.DataFrame):the dataframe containing features to transform

        Returns:
        pd.DataFrame:the dataframe with scaled features
        '''
        logging.info(f"Applying standard scaling to features:{self.features}")
        df_transformed=df.copy()
        df_transformed[self.features]=self.scaler.fit_transform(df[self.features])
        logging.info("Standard sclaing completed")
        return df_transformed
    
#concrete strategy for Min-Max Scaling
#--------------------------------------
#This strategy applies Min-Max scaling to features,scaling them to a specif range,typically [0,1]
class MinMaxScaling(FeatureEngineeringStrategy):
    def __init__(self,features,feature_range=(0,1)):
        '''
        Initializes the MinMaxScaling with the specific features

        Parameters:
        features(list):The list of features to apply the Min-Max Scaling to scale and target range

        parameters:
        feature(list):the list of features to apply the Min-Max scaling to
        feature_range(tuple):the target range for scaling,default is (0,1) 
        '''
        self.features=features
        self.scaler=MinMaxScaler(feature_range=feature_range)

    def apply_transformation(self, df:pd. DataFrame)->pd.DataFrame:
        '''
        Apploes Min-Max scaling to the specified features in the DataFrame

        parameters:
        df(pd.DataFrame):the dataframe containing faeatures to trandform

        returns:
        pd.DataFrame:the dataframe with Min-Max scaled features
        '''
        logging.info(f"Applying Min-Max scaling to features:{self.features} with range {self.scaler.feature_range}")
        df_transformed=df.copy()
        df_transformed[self.features]=self.scaler.fit_transform(df[self.features])
        logging.info("Min-Max scaling completed")
        return df_transformed
    
#concrete strategy for One-Hot Encoding
#-----------------------------------------
#this strategy applies One-Hot Strategy to categorical features
class OneHotEncoding(FeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initializes the OneHotEncoding with the specific features to encode.

        Parameters:
        features (list): The list of categorical features to apply the one-hot encoding to.
        """
        self.features = features
        self.encoder = OneHotEncoder(sparse=False, drop="first")

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        applies one-hot encoding to the specified categorical features in the dataframe

        parameters:
        df(pd.DataFrame):the dataframe containing features to transform

        returns:
        pd.Dataframe:the dataframe with one-hot encoding features
        '''
        logging.info(f"Applying One-hot encoding to features:{self.features}")
        df_transformed=df.copy()
        encoded_df=pd.DataFrame(
            self.encoder.fit_transform(df[self.features]),
            columns=self.encoder.get_feature_names_out(self.features)
        )
        df_transformed=df_transformed.drop(columns=self.features)
        df_transformed=pd.concat([df_transformed,encoded_df],axis=1)    
        logging.info("One-hot encoding completed")
        return df_transformed

#context class for feature engineering
#-------------------------------------------
#this class uses a FeatureEngineeringStrategy to apply transformations to a  dataset
class FeatureEngineer:
    def __init__(self,strategy:FeatureEngineeringStrategy):
        '''
        Initializes the FeatureEngineer with a sepecific feature engineering strategy

        Parameters:
        strategy(FeatureEngineeringStrategy):the strategy to be used for feature engineering
        '''
        self._strategy=strategy
    
    def set_strategy(self,strategy:FeatureEngineeringStrategy):
        '''
        sets a new strategy for the FeatureEngineer

        parameter:
        strategy(FeatureEngineeringStrategy):the new strategy to be used for feature engineering
        '''
        logging.info("Switching feature engineering strategy")
        self._strategy=strategy
    def apply_feature_engineering(self,df:pd.DataFrame)->pd.DataFrame:
        '''
        executes the feature engineering transformation using the current strategy

        parameters:
        df(pd.DataFrame):the dataframe containing features to transform

        returns:
        pd.DataFrame:the dataframe with applied feature engineering transformations
        '''
        logging.info("Applying feature engineering strategy")
        return self._strategy.apply_transformation(df)
    
#example usage
if __name__=="__main__":
    #example dataframe
    df=pd.read_csv('extracted_data/AmesHousing.csv')

    #log transformation example
    log_transformer=FeatureEngineer(LogTransformation(features=['SalePrice', 'Gr Liv Area']))
    df_log_transformed=log_transformer.apply_feature_engineering(df)

    #standard scaling example
    standard_scaler=FeatureEngineer(MinMaxScaling(features=['SalePrice', 'Gr Liv Area'], feature_range=(0, 1)))
    df_standard_scaled=standard_scaler.apply_feature_engineering(df)

    #Min-Max Scaling Example
    minmax_scaler=FeatureEngineer(MinMaxScaling(features=['SalePrice', 'Gr Liv Area'], feature_range=(0, 1)))
    # df_minmax_scaled = minmax_scaler.apply_feature_engineering(df)

    # One-Hot Encoding Example
    onehot_encoder = FeatureEngineer(OneHotEncoding(features=['Neighborhood']))
    df_onehot_encoded = onehot_encoder.apply_feature_engineering(df)

    pass
















