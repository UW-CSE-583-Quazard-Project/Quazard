"""
Module for Janitor GUI component
Allows user to drop unwanted columns
by interacting with the GUI 
"""
import tkinter as tk
import tkinter.ttk as ttk
import janitor
import pandas as pd
from tkinter import messagebox

class JanitorGUI:
    """ 
    A GUI class for the Janitor functionality (drop selected columns).

    Parameters:
    - app_instance: An instance of the main application class.

    Usage:
    - Create an instance of this class, passing the main application instance.
    - Use the created instance to create the Decapitator tab within the application GUI.
    """
    def __init__(self, app_instance):
        self.app_instance = app_instance
        self.options = ["a", "b", "c"]

    def create_janitor_tab(self, tab_control, dataframe=None):
        """    
        Parameters:
        - tab_control: The upper layer control from the main GUI
        - dataframe: The dataframe passed from previous component
        """
        janitor_tab = ttk.Frame(tab_control)
        tab_control.add(janitor_tab, text='Janitor')

        label_janitor_top = ttk.Label(janitor_tab, text='This is the Janitor Tab.\n \
                                        Here you can drop unwanted columns')
        label_janitor_top.grid(padx=10, pady=10)

        # Create a Frame for three columns
        frame_columns = tk.Frame(janitor_tab)
        frame_columns.grid(row=1, column=0, padx=10, pady=10)

        # Create a button to add refresh data
        add_button1 = ttk.Button(frame_columns, text="Refresh Data",
                                command=lambda: self.refresh())
        add_button1.grid(row=0, column=0, padx=60, pady=5, sticky=tk.W)
        if self.app_instance.get_dataframe():
            self.options = self.app_instance.get_dataframe().columns.tolist()
        
        # Create labels
        label1 = ttk.Label(frame_columns, text="Select columns to be dropped:")
        label1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        # Create a dropmenu with options of dataframe columns
        self.selected_values = []
        self.combobox = ttk.Combobox(frame_columns, values=self.options)
        self.combobox.grid(row=2, column=0, padx=20, pady=20, sticky=tk.W)
        
        # Create a box to display selected columns
        listbox = tk.Listbox(frame_columns)
        listbox.grid(row=3, column=0, padx=30, pady=10, sticky=tk.W)
        
        # # Create a button to add selected values
        add_button1 = ttk.Button(frame_columns, text="Add",
                                command=lambda: self.add_to_list(self.combobox, self.selected_values, listbox))
        add_button1.grid(row=4, column=0, padx=60, pady=5, sticky=tk.W)
                
        # Create a button to submit selected values
        drop_button = ttk.Button(frame_columns, text="Drop Selected Columns",
                                command=lambda: self.drop_selected_columns(self.selected_values))
        drop_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Create a button to clear selected columns
        clear_button = ttk.Button(frame_columns, text="Clear List", command=lambda: self.clear_list(listbox))
        clear_button.grid(row=2, column=1, padx=10, pady=10)
    
    def refresh(self):
        """
        Refreshes the current dataframe
        """
        self.options = self.app_instance.get_dataframe().columns.tolist()
        self.combobox['values'] = self.options
    
    def add_to_list(self, combobox, selected_values, listbox):
        """
        Parameters:
        - combobox: The comobbox widget
        - selected_values: The selected values from dropdown menu 
        - listbox: The display box 
        """
        selected_value = combobox.get()
        if selected_value not in selected_values:
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
            
    def clear_list(self, listbox):
        """
        Parameters:
        - listbox: The display box for columns to be dropped
        """
        listbox.delete(0, tk.END)
        self.selected_values = []
        
    def drop_selected_columns(self, selected_values):
        """
        Parameters:
        - listbox: The display box for columns to be dropped
        
        Returns:
        - new_dataframe: The new dataframe without selected columns
        """
        dataframe = self.app_instance.get_dataframe()
        if selected_values:
            try:
                new_dataframe = janitor.drop_cols(dataframe, selected_values)
                messagebox.showinfo("Columns Dropped", "Selected columns have been dropped.")
                self.app_instance.update_dataframe(new_dataframe)
            except ValueError:
                messagebox.showwarning("Dropping Failed", "Selected columns have not beed dropped properly!")
        else:
            messagebox.showwarning("Dropping Failed", "Invalid input!")