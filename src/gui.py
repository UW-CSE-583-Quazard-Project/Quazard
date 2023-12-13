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
        reader = reader_gui.ReaderGUI(self)
        decapitator = decapitator_gui.DecapitatorGUI(self)
        executioner = executioner_gui.Executioner(self)
        converter = longwideconverter_gui.LongWideConverter(self)
        janitor = janitor_gui.JanitorGUI(self)
        frankenstein = frankenstein_gui.FrankensteinGUI(self)
        outputer = outputer_gui.OutputerGUI(self) 
        
        reader.create_reader_tab(tab_control)
        decapitator.create_decapitator_tab(tab_control)
        executioner.create_executioner_tab(tab_control)
        converter.create_converter_tab(tab_control)
        janitor.create_janitor_tab(tab_control)
        frankenstein.create_frankenstein_tab(tab_control)
        outputer.create_outputer_tab(tab_control)
        
        tab_control.pack(expand=1, fill='both')
        root.mainloop()
    
    def update_dataframe(self, dataframe):
        self.dataframe = dataframe
        print("Dataframe updated in App class:", self.dataframe)
        # Now you can pass self.dataframe to other instances of other classes
        
    def get_dataframe(self):
        print(f"Current dataframe: {self.dataframe}")
        return self.dataframe


def main():
    app = App()
    app.run()
    

if __name__ == "__main__":
    main()

