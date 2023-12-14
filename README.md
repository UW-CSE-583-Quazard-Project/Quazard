This is a Qualtrics cleaning tool. We call it Qualtrics Wizard (or 
Quazard, for short). This tool was originally conceived and created for UW 
CSE 583 and by Amanda Lin, Chao Qin, Sharon Wang, and Ted Zhong.

Qualtrics is an online survey management tool. Once data has been collected, it is typically exported from Qualtrics for further data analysis. However, this export tends contain redundancies and unnecessary data that most users manually clean prior to data analysis. 

Quazard was designed to assist users in cleaning raw exported data from Qualtrics. It has capabilities to clean, process, reformat, and more. 

Quazard
├── LICENSE
├── README.md
├── docs
│   ├── componentspecs.md
│   ├── finalpresentation.pdf
│   ├── functionalspecs.md
│   └── techreview.md
├── environment.yml
├── src
│   ├── __init__.py
│   ├── decapitator.py
│   ├── decapitator_gui.py
│   ├── executioner.py
│   ├── executioner_gui.py
│   ├── frankenstein.py
│   ├── frankenstein_gui.py
│   ├── gui.py
│   ├── janitor.py
│   ├── janitor_gui.py
│   ├── longwideconverter.py
│   ├── longwideconverter_gui.py
│   ├── outputer.py
│   ├── outputer_gui.py
│   ├── reader.py
│   └── reader_gui.py
└── test
    ├── __init__.py
    ├── test_decapitator.py
    ├── test_executioner.py
    ├── test_janitor.py
    ├── test_longwideconverter.py
    ├── test_outputer.py
    └── test_reader.py
