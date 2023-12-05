"""
This is module asks the user for their working directory (must contain
their raw .csv file from Qualtrics). This module also contains a 
function for reading the raw Qualtrics file (.csv) into a pandas 
dataframe. This allows for further processing by Quazard.
"""

import os
import glob
from tkinter.filedialog import askdirectory
import pandas as pd


# ask for user's working directory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
os.chdir(path)

# making dataframe
filename = glob.glob("*.csv") # returns a list
for f in filename:
    df = pd.read_csv(f)
