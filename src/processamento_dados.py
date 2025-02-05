import pandas as pd
import os
from typing import Dict, List, Any, Sequence
from sklearn.preprocessing import LabelEncoder

def load_data(filepath: str, sep: str = ';'):
    return pd.read_csv(filepath)

def treats_null_values(dataframe, dict: Dict['str', 'Any']):
    for key, value in dict.items():
        dataframe.fillna({key: value}, inplace=True)
    return dataframe

def rename_columns(dataframe: pd.DataFrame, cols: Dict['str', 'str'])-> pd.DataFrame:
    return dataframe.rename(columns=cols)

def create_column(dataframe: pd.DataFrame, column_name: str, data: Sequence[Any]) -> pd.DataFrame:
    if isinstance(data, pd.Series):
        dataframe[column_name] = data.reindex(dataframe.index)
    else:
        dataframe[column_name] = pd.Series(data, index=dataframe.index)
    return dataframe


def remove_columns(dataframe: pd.DataFrame, cols: List['str']) -> pd.DataFrame:
    return dataframe.drop(columns=cols)

def encode_categorical(dataframe: pd.DataFrame, col: str) -> pd.DataFrame:
    label_encoder = LabelEncoder()
    encode = col+'_encode'
    dataframe[encode] = label_encoder.fit_transform(dataframe[col])
    return dataframe

def remove_outliers(dataframe: pd.DataFrame, cols: List['float']) -> pd.DataFrame:
    for col in cols:
        Q1 = dataframe[col].quantile(0.25)
        Q3 = dataframe[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        dataframe = dataframe[(dataframe[col] >= lower) & (dataframe[col] <= upper)]
    return dataframe

def save_dataframe_csv(dataframe: pd.DataFrame, name: str):
    path = os.path.join('..','data')
    type = 'csv'
    path_file = f"{path}/{name}.{type}"
    dataframe.to_csv(path_file, index=False)
    
    
