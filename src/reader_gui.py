"""
This is the module to handle the GUI tab for Reader
"""
import tkinter.ttk as ttk
from tkinter import ttk
from tkinter import filedialog as fd
import reader as rd

class ReaderGUI:
    def __init__(self, app_instance):
        self.app_instance = app_instance
    
    # def get_file_name(self):
    #     file_name = simpledialog.askstring("Input", "Enter file name:")
    #     return file_name

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

        label_reader_threeheader = ttk.Label(reader_tab, text='Use this button if your data has three rows of header \n'
                                             ' and will need to go through the decapitator')
        label_reader_threeheader.pack(padx=10, pady=10)

        button_reader = ttk.Button(reader_tab, text='Select File', command=self.on_button_click)
        button_reader.pack(pady=10)

        label_reader_oneheader = ttk.Label(reader_tab, text='Use this button if your data has one row of header \n'
                                             ' and will not go through the decapitator')
        label_reader_oneheader.pack(padx=10, pady=10)

        button_reader_header = ttk.Button(reader_tab, text='Select File', command=self.on_button_click_one_header)
        button_reader_header.pack(pady=10)              
        
    def on_button_click(self):
        filetypes = (('csv files', '*.csv'),
                    ('All files', '*.*'))
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        dataframe = rd.reader(filename)
        self.app_instance.update_dataframe(dataframe)

    def on_button_click_one_header(self):
        filetypes = (('csv files', '*.csv'),
                    ('All files', '*.*'))
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        dataframe = rd.reader_oneheader(filename)
        self.app_instance.update_dataframe(dataframe)