"""
This is module asks the user for their working directory (must contain
their raw .csv file from Qualtrics). This module also contains a 
function for reading the raw Qualtrics file (.csv) into a pandas 
dataframe. This allows for further processing by Quazard.
"""

import pandas as pd


# ask for working file
def reader(file_path):
    df = pd.read_csv(file_path, header=None)
    return df