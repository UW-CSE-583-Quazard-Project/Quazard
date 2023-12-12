"""
This is the main module for our application GUI
"""
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import reader_gui, decapitator_gui, executioner_gui, longwideconverter_gui, janitor_gui, frankenstein_gui, outputer_gui

class App:
    def __init__(self):
        self.dataframe = None
        
    def run(self):
        root = tk.Tk()
        root.title('Seven Tabbed GUI')
        tab_control = ttk.Notebook(root)
        reader = reader_gui.ReaderGUI()
        decapitator = decapitator_gui.DecapitatorGUI()
        
        reader.create_reader_tab(tab_control)
        # reader_gui.create_reader_tab(tab_control)
        decapitator.create_decapitator_tab(tab_control)
        
        executioner_gui.create_executioner_tab(tab_control)
        longwideconverter_gui.create_converter_tab(tab_control)
        janitor_gui.create_janitor_tab(tab_control)
        frankenstein_gui.create_frankenstein_tab(tab_control)
        outputer_gui.create_outputer_tab(tab_control)
        tab_control.pack(expand=1, fill='both')
        root.mainloop()


def main():
    app = App()
    app.run()
    

if __name__ == "__main__":
    main()

