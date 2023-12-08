import tkinter as tk
import tkinter.ttk as ttk
import janitor
import pandas as pd
from tkinter import messagebox
def create_janitor_tab(tab_control, dataframe=None):
    janitor_tab = ttk.Frame(tab_control)
    tab_control.add(janitor_tab, text='Janitor')
    
    # Test dataframe
    df = pd.read_csv("../test/data/vt3 data cleaned not converted or aggregated.csv")
    columns = df.columns.tolist()
    
    # Create a box to display selected columns
    listbox = tk.Listbox(janitor_tab)
    listbox.pack(pady=10)
    
    # Create a dropmenu with options of dataframe columns
    selected_values = []
    combobox = ttk.Combobox(janitor_tab, values=columns)
    combobox.bind("<<ComboboxSelected>>", lambda event, cb=combobox: add_to_list(cb, selected_values, listbox))
    combobox.pack(padx=20, pady=20)
    
    # Create a button to submit selected values
    drop_button = ttk.Button(janitor_tab, text="Drop Selected Columns", command=lambda: drop_selected_columns(selected_values, df))
    drop_button.pack(pady=10)
    
    # Create a button to clear selected columns
    clear_button = ttk.Button(janitor_tab, text="Clear List", command=lambda: clear_list(listbox))
    clear_button.pack(pady=10)
    
def add_to_list(combobox, selected_values, listbox):
    selected_value = combobox.get()
    if selected_value not in selected_values:
        selected_values.append(selected_value)
        update_listbox(selected_values, listbox)

def update_listbox(selected_values, listbox):
    listbox.delete(0, tk.END)
    for value in selected_values:
        listbox.insert(tk.END, value)
        
def clear_list(listbox):
    listbox.delete(0, tk.END)
    
def drop_selected_columns(selected_values, dataframe):
    # Check if there are columns selected
    if selected_values:
        new_dataframe = janitor.drop_cols(dataframe, selected_values)
        if len(new_dataframe.columns) != len(dataframe.columns):
            messagebox.showinfo("Columns Dropped", "Selected columns have been dropped.")
        else:
            messagebox.showwarning("Dropping Failed", "Selected columns have not beed dropped properly!")