import tkinter.ttk as ttk

def create_decapitator_tab(tab_control):
    decapitator_tab = ttk.Frame(tab_control)
    tab_control.add(decapitator_tab, text='Decapitator')
    
    label_decapitator = ttk.Label(decapitator_tab, text='This is the Decapitator Tab')
    label_decapitator.pack(padx=10, pady=10)