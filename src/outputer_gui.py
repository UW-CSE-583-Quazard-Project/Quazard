"""
Module for Outputer GUI component
Allows user to export the current dataframe to csv files
by interacting with the GUI
"""
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import outputer

class OutputerGUI:
    """ 
    A GUI class for the outputer functionality
    It will export the current dataframe as csv file with the given file name

    Parameters:
    - app_instance: An instance of the main application class.

    Usage:
    - Create an instance of this class, passing the main application instance.
    - Use the created instance to create the Decapitator tab within the application GUI.
    """
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def outputer_function(self, file_path):
        """   
        This function calls your outputer function with the file path 
        Parameters:
        - tab_control: The upper layer control from the main GUI
        """
        print(f"Outputer function called with file path: {file_path}")
        file = self.app_instance.get_dataframe()
        outputer.outputer(file, file_path)

    def create_outputer_tab(self, tab_control):
        """    
        Parameters:
        - tab_control: The upper layer control from the main GUI
        """
        outputer_tab = ttk.Frame(tab_control)
        tab_control.add(outputer_tab, text='Outputer')
        
        label_outputer = ttk.Label(outputer_tab, text='This is the Outputer Tab. You can download the csv file from here!\n \
                                   Please enter the COMPLTE file path here.')
        label_outputer.pack(padx=10, pady=10)

        # Add an Entry widget for the file path
        file_path_var = tk.StringVar()
        file_path_entry = ttk.Entry(outputer_tab, textvariable=file_path_var)
        file_path_entry.pack(pady=10)

        # Add a Download Button
        download_button = ttk.Button(outputer_tab, text='Download', command=lambda: self.outputer_function(file_path_var.get()))
        download_button.pack(pady=10)