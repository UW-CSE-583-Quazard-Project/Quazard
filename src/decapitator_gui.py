import tkinter.ttk as ttk
import decapitator
def create_decapitator_tab(tab_control):
    decapitator_tab = ttk.Frame(tab_control)
    tab_control.add(decapitator_tab, text='Decapitator')
    
    label_decapitator = ttk.Label(decapitator_tab, text='This is the Decapitator Tab. You can choose which ')
    label_decapitator.pack(padx=10, pady=10)