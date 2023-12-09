import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

def create_converter_tab(tab_control):
    converter_tab = ttk.Frame(tab_control)
    tab_control.add(converter_tab, text='Long-wide Converter')
    
    label_converter = ttk.Label(converter_tab, text='This is the Long-wide Converter Tab')
    label_converter.pack(padx=10, pady=10)