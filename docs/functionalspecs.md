**Functional Specification**

_Background:_
    Data exported from Qualtrics contains redundancies and unnecessary
    data. Users often have to clean the raw data before they can data
    analyze.

_User profile:_
    Individuals who export data from Qualtrics and want to clean it
    before analysis.

_Data sources:_
    Exported data file from Qualtrics (in csv format).

_Use cases:_

(1) A data analyst in marketing team uses Qualtrics forms to collect
    lots of data from various users. She struggles to prepare the data
    manually because the Qualtrics survey and data gathered are very
    complex. The data contain several groups of users who have very
    different experiences. She wants to organize the data by certain
    parameters and she wants to eliminate incomplete surveys. She does
    not have programming skills, but she does have statistical knowledge.
    She can use the Long-wide Converter and the Executioner components 
    from our tool to speed up her workflow.

(2) A social scientist frequently uses Qualtrics surveys to collect data
    for her thesis. She wants to extract data from her survey and export
    the data into a format to be analyzed in R. She knows how to program
    in R but not in Python, so she would prefer a clear user interface.
    She can use the GUI component (which contains all other components) 
    to clean her data before data analysis in R.
