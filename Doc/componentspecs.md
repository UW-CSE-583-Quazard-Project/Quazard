Component Specification


Reader (required): Read the csv file from date file system and translate
.csv file into pandas dataframe
	input: .csv file
	output: pandas dataframe

 
Decapitator (optional): Remove duplicate header rows (i.e., 2 & 3)
	input: dataframe & list of numbers indicating which rows should be 
	deleted
	output: dataframe with duplicate rows removed

Executioner (optional): Remove invalid rows based on required values in
certain columns (e.g., failed reCAPTCHA)
	input: dataframe & list of column names with required values
	output: dataframe with invalid rows removed

Janitor (optional): Remove unused columns (e.g., web broswer 
information)
	input: dataframe & list of columns names to be removed
	output: dataframe with unused columns removed

Long-wide Converter (optional): Convert repeated measures/multi-trial
surveys from one participant per row to each measure/trial per row.
	input: dataframe & list of ***
	output: dataframe with ***

Frankenstein (optional): Aggregate quantitative data
	input: dataframe & list of "group by" variables
	output: re-ordered dataframe by "group by" variable(s)

Outputer (required): Convert dataframe into .csv file for further
processing
	input: finalized dataframe
	output: .csv file

GUI: Interface for users unfamiliar with Python or programming to
utilize Quazard tool
	input: user-specified preferences/needs
	output: a list of parameters that specify the actions
