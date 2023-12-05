"""
This component will ask the user to specify which columns they do not need
and then remove those columns
"""
def drop_cols(dataframe, col_name_list):
    """
    Parameters:
    - df: Dataframe passed from the previous component
    - col_name_list: A list containing unwanted column names

    Returns:
    dataframe: A modified dataframe that excluded the given column names

    Raise:
    ValueError: When there is invalid dataframe
    ValueError: When the given column name is not in the current dataframe
    """
    if dataframe is None:
        raise ValueError("Invalid dataframe found.")
    for name in col_name_list:
        if name not in dataframe.columns:
            raise ValueError("Parameters already dropped or not existing in the database.")
        dataframe = dataframe.drop(name, axis=1)
    return dataframe
