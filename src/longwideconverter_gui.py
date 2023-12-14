"""
Module for Converter GUI component
Allows user to convert the wide format data to long format data
by interacting with the GUI 
"""
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import longwideconverter as convert

class LongWideConverter:
    """ 
    A GUI class for the converter functionality
    It will convert the wide-format data to long-format data for future easier analysis

    Parameters:
    - app_instance: An instance of the main application class.

    Usage:
    - Create an instance of this class, passing the main application instance.
    - Use the created instance to create the Decapitator tab within the application GUI.
    """
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def create_converter_tab(self, tab_control):
        """    
        Parameters:
        - tab_control: The upper layer control from the main GUI
        """
        file = self.app_instance.get_dataframe()
        
        converter_tab = ttk.Frame(tab_control)
        tab_control.add(converter_tab, text='Long-Wide Converter')

        label_converter = ttk.Label(converter_tab, text="This is the Converter Tab. \n"
                                    "Here you can reconfigure your wide format data to long format.\n"
                                    "Before you start, make sure the dataset meets the following criteria.\n"
                                    "If you are unsure, go to the output tab and print out the csv to check.\n"
                                    "#1. The data has only one line of header\n"
                                    "#2. Each trial/set of repeated measure\'s columns should be right next to each other.\n"
                                    "E.g.,: Trial1Q1,Trial1Q2,Trial2Q1,Trial2Q2\n"
                                    "#3. Each trial/set of repeated measure has the EXACTLY same number of columns \n"
                                    "#4. Each question/column in the trials has the EXACTLY same question type (number, string, .etc)")
        label_converter.pack(padx=10, pady=10)

        #### Upon Submission ####
        def submit():
            """    
            After clicking the submit button, this function will read the input and pass
            them onto the longwideconverter function.
            """
            # get arguments
            response_id_column = entry_id.get()
            trial_num_text = entry_trial_num.get()
            trial_length_text = entry_trial_length.get()
            trial_start = str(entry_start.get())
            file = self.app_instance.get_dataframe()
            # Check if any of the trial inputs are empty
            if not (trial_num_text and trial_length_text):
                messagebox.showerror("Error", "Trial number and length cannot be empty.")
                return None

            # Validate and convert trial_num and trial_length to integers
            try:
                trial_num = int(trial_num_text)
                trial_length = int(trial_length_text)
            except ValueError:
                messagebox.showerror("Error", "Trial number and length must be integers.")
                return None

            new_file = convert.long_dataframe_maker(file, response_id_column, trial_num, trial_length, trial_start)
            messagebox.showinfo("Success!","Success!")
            # print(file)
            self.app_instance.update_dataframe(new_file)
            # return file
        
        #### Interface ####

        ### General Paramters ###
        # Create an input text entry for response id
        label_id = tk.Label(converter_tab, text="Enter the column name for response id column.\n"
                            "If you are unsure, please go to the output tab and print out the CSV to check")
        label_id.pack()
        entry_id = tk.Entry(converter_tab)
        entry_id.pack()

        # crete an input text entry for number of trials
        label_trial_num = tk.Label(converter_tab, text="Enter the number of trials. Must be a positive integer.")
        label_trial_num.pack()
        validate_func = converter_tab.register(self.validate_input)
        entry_trial_num = tk.Entry(converter_tab, validate="key", validatecommand=(validate_func, '%P'))
        entry_trial_num.pack()

        # crete an input text entry for trial length
        label_trial_length = tk.Label(converter_tab, text="Enter the length (number of columns) of each trial/set "
                                      "of repeated measure. Must be a positive integer.")
        label_trial_length.pack()
        validate_func = converter_tab.register(self.validate_input)
        entry_trial_length = tk.Entry(converter_tab, validate="key", validatecommand=(validate_func, '%P'))
        entry_trial_length.pack()

        # Create an input text entry for starting column
        label_start = tk.Label(converter_tab, text="Enter the column name where the trials first start. E.g., Trial1Q1.\n"
                               "If you are unsure, please go to the output tab and print out the CSV to check")
        label_start.pack()
        entry_start = tk.Entry(converter_tab)
        entry_start.pack()

        
        #### At the end ####
        # Create a Button to submit the tab
        button_submit = tk.Button(converter_tab, text="Submit", command=submit)
        button_submit.pack()


    def validate_input(self, new_value):
        if new_value == "":
            return True

        try:
            int(new_value)
            return True
        except ValueError:
            return False
