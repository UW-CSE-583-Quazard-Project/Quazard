import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

def create_frankenstein_tab(tab_control):
    frankenstein_tab = ttk.Frame(tab_control)
    tab_control.add(frankenstein_tab, text='Frankenstein')
    
    label_frankenstein = ttk.Label(frankenstein_tab, text='This is the Frankenstein Tab')
    label_frankenstein.pack(padx=10, pady=10)