import pandas as pd
from src.feature_engineering import(
    FeatureEngineer,
    LogTransformation,
    MinMaxScaling,
    OneHotEncoding,
    StandardScaling,
)
from zenml import step

@step
def feature_engineering_step(
    df:pd.DataFrame,strategy:str="log",
    features=list
)->pd.DataFrame:
    '''
    performs featire engineering using FeatureEngineer and selected strategy
    '''
    #ensure features is a list,even if not provided
    if features is None:
        features = []#or raise and error if features are requires
    if strategy=="log":
        engineer=FeatureEngineer(LogTransformation(features))
    elif strategy == "standard_scaling":
        engineer = FeatureEngineer(StandardScaling(features))
    elif strategy == "minmax_scaling":
        engineer = FeatureEngineer(MinMaxScaling(features))
    elif strategy == "onehot_encoding":
        engineer = FeatureEngineer(OneHotEncoding(features))
    else:
        raise ValueError(f"Unsupported feature engineering strategy: {strategy}")

    transformed_df = engineer.apply_feature_engineering(df)
    return transformed_df
    