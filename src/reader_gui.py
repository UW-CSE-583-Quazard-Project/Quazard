"""
Module for Reader GUI component
Allows user to read the selected csv raw data file
by interacting with the GUI
"""
import tkinter.ttk as ttk
from tkinter import ttk
from tkinter import filedialog as fd
import reader as rd

class ReaderGUI:
    """ 
    A GUI class for the reader functionality
    It will read the selected file as a dataframe and pass them to other components

    Parameters:
    - app_instance: An instance of the main application class.

    Usage:
    - Create an instance of this class, passing the main application instance.
    - Use the created instance to create the Decapitator tab within the application GUI.
    """
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def create_reader_tab(self, tab_control):
        """    
        Parameters:
        - tab_control: The upper layer control from the main GUI
        """
        reader_tab = ttk.Frame(tab_control)
        tab_control.add(reader_tab, text='Reader')
        
        label_reader = ttk.Label(reader_tab, text='This is the Reader Tab')
        label_reader.pack(padx=10, pady=10)

        # file_name = self.get_file_name()
        label_file_name = ttk.Label(reader_tab, text=f'File Name: "Test"')
        label_file_name.pack(pady=10)

        button_reader = ttk.Button(reader_tab, text='Select File', command=self.on_button_click)
        button_reader.pack(pady=10)        
        
    def on_button_click(self):
        filetypes = (('csv files', '*.csv'),
                    ('All files', '*.*'))
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        dataframe = rd.reader(filename)
        self.app_instance.update_dataframe(dataframe)