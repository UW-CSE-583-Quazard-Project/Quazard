import tkinter as tk
from tkinter import ttk, simpledialog

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

def create_decapitator_tab(tab_control):
    decapitator_tab = ttk.Frame(tab_control)
    tab_control.add(decapitator_tab, text='Decapitator')
    
    label_decapitator = ttk.Label(decapitator_tab, text='This is the Decapitator Tab')
    label_decapitator.pack(padx=10, pady=10)

def create_executioner_tab(tab_control):
    executioner_tab = ttk.Frame(tab_control)
    tab_control.add(executioner_tab, text='Executioner')
    
    label_executioner = ttk.Label(executioner_tab, text='This is the Executioner Tab')
    label_executioner.pack(padx=10, pady=10)

def create_janitor_tab(tab_control):
    janitor_tab = ttk.Frame(tab_control)
    tab_control.add(janitor_tab, text='Janitor')
    
    label_janitor = ttk.Label(janitor_tab, text='This is the Janitor Tab')
    label_janitor.pack(padx=10, pady=10)

def create_frankenstein_tab(tab_control):
    frankenstein_tab = ttk.Frame(tab_control)
    tab_control.add(frankenstein_tab, text='Frankenstein')
    
    label_frankenstein = ttk.Label(frankenstein_tab, text='This is the Frankenstein Tab')
    label_frankenstein.pack(padx=10, pady=10)

def create_converter_tab(tab_control):
    converter_tab = ttk.Frame(tab_control)
    tab_control.add(converter_tab, text='Long-wide Converter')
    
    label_converter = ttk.Label(converter_tab, text='This is the Long-wide Converter Tab')
    label_converter.pack(padx=10, pady=10)

def create_outputer_tab(tab_control):
    outputer_tab = ttk.Frame(tab_control)
    tab_control.add(outputer_tab, text='Outputer')
    
    label_outputer = ttk.Label(outputer_tab, text='This is the Outputer Tab')
    label_outputer.pack(padx=10, pady=10)

def on_button_click():
    print("Button clicked!")

def main():
    root = tk.Tk()
    root.title('Seven Tabbed GUI')

    tab_control = ttk.Notebook(root)

    create_reader_tab(tab_control)
    create_decapitator_tab(tab_control)
    create_executioner_tab(tab_control)
    create_janitor_tab(tab_control)
    create_frankenstein_tab(tab_control)
    create_converter_tab(tab_control)
    create_outputer_tab(tab_control)

    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == "__main__":
    main()
