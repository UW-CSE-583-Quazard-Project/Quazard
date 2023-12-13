"""
This is the module to handle the GUI tab for Frankenstein
"""
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import frankenstein as fc

class FrankensteinGUI:
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def create_frankenstein_tab(self, tab_control, dataframe=None):
        """    
        Parameters:
        - tab_control: The upper layer control from the main GUI
        """
        frankenstein_tab = ttk.Frame(tab_control)
        tab_control.add(frankenstein_tab, text='Frankenstein')
        
        # Test dataframe
        if not dataframe:
            dataframe = pd.read_csv("../test/data/vx3 data long format.csv")
            columns = dataframe.columns.tolist()
        
        # Create labels
        label1 = ttk.Label(frankenstein_tab, text="Select columns to be grouped:")
        label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        group_keys = []
        combobox = ttk.Combobox(frankenstein_tab, values=columns)
        combobox.grid(row=1, column=0, padx=20, pady=5)
        
        # Create a box to display selected columns
        listbox = tk.Listbox(frankenstein_tab)
        listbox.grid(row=2, column=0, pady=10)
        
        # Create a button to add selected values
        add_button1 = ttk.Button(frankenstein_tab, text="Add",
                                command=lambda: self.add_to_group_list(combobox, group_keys, listbox, mode=False))
        add_button1.grid(row=3, column=0, padx=60, pady=5, sticky=tk.W)
        
        # Create labels
        label2 = ttk.Label(frankenstein_tab, text="Select columns to be aggregated on:")
        label2.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        applied_keys = []
        combobox2 = ttk.Combobox(frankenstein_tab, values=columns)
        combobox2.grid(row=1, column=1, padx=20, pady=5)
        
        # Create a box to display selected columns
        listbox2 = tk.Listbox(frankenstein_tab)
        listbox2.grid(row=2, column=1, pady=10)
        
        # Create a button to add selected values
        add_button2 = ttk.Button(frankenstein_tab, text="Add",
                                command=lambda: self.add_to_group_list(combobox2, applied_keys, listbox2, mode=False))
        add_button2.grid(row=3, column=1, padx=80, pady=5, sticky=tk.W)
        
        # Create labels
        label3 = ttk.Label(frankenstein_tab, text="Select aggregation mode:")
        label3.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        modes = ["max", "min", "mean", "sum", "count"]
        selected_modes = []
        combobox3 = ttk.Combobox(frankenstein_tab, values=modes)
        combobox3.grid(row=1, column=2, padx=20, pady=5)
        
        # Create a box to display selected columns
        listbox3 = tk.Listbox(frankenstein_tab)
        listbox3.grid(row=2, column=2, pady=10)
        
        # Create a button to add selected values
        add_button3 = ttk.Button(frankenstein_tab, text="Add",
                                command=lambda: self.add_to_group_list(combobox3, selected_modes, listbox3, mode=True))
        add_button3.grid(row=3, column=2, padx=80, pady=5, sticky=tk.W)
        
        # Create a button to clear selected columns
        clear_button = ttk.Button(frankenstein_tab, text="Reset",
                                command=lambda: self.clear_values(listbox, listbox2, listbox3))
        clear_button.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)
        
        # Create a button to execute specified aggregation function
        exe_button = ttk.Button(frankenstein_tab, text="Execute",
                                command=lambda: self.execute(dataframe, group_keys, applied_keys, selected_modes))
        exe_button.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)
        
    def add_to_group_list(self, combobox, selected_values, listbox, mode=False):
        """
        Parameters:
        - dataframe: Dataframe passed from the previous component
        - combobox: The comobbox widget
        - selected_values: The selected values from dropdown menu 
        - listbox: The display box 
        - mode: If this is a function for mode selection
        """
        selected_value = combobox.get()
        if mode:
            if selected_value not in selected_values:
                selected_values.append(selected_value)
                self.update_listbox(selected_values, listbox)
        else:
            selected_values.append(selected_value)
            self.update_listbox(selected_values, listbox)

    def update_listbox(self, selected_values, listbox):
        """
        Parameters:
        - selected_values: The selected values from dropdown menu 
        - listbox: The display box 
        """
        listbox.delete(0, tk.END)
        for value in selected_values:
            listbox.insert(tk.END, value)
        
    def clear_values(self, listbox1, listbox2, listbox3):
        """
        Parameters:
        - listbox1: The display box for group columns
        - listbox2: The display box for aggregation columns
        - listbox3: The display box for mode selection 
        """
        listbox1.delete(0, tk.END)
        listbox2.delete(0, tk.END)
        listbox3.delete(0, tk.END)
        
    def execute(self, group_keys, applied_keys, selected_mode):
        """
        Parameters:
        - dataframe: Dataframe passed from the previous component
        - group_keys: Selected columns to be grouped
        - applied_keys: The selected columns to be aggregated on 
        - selected_mode: Selcted modes corresponding to the applied columns
        
        Returns:
        - new_df: An aggregated dataframe
        """
        dataframe = self.app_instance.get_dataframe()
        if group_keys and applied_keys and not selected_mode == "Mode: None":
            try:    
                new_df = fc.aggregate(dataframe, group_keys, applied_keys, selected_mode)
                self.app_instance.update_dataframe(new_df)
                messagebox.showinfo("Columns Aggregated", "Selected columns have been aggregated.")
            except ValueError:
                messagebox.showwarning("Aggregation Failed", "Selected columns have not beed aggregated properly!")
        else:
            messagebox.showwarning("Aggregation Failed", "Invalid input, please double check")