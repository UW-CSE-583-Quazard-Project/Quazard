import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import longwideconverter as convert

class LongWideConverter:
    def __init__(self):
        pass

    def create_converter_tab(self, tab_control, file):
        
        converter_tab = ttk.Frame(tab_control)
        tab_control.add(converter_tab, text='Long-Wide Converter')

        label_converter = ttk.Label(converter_tab, text='This is the Converter Tab. Here you can reconfigure your wide format data to long format.\nBefore you start, make sure the dataset meets the following criteria.\nIf you are unsure, go to the output tab and print out the csv to check.\n#1. The data has only one line of header\n#2. Each trial/set of repeated measure\'s columns should be right next to each other.\nE.g.,: Trial1Q1,Trial1Q2,Trial2Q1,Trial2Q2\n#3. Each trial/set of repeated measure has the EXACTLY same number of columns')
        label_converter.pack(padx=10, pady=10)

        #### Upon Submission ####
        def submit(file):
            # get arguments
            response_id_column = entry_id.get()
            trial_num_text = entry_trial_num.get()
            trial_length_text = entry_trial_length.get()
            trial_start = str(entry_start.get())

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

            file = convert.long_dataframe_maker(file, response_id_column, trial_num, trial_length, trial_start)
            messagebox.showinfo("Success!")
            print(file)
                
            return file
        
        #### Interface ####

        ### General Paramters ###
        # Create an input text entry for response id
        label_id = tk.Label(converter_tab, text="Enter the column name for response id column.\nIf you are unsure, please go to the output tab and print out the CSV to check")
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
        label_trial_length = tk.Label(converter_tab, text="Enter the length (number of columns) of each trial/set of repeated measure. Must be a positive integer.")
        label_trial_length.pack()
        validate_func = converter_tab.register(self.validate_input)
        entry_trial_length = tk.Entry(converter_tab, validate="key", validatecommand=(validate_func, '%P'))
        entry_trial_length.pack()

        # Create an input text entry for starting column
        label_start = tk.Label(converter_tab, text="Enter the column name where the trials first start. E.g., Trial1Q1.\nIf you are unsure, please go to the output tab and print out the CSV to check")
        label_start.pack()
        entry_start = tk.Entry(converter_tab)
        entry_start.pack()

        
        #### At the end ####
        # Create a Button to submit the tab
        button_submit = tk.Button(converter_tab, text="Submit", command=submit)
        button_submit.pack()

        # return file so that other tabs can do something with it.
        return file

    def validate_input(new_value):
        if new_value == "":
            return True

        try:
            int(new_value)
            return True
        except ValueError:
            return False
