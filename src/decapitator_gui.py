"""
Module for decapitator GUI component
Allows user to drop the repeated headers of the dataframe
by interacting with the GUI
"""
import tkinter as tk
import tkinter.ttk as ttk
import decapitator
import re

class DecapitatorGUI:
    """
    A GUI class for the Decapitator functionality.

    Parameters:
    - app_instance: An instance of the main application class.

    Usage:
    - Create an instance of this class, passing the main application instance.
    - Use the created instance to create the Decapitator tab within the application GUI.
    """
    def __init__(self, app_instance):
        self.app_instance = app_instance
    
    def is_valid_input(self, user_input):
        """
        Checks if the input contains valid characters for the decapitator function.

        Parameters:
        - user_input (str): The user-provided input for selecting rows.

        Returns:
        - bool: True if the input is valid, False otherwise.
        """
        if len(user_input) == 0:
            return False
        pattern = re.compile(r'[^1-3,]')
        return not bool(pattern.search(user_input))

    def decapitator_function(self, dataframe, rows, submit_button, result_label):
        """
        Executes the decapitator function based on user input and updates the application's dataframe.

        Parameters:
        - dataframe: The input DataFrame for the decapitator function.
        - rows (str): Comma-separated string representing the rows to be removed.
        - submit_button: The button triggering the decapitator function.
        - result_label: The label for displaying the result message.
        """
        submit_button.configure(state="disabled")
        if not self.is_valid_input(rows):
            rows = None
            result_label.config(text="The default redundant headers are removed")
        else:
            rows = rows.split(",")
            rows = [int(s) for s in rows]
            print(rows)
            result_label.config(text="Redundant headers are removed")
        decapitator_result = decapitator.decapitator(dataframe, rows)
        self.app_instance.update_dataframe(decapitator_result)
        
    def create_decapitator_tab(self, tab_control):
        """
        Creates the Decapitator tab within the given tab control.

        Parameters:
        - tab_control: The parent tab control where the Decapitator tab should be added.
        """
        decapitator_tab = ttk.Frame(tab_control)
        tab_control.add(decapitator_tab, text='Decapitator')
        
        label_decapitator = ttk.Label(decapitator_tab, text="This is the Decapitator Tab. \n"
                                      "You can choose which redundant header that you want to delete. \n"
                                      "By default it deletes the second and the third row. \n"
                                      "But if you want to delete the first row and the third row, please enter 1,3 without any space")
        label_decapitator.pack(padx=10, pady=10)

        entry_text = tk.StringVar()
        entry = ttk.Entry(decapitator_tab, textvariable=entry_text)
        entry.pack(pady=10)

        # Add a Label for displaying the result
        result_label = ttk.Label(decapitator_tab, text="")
        result_label.pack(pady=10)

        submit_button = ttk.Button(decapitator_tab, text='Submit',
                                   command=lambda: self.decapitator_function(self.app_instance.get_dataframe(), entry_text.get(), submit_button, result_label))
        submit_button.pack(pady=10)
        