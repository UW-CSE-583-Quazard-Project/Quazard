import pandas as pd


def executioner_preview(file, response_id_column, status_column):
    '''
    This function will remove rows/partiicpants based on the recaptcha score

    Parameters:
    - file (pandas.DataFrame): The input DataFrame coming from upstream.
    - response_id_column: string. The column that has the response ID. User needs to input this.
    - status_column: string. The column that has the status. User needs to input this.
    - threshold: float. The recaptcha score threshold
    - equal_score: boolean. If yes, then participants with scores equal to or above the threshold
    will be kept. If no, then only participants with scores equal to the theshold will be kept.
    - missing_score: boolean. If yes, then participants without a score will be kept. If no, they
    will be removed

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> from itertools import cycle, islice
    >>> data = {'ID': ["PX_A", "PX_B", "PX_C", "PX_D"],
        'status_px': ["Survey Preview", "IP Address", "IP Address", "IP Address"]}
    >>> df = pd.DataFrame(data)
    >>> cleaned = executioner_preview(df,"ID", "status_px")
    '''
    # Check whether the response ID column is in the dataframe
    if response_id_column not in file.columns:
        raise ValueError("Please make sure response ID column name is properly entered")
    
    # Check whether the finished column is in the dataframe
    if status_column not in file.columns:
        raise ValueError("Please make sure the status column name is properly entered")

    # Remove rows that were preview
    newdf = file[file[status_column] != 'Survey Preview']
    id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    
    # make the change final
    file = newdf
    # return dataframe, a list of ID that was removed, and how many removed
    return file, id_difference, len(id_difference)

def executioner_completion(file, response_id_column, finished_column):
    '''
    This function will remove rows/partiicpants based on completion

    Parameters:
    - file (pandas.DataFrame): The input DataFrame coming from upstream.
    - response_id_column: string. The column that has the response ID. User needs to input this.
    - finished_column: string. The column that tells whether the survey was finished User needs to input this.
    - threshold: float. The recaptcha score threshold
    - equal_score: boolean. If yes, then participants with scores equal to or above the threshold
    will be kept. If no, then only participants with scores equal to the theshold will be kept.
    - missing_score: boolean. If yes, then participants without a score will be kept. If no, they
    will be removed

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> from itertools import cycle, islice
    >>> data = {'ID': ["PX_A", "PX_B", "PX_C", "PX_D"],
        'finished': ["TRUE", "TRUE", "FALSE", "FALSE"]}
    >>> df = pd.DataFrame(data)
    >>> cleaned = executioner_completion(df,"ID", "finished")
    '''
    # Check whether the response ID column is in the dataframe
    if response_id_column not in file.columns:
        raise ValueError("Please make sure response ID column name is properly entered")
    
    # Check whether the finished column is in the dataframe
    if finished_column not in file.columns:
        raise ValueError("Please make sure the finished column name is properly entered")
    
    # Check whether the finished column has only TRUE and FALSE as values.
    expected_values = ['TRUE', 'FALSE']
    check_values = file[finished_column].isin(expected_values)

    # Check if all values are either 'TRUE' or 'FALSE'
    result = check_values.all()

    if result:
        pass
    else:
        raise ValueError("Please make sure the finished column has only TRUE and FALSE. Capitalization matters.")

    # Remove rows that were unfinished
    newdf = file[file[finished_column] != 'FALSE']
    id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    
    # make the change final
    file = newdf
    # return dataframe, a list of ID that was removed, and how many removed
    return file, id_difference, len(id_difference)


def executioner_recaptcha(file, response_id_column, recaptcha_id_column, threshold, equal_score, missing_score):
    '''
    This function will remove rows/partiicpants based on the recaptcha score

    Parameters:
    - file (pandas.DataFrame): The input DataFrame coming from upstream.
    - response_id_column: string. The column that has the response ID. User needs to input this.
    - recaptcha_id_column: string. The column that has the recaptcha score. User needs to input this.
    - threshold: float. The recaptcha score threshold
    - equal_score: boolean. If yes, then participants with scores equal to or above the threshold
    will be kept. If no, then only participants with scores equal to the theshold will be kept.
    - missing_score: boolean. If yes, then participants without a score will be kept. If no, they
    will be removed

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> from itertools import cycle, islice
    >>> data = {'ID': ["PX_A", "PX_B", "PX_C", "PX_D"],
        'recaptcha': [0.2, 0.8, 0.5, np.nan]}
    >>> df = pd.DataFrame(data)
    >>> cleaned = executioner_recaptcha(df,"ID", "recaptcha", 0.5, True, False)
    '''
    # Check whether the response ID column is in the dataframe
    if response_id_column not in file.columns:
        raise ValueError("Please make sure response ID column name is properly entered")
    
    # Check whether the recaptcha column is in the dataframe
    if recaptcha_id_column not in file.columns:
        raise ValueError("Please make sure recaptcha column name is properly entered")

    # Check if the number of trials is a positive integer
    if not (isinstance(threshold, float) or isinstance(threshold, int)) and threshold >= 0:
         raise ValueError("The number of trials should be a positive integer")
    
    # Check if the equal_score is a boolean
    if not isinstance(equal_score, bool):
         raise ValueError("Please make sure the input for whether it is equal or above is True or False")
    
    # Check if the equal_score is a boolean
    if not isinstance(missing_score, bool):
         raise ValueError("Please make sure the input for whether to keep missing scores is True or False")

    # Remove rows based on threshold
    if equal_score == True:
        newdf = file[(file[recaptcha_id_column] >= 0.5) | pd.isnull(file[recaptcha_id_column])]
        id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    elif equal_score == False:
        newdf = file[(file[recaptcha_id_column] > 0.5) | pd.isnull(file[recaptcha_id_column])]
        id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    # Remove based on missing score
    if missing_score == False:
        newdf = newdf.dropna(subset=[recaptcha_id_column])
        id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    # make the change final
    file = newdf
    # return dataframe, a list of ID that was removed, and how many removed
    return file, id_difference, len(id_difference)

    
def executioner_attentioncheck_multiplechoice(file, response_id_column, attentioncheck_mp, right_answer):
    '''
    This function will remove rows/partiicpants based on multiple choice attention checks.

    Parameters:
    - file (pandas.DataFrame): The input DataFrame coming from upstream.
    - response_id_column: string. The column that has the response ID. User needs to input this.
    - attentioncheck_mp: string. The column name of the attention check question.
    - right_answer: list. A list of correct answers. Should be integers.

    Example:
    >>> import pandas as pd
    >>> from itertools import cycle, islice
    >>> data = {'ID': ["PX_A", "PX_B", "PX_C", "PX_D"],
        'attentioncheck': [1, 2, 3, 4]}
    >>> df = pd.DataFrame(data)
    >>> cleaned = executioner_attentioncheck_multiplechoice(df,"ID", "attentioncheck", [1,2])
    '''
    # Check whether the response ID column is in the dataframe
    if response_id_column not in file.columns:
        raise ValueError("Please make sure response ID column name is properly entered")
    
    # Check whether the response ID column is in the dataframe
    if attentioncheck_mp not in file.columns:
        raise ValueError("Please make sure attention check column name is properly entered")

    # Check if the right answer is list with all positive integers
    if not all(isinstance(numbers, int) for numbers in right_answer):
         raise ValueError("Please make sure the right answer is a list of numbers. Select 'Use Numeric Values' when downloading from qualtrics")

    # Remove rows based on the right answer
    newdf = file[file[attentioncheck_mp].isin(right_answer)]
    id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    
    # make the change final
    file = newdf
    # return dataframe, a list of ID that was removed, and how many removed
    return file, id_difference, len(id_difference)

def executioner_attentioncheck_text(file, response_id_column, attentioncheck_text, right_answer, reportonly):
    '''
    This function will remove rows/partiicpants based on multiple choice attention checks.

    Parameters:
    - file (pandas.DataFrame): The input DataFrame coming from upstream.
    - response_id_column: string. The column that has the response ID. User needs to input this.
    - attentioncheck_text: string. The column name of the attention check question.
    - right_answer: list. A list of correct answers. Should be strings.
    - reportonly: Boolean. If yes, then the function only returns the list of unmatching
    rows. If no, then these rows are removed.

    Example:
    >>> import pandas as pd
    >>> from itertools import cycle, islice
    >>> data = {'ID': ["PX_A", "PX_B", "PX_C", "PX_D"],
        'attentioncheck': ["tiger", "car", "dog", "cat"]}
    >>> df = pd.DataFrame(data)
    >>> cleaned = executioner_attentioncheck_text(df,"ID", "attentioncheck", ["tiger","cat"], True)
    '''
    # Check whether the response ID column is in the dataframe
    if response_id_column not in file.columns:
        raise ValueError("Please make sure response ID column name is properly entered")
    
    # Check whether the response ID column is in the dataframe
    if attentioncheck_text not in file.columns:
        raise ValueError("Please make sure attention check column name is properly entered")

    # Check if the right answer is a list of strings
    if not all(isinstance(answers, str) for answers in right_answer):
         raise ValueError("Please make sure the right answer is a list of strings.")
 
    newdf = file[file[attentioncheck_text].isin(right_answer)]
    id_difference = pd.concat([file[response_id_column], newdf[response_id_column]]).drop_duplicates(keep=False).tolist()
    # If report only is no, remove rows based on the right answer
    if reportonly == False:       
        # make the change final
        file = newdf
    # return dataframe, a list of ID that was removed, and how many removed
    return file, id_difference, len(id_difference)