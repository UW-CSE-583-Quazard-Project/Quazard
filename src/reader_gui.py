import tkinter.ttk as ttk
from tkinter import ttk, simpledialog
import reader as rd

class ReaderGUI:
    def __init__(self):
        pass
    
    def get_file_name(self):
        file_name = simpledialog.askstring("Input", "Enter file name:")
        return file_name

    def create_reader_tab(self, tab_control):
        reader_tab = ttk.Frame(tab_control)
        tab_control.add(reader_tab, text='Reader')
        
        label_reader = ttk.Label(reader_tab, text='This is the Reader Tab')
        label_reader.pack(padx=10, pady=10)

        # file_name = self.get_file_name()
        label_file_name = ttk.Label(reader_tab, text=f'File Name: "Test"')
        label_file_name.pack(pady=10)

        button_reader = ttk.Button(reader_tab, text='Test Button', command=self.on_button_click)
        button_reader.pack(pady=10)
        
        # return rd.reader(file_name)
        
        
    def on_button_click(self):
        print("Button clicked!")