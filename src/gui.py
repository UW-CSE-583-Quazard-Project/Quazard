import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
# import pandas as pd
# import numpy as np
import reader_gui, decapitator_gui, executioner_gui, longwideconverter_gui, janitor_gui, frankenstein_gui, outputer_gui
def main():
    root = tk.Tk()
    root.title('Seven Tabbed GUI')
    
    tab_control = ttk.Notebook(root)
    
    reader_gui.create_reader_tab(tab_control)
    decapitator_gui.create_decapitator_tab(tab_control)
    executioner_gui.create_executioner_tab(tab_control)
    longwideconverter_gui.create_converter_tab(tab_control)
    janitor_gui.create_janitor_tab(tab_control)
    frankenstein_gui.create_frankenstein_tab(tab_control)
    outputer_gui.create_outputer_tab(tab_control)

    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == "__main__":
    main()

