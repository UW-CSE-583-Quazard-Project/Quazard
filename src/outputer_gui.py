import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

def create_outputer_tab(tab_control):
    outputer_tab = ttk.Frame(tab_control)
    tab_control.add(outputer_tab, text='Outputer')
    
    label_outputer = ttk.Label(outputer_tab, text='This is the Outputer Tab')
    label_outputer.pack(padx=10, pady=10)