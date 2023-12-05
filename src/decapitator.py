import pandas as pd

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
    if not isinstance(rows, None) or not isinstance(rows, list):
        raise ValueError("The type of the rows should be None or a list")
    if not isinstance(file, pd.DataFrame):
        raise ValueError()
    if rows == None:
        rows = [1, 2]
    else:
        for i in range(len(rows)):
            rows[i] -= 1
    file = file.drop(labels=rows, axis=0)
    file = file.reset_index(drop=True)
    return file
