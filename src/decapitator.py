'''
This module is for the decapitator component. It is used to remove redundent headers generated
by Qualtrics.
'''
import pandas as pd
import os

def decapitator(file, rows=None):
    """
    Remove specified rows from a DataFrame.

    Parameters:
    - file (pandas.DataFrame): The input DataFrame.
    - rows (list, optional): List of row indices to remove. If None, default rows [1, 2] are removed.

    Returns:
    pandas.DataFrame: A new DataFrame with specified rows removed.

    Example:
    >>> import pandas as pd
    >>> data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    >>> df = pd.DataFrame(data)
    >>> result = decapitator(df, rows=[1])
    """
    # print(file)
    if rows != None and not isinstance(rows, list):
        raise ValueError("The type of the rows should be None or a list")
    if not isinstance(file, pd.DataFrame):
        raise ValueError("The input file should be a dataframe")
    if rows == None:
        rows = [1, 2]
    else:
        for i in range(len(rows)):
            rows[i] -= 1
    if len(rows) > 2:
        raise ValueError("The number of rows shoudl be less or equal to two")
    file = file.drop(labels=rows, axis=0)
    file = file.reset_index(drop=True)
    file.columns = file.iloc[0]
    file = file.drop(labels=0, axis=0)
    file = file.reset_index(drop=True)
    # file = file.convert_dtypes()
    for col in file.columns:
        if file[col].dtype == 'object':
            try:
                file[col] = pd.to_numeric(file[col])
            except ValueError:
                try:
                    file[col] = pd.to_datetime(file[col])
                except ValueError:
                    pass  # Handle non-convertible columns
    print(file.dtypes)
    print(file['Q_RecaptchaScore'].dtypes)
    return file
