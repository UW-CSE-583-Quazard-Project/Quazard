import tkinter.ttk as ttk
from tkinter import ttk, simpledialog, messagebox

def get_file_name():
    file_name = simpledialog.askstring("Input", "Enter file name:")
    return file_name

def create_reader_tab(tab_control):
    reader_tab = ttk.Frame(tab_control)
    tab_control.add(reader_tab, text='Reader')
    
    label_reader = ttk.Label(reader_tab, text='This is the Reader Tab')
    label_reader.pack(padx=10, pady=10)

    file_name = get_file_name()
    label_file_name = ttk.Label(reader_tab, text=f'File Name: {file_name}')
    label_file_name.pack(pady=10)

    button_reader = ttk.Button(reader_tab, text='Click me!', command=on_button_click)
    button_reader.pack(pady=10)
    
def on_button_click():
    print("Button clicked!")