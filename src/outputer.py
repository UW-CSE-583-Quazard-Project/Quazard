'''
This is the outputer module used to output a csv file.
'''
import os
import pandas as pd

def outputer(file, file_path):
    '''
    This function takes a dataframne and a file path to output a csv file.
    Parameters:
    - file: Dataframe from upstream
    - file_path: The path to output the csv file.
    '''
    if not isinstance(file, pd.DataFrame):
        raise ValueError("The input file in outputer should be a dataframe.")
    if not isinstance(file_path, str):
        raise ValueError("The file path should be a string.")
    if not os.path.isdir(os.path.dirname(file_path)):
        raise ValueError("The file path is invalid.")
    file.to_csv(file_path, index=False)