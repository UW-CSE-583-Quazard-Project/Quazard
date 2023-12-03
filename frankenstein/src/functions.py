"""
This components provides aggregate functions: min, max, mean, sum, count
"""
import pandas as pd
from pandas.api.types import is_numeric_dtype
def aggregate(dataframe, group_keys, applied_keys, modes):
    """
    Parameters:
    - dataframe: Dataframe with only numeric values passed from the previous component
    - group_keys: Given columns to be grouped by
    - applied_keys: Given columns to be aggregated on
    - mode: Mode that chooses which aggregation function

    Returns:
    dataframe: A modified dataframe that excluded the given column names

    Raise:
    ValueError: When there cannot be valid aggregation functions
    """
    
    # Check if the column is numeric: if so, it can be applied by any aggregation method
    # Else if it is bool or string, it should only be aggregated by count
    
    # Three important args:
    # 1. Groupby columns
    # 2. Applied columns
    # 3. Mode
    if dataframe is None:
       raise ValueError("Invalid dataframe found.")
    col_mode_pairs = {}
    numeric_oprations = ["min", "max", "mean", "sum"]
    for i in range(len(applied_keys)):
        if (not is_numeric_dtype(dataframe[applied_keys[i]])) and modes[i] in numeric_oprations:
            raise ValueError("You cannot apply this operation because the target is invalid")
        col_mode_pairs[applied_keys[i]] = modes[i]
    return dataframe.groupby(group_keys).agg(col_mode_pairs).reset_index()

   