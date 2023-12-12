import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import outputer

def outputer_function(file, file_path):
    # Call your outputer function with the file path
    print(f"Outputer function called with file path: {file_path}")
    outputer.outputer(file, file_path)

def create_outputer_tab(tab_control, dataframe=None):
    outputer_tab = ttk.Frame(tab_control)
    tab_control.add(outputer_tab, text='Outputer')
    
    label_outputer = ttk.Label(outputer_tab, text='This is the Outputer Tab. You can download the csv file from here!\n Please enter the file path here.')
    label_outputer.pack(padx=10, pady=10)

    # Add an Entry widget for the file path
    file_path_var = tk.StringVar()
    file_path_entry = ttk.Entry(outputer_tab, textvariable=file_path_var)
    file_path_entry.pack(pady=10)

    # Add a Download Button
    download_button = ttk.Button(outputer_tab, text='Download', command=lambda: outputer_function(dataframe, file_path_var.get()))
    download_button.pack(pady=10)