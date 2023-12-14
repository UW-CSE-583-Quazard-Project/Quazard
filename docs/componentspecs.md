**Component Specification**


_Reader (required):_ Read the csv file from date file system and translate
.csv file into pandas dataframe
- input: .csv file
- output: pandas dataframe

 
_Decapitator (optional):_ Remove duplicate header rows (i.e., 2 & 3)
- input: dataframe & list of numbers indicating which rows should be 
deleted
- output: dataframe with duplicate rows removed

_Executioner (optional):_ Remove invalid rows based on required values in
certain columns (e.g., failed reCAPTCHA)
- input: dataframe & list of column names with required values
- output: dataframe with invalid rows removed

_Janitor (optional):_ Remove unused columns (e.g., web broswer 
information)
- input: dataframe & list of columns names to be removed
- output: dataframe with unused columns removed

_Long-wide Converter (optional):_ Convert repeated measures/multi-trial
surveys from one participant per row to each measure/trial per row.
- input: dataframe & list of trials/rows per participant
- output: dataframe with the repeated measures/trials merged into one
organized by participant

_Frankenstein (optional):_ Aggregate quantitative data
- input: dataframe & list of "group by" variables
- output: re-ordered dataframe by "group by" variable(s)

_Outputer (required):_ Convert dataframe into .csv file for further
processing
- input: finalized dataframe
- output: .csv file

_GUI:_ Interface for users unfamiliar with Python or programming to
utilize Quazard tool
- input: user-specified preferences/needs
- output: a list of parameters that specify the actions
