import pandas as pd
from zenml import step

import sys
import os

# Add the src folder to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now you can import the module
from handling_missing_values import (
    DropMissingValuesStrategy,
    FillMissingValuesStrategy,
    MissingValueHandler
    )  # Replace with actual function or class

# Use the function or class as needed
MissingValueHandler(FillMissingValuesStrategy)


@step
def handle_missing_values_step(df:pd.DataFrame,strategy:str="mean")->pd.DataFrame:
    '''
    handles missing values using MissingValueHandler and the specified strategy
    '''
    if strategy=="drop":
        handler=MissingValueHandler(DropMissingValuesStrategy(axis=0))

    elif strategy in ["mean","median","mode","constant"]:
        handler=MissingValueHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling stratgy:{strategy}")

    cleaned_df=handler.handle_missing_values(df)
    return cleaned_df
