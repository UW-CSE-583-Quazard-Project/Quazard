import pandas as pd
from itertools import cycle, islice


def long_dataframe_maker(file, response_id_column, trial_num, trial_length, trial_start):
    '''
    This function will create a new dataframe that is long format from the exisiting dataframe.

    Parameters:
    - file (pandas.DataFrame): The input DataFrame coming from upstream.
    - trial_num: integer. how many trials/rows per participant should the long dataframe have.
    User needs to input this.
    - trial_length: integer. how many columns each trial has.
    - trial_start: string. At which column in the wide dataframe does the trial start.
    - response_id_column: string. The column that has the response ID. User needs to input this.
    Example:
    >>> import pandas as pd
    >>> from itertools import cycle, islice
    >>> data = {'ID': ["PX_A", "PX_B", "PX_C"],
        'Trial1Q1': ["12", "13", "12"],
        'Trial1Q2': ["23", "25", "22"],
        'Trial2Q1': ["33", "36", "34"],
        'Trial2Q2': ["44", "32", "34"],
        'Age': ["18", "23", "22"],}
    >>> df = pd.DataFrame(data)
    >>> outputlong = long_dataframe_maker(df, "ID", 2, 2, "Trial1Q1")
    '''
    # Check whether the response ID column is in the dataframe
    if response_id_column not in file.columns:
        raise ValueError("Please make sure response ID column name is properly entered")

    # Check if the the number of trials is a positive integer 
    if not isinstance(trial_num, int) and trial_num > 0:
         raise ValueError("The number of trials should be a positive integer")
    
    # Check if the the length of a trial is a positive integer 
    if not isinstance(trial_length, int) and trial_num > 0:
         raise ValueError("The length of a trial should be a positive integer")
    
    # Check if the the start of the trials is in the  dataframe 
    if trial_start not in file.columns:
         raise ValueError("Please make sure the name of the starting column of the trials is properly entered")

    # Create a dataframe with a number of rows per participant
    response_id_list = file[response_id_column].tolist()
    long_dataframe = pd.DataFrame({response_id_column: response_id_list * ((len(response_id_list)*trial_num // len(response_id_list)) + 1)})[:len(response_id_list)*trial_num]
    # Sort the dataframe in preparation for the next move
    long_dataframe = long_dataframe.sort_values(by = response_id_column, ascending=[True])

    # Add in trial number
    # get repeated values first
    repeating_numbers = cycle(range(1, trial_num + 1))

    # now we add the repeated values along with the series name
    num_rows = len(long_dataframe)
    repeated_values = list(islice(repeating_numbers, num_rows))

    # Add a new column 'trial' with repeating numbers
    long_dataframe['trial'] = repeated_values

    # need to sort the dataframe in preparation for the next step
    long_dataframe = long_dataframe.sort_values(by=list(long_dataframe.columns))

    ### Next we are going to add data to the long dataframe
    # First we remove all unwanted columns from the wide dataframe.
    # That is, all columns not in trials or not response ID.

    # Get response ID column index
    response_id_column_index = file.columns.get_loc(response_id_column)

    # Get the indices for the trials:
    trial_start_index = file.columns.get_loc(trial_start)
    trials_indices = list(range(trial_start_index, trial_start_index + (trial_num * trial_length)))
    trials_indices.append(response_id_column_index)

    # remove unwanted columns. In this new dataframe, the last column is the response ID.
    # the trials start at the first column
    wide_trials = file.iloc[:, trials_indices]

    # get a list of column index
    column_index_list = list(range(0, trial_length))

    # new response id location
    response_id_column_index_wide_trials = wide_trials.columns.get_loc(response_id_column)
    
    # Now let's convert it into long format. Question by question.
    for column_index in column_index_list:
        # get a list of columns to keep. 
        # The columns should be all the columns for one question in different trials.
        columns_to_keep = list(range(column_index, trial_length*trial_num, trial_length))
        # We also need response ID
        columns_to_keep.append(response_id_column_index_wide_trials)
        # now remove all unwanted columns
        temp_wide_df = wide_trials.iloc[:, columns_to_keep]
        # covert it into long
        temp_long_df = temp_wide_df.melt(id_vars=response_id_column, var_name='trial', value_name="Question " + str(column_index + 1))
        # Create a mapping dictionary for variable columns to sequential numbers
        var_mapping = {var: i + 1 for i, var in enumerate(temp_wide_df.columns[temp_wide_df.columns != response_id_column])}
        # Map variable columns to sequential numbers in the long DataFrame
        temp_long_df['trial'] = temp_long_df['trial'].map(var_mapping)
        # Make sure trial number is int64
        temp_long_df['trial'] = temp_long_df['trial'].astype('int64')
        # merge this temp long df with the long dataframe we created earlier.
        long_dataframe = pd.merge(long_dataframe, temp_long_df, on=[response_id_column, 'trial'], how='left')

    # Now we want to merge the deleted non-trial columns back.
    # First find the indices again. We don't want the response ID indices here so redo it.
    trials_indices_new = list(range(trial_start_index, trial_start_index + (trial_num * trial_length)))
    # create dataframe to hold the non-trial data
    wide_non_trials = file.drop(file.columns[trials_indices_new], axis=1)
    # merge based on response id
    long_dataframe = pd.merge(long_dataframe, wide_non_trials, on=[response_id_column], how='left')

    # now let's yolo. replace the file df with the long_dataframe!
    file = long_dataframe
    return file

    
