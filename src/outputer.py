import os
import pandas as pd

def outputer(file, file_path):
    if not isinstance(file, pd.DataFrame):
        raise ValueError("The input file in outputer should be a dataframe.")
    if not isinstance(file_path, str):
        raise ValueError("The file path should be a string.")
    if not os.path.isdir(os.path.dirname(file_path)):
        raise ValueError("The file path is invalid.")
    file.to_csv(file_path, index=False)