"""
Module for frankenstein GUI component
Allows user to aggregate expected columns from the data
by selecting columns
"""
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import frankenstein as fc

class FrankensteinGUI:
    """ 
    A GUI class for the aggregation functionality.

    Parameters:
    - app_instance: An instance of the main application class.

    Usage:
    - Create an instance of this class, passing the main application instance.
    - Use the created instance to create the Decapitator tab within the application GUI.
    """
    def __init__(self, app_instance):
        self.app_instance = app_instance
        self.options = ["a", "b", "c"]
        
    def create_frankenstein_tab(self, tab_control):
        """    
        Parameters:
        - tab_control: The upper layer control from the main GUI
        """
        frankenstein_tab = ttk.Frame(tab_control)
        tab_control.add(frankenstein_tab, text='Frankenstein')

        label_frankenstein_top = ttk.Label(frankenstein_tab, text="This is the Frankenstein Tab.\n"
                                        "Here you can conduct aggregation on your dataset\n"
                                        "Please make sure your dataset has only one header.\n"
                                        "If not, use decapitator first."
                                        "If your dataset has repeated measures/multiple trials, please "
                                        "use the long-wide converter first \n"
                                        "Refresh the data first\n"
                                        "NOTE: The aggregated dataset will ONLY have the columns you selected here\n"
                                        "Therefore it is recommended to output and save your data first")
        label_frankenstein_top.grid(row=0, column=0, padx=10, pady=10)
        
        # Create a Frame for three columns
        frame_columns = tk.Frame(frankenstein_tab)
        frame_columns.grid(row=1, column=0, padx=10, pady=10)

        # Create labels
        label1 = ttk.Label(frame_columns, text="Select columns to be grouped:")
        label1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        self.group_keys = []
        self.combobox = ttk.Combobox(frame_columns, values=self.options)
        self.combobox.grid(row=2, column=0, padx=20, pady=5)
        
        # Create a box to display selected columns
        listbox = tk.Listbox(frame_columns)
        listbox.grid(row=3, column=0, pady=10)
        
        # Create a button to add selected values
        add_button1 = ttk.Button(frame_columns, text="Add",
                                command=lambda: self.add_to_group_list(self.combobox, self.group_keys, listbox, mode=False))
        add_button1.grid(row=4, column=0, padx=60, pady=5, sticky=tk.W)
        
        # Create labels
        label2 = ttk.Label(frame_columns, text="Select columns to be aggregated on:")
        label2.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        self.applied_keys = []
        self.combobox2 = ttk.Combobox(frame_columns, values=self.options)
        self.combobox2.grid(row=2, column=1, padx=20, pady=5)
        
        # Create a box to display selected columns
        listbox2 = tk.Listbox(frame_columns)
        listbox2.grid(row=3, column=1, pady=10)
        
        # Create a button to add selected values
        add_button2 = ttk.Button(frame_columns, text="Add",
                                command=lambda: self.add_to_group_list(self.combobox2, self.applied_keys, listbox2, mode=False))
        add_button2.grid(row=4, column=1, padx=80, pady=5, sticky=tk.W)
        
        # Create labels
        label3 = ttk.Label(frame_columns, text="Select aggregation mode:")
        label3.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        modes = ["max", "min", "mean", "sum", "count"]
        self.selected_modes = []
        self.combobox3 = ttk.Combobox(frame_columns, values=modes)
        self.combobox3.grid(row=2, column=2, padx=20, pady=5)
        
        # Create a box to display selected columns
        listbox3 = tk.Listbox(frame_columns)
        listbox3.grid(row=3, column=2, pady=10)
        
        # Create a button to add selected values
        add_button3 = ttk.Button(frame_columns, text="Add",
                                command=lambda: self.add_to_group_list(self.combobox3, self.selected_modes, listbox3, mode=True))
        add_button3.grid(row=4, column=2, padx=80, pady=5, sticky=tk.W)
        
        # Create a button to add refresh data
        ref_button1 = ttk.Button(frame_columns, text="Refresh Data",
                                command=lambda: self.refresh())
        ref_button1.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)
        
        # Create a button to clear selected columns
        clear_button = ttk.Button(frame_columns, text="Reset",
                                command=lambda: self.clear_values(listbox, listbox2, listbox3))
        clear_button.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)
        
        # Create a button to execute specified aggregation function
        exe_button = ttk.Button(frame_columns, text="Execute",
                                command=lambda: self.execute(self.group_keys, self.applied_keys, self.selected_modes))
        exe_button.grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)
    
    def refresh(self):
        """
        Refreshes the current dataframe
        """
        self.options = self.app_instance.get_dataframe().columns.tolist()
        self.combobox['values'] = self.options
        self.combobox2['values'] = self.options
       
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
        self.applied_keys = []
        self.group_keys = []
        self.selected_modes = []
        
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