import tkinter.ttk as ttk

def create_janitor_tab(tab_control):
    janitor_tab = ttk.Frame(tab_control)
    tab_control.add(janitor_tab, text='Janitor')
    
    # Create text entry widgets within the frame
    label1 = ttk.Label(janitor_tab, text="Entry 1:")
    entry1 = ttk.Entry(janitor_tab)

    label1.pack(padx=10, pady=10)
    entry1.pack(pady=10)
    
    label2 = ttk.Label(janitor_tab, text="Entry 2:")
    entry2 = ttk.Entry(janitor_tab)

    label2.pack(padx=10, pady=10)
    entry2.pack(pady=10)
    
    