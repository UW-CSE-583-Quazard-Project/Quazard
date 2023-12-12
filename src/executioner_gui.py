import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import executioner as exe

class Executioner:
    def __init__(self):
        pass

    def create_executioner_tab(self, tab_control, file):
        # Canvas for scroll bar
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        executioner_tab = ttk.Frame(tab_control)
        tab_control.add(executioner_tab, text='Executioner')
    
        # Create a Canvas widget within the tab's frame
        canvas = tk.Canvas(executioner_tab)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(executioner_tab, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure canvas and scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Create a frame to contain the scrollable content
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

        label_executioner = ttk.Label(scrollable_frame, text='This is the Executioner Tab.\n \
                                      Here you can remove rows based on a number of parameters\n \
                                      Please make sure your dataset has only one header. \
                                      If not, use decapitator first.')
        label_executioner.pack(padx=10, pady=10)

        #### Upon Submission ####
        def submit(file):
            # participant ID
            response_id_column = entry_id.get()
            ## Preview ##
            # Update the 'preview statemachine' variable based on checkbox state
            previewSM = var_preview_checkbox.get()
            # Get the text entries
            status_column = entry_previewtext_status.get()
            if previewSM == 1:
                # Check if any of the arguments are empty
                if not (status_column):
                    messagebox.showerror("Error", "Status column cannot be empty.")
                    return None
                # run the executioner
                mylist = exe.executioner_preview(file, response_id_column, status_column)
                file =  mylist[0]
                messagebox.showinfo("Success!", f"{mylist[2]} participants/rows removed for being survey previews.\
                                    Here are their IDs:{mylist[1]}")
                print(f"{mylist[2]} participants/rows removed for being survey previews. Here are their IDs")
                print(mylist[1])

            
            ## Completion ##
            # Update the 'completion statemachine' variable based on checkbox state
            completionSM = var_finished_checkbox.get()
            # Get the text entries
            finished_column = entry_finished.get()
            if completionSM == 1:
                # Check if any of the arguments are empty
                if not (finished_column):
                    messagebox.showerror("Error", "Finished column cannot be empty.")
                    return None
                # run the executioner
                mylist = exe.executioner_completion(file, response_id_column, finished_column)
                file =  mylist[0]
                messagebox.showinfo("Success!", f"{mylist[2]} unfinished participants/rows removed. Here are their IDs:{mylist[1]}")
                print(f"{mylist[2]} unfinished participants/rows removed. Here are their IDs")
                print(mylist[1])
                
            
            ## Recaptcha ##
            # Update the 'completion statemachine' variable based on checkbox state
            recaptchaSM = var_recap.get()
            if recaptchaSM == 1:
                recaptchaequalSM = var_equal.get()
                recaptchamissingSM = var_missing.get()
                # Get the column and threshold
                recaptcha_id_column = entry_recap_col.get()
                threshold = float(entry_recap_threshold.get())
                # Check if any of the arguments are empty
                if not (recaptcha_id_column and threshold):
                    messagebox.showerror("Error", "Recaptcha column and threshold cannot be empty.")
                    return None
                # run the executioner
                mylist = exe.executioner_recaptcha(file, 
                                            response_id_column, 
                                            recaptcha_id_column,
                                            threshold,
                                            recaptchaequalSM,
                                            recaptchamissingSM
                                                )
                file =  mylist[0]
                messagebox.showinfo("Success!", f"{mylist[2]} participants/rows removed based on recaptcha scores. Here are their IDs:{mylist[1]}")
                print(f"{mylist[2]} participants/rows removed based on recaptcha scores. Here are their IDs")
                print(mylist[1])
                

            ## Attention Check Multiple Choice ##
            # Update the 'acmp statemachine' variable based on checkbox state
            attentioncheckMPSM = var_acmp.get()
            if attentioncheckMPSM == 1:
            # Get the text entries
                attentioncheck_mp = entry_acmp_col.get()
                temp = str(entry_acmp_answer.get())
                temp = [s.strip().strip("'") for s in temp.split(',')]
                right_answer = [int(x) for x in temp]
                # Check if any of the arguments are empty
                if not (attentioncheck_mp and right_answer):
                    messagebox.showerror("Error", "Attention check column and right answer cannot be empty.")
                    return None
                # run the executioner
                mylist = exe.executioner_attentioncheck_multiplechoice(file, 
                                            response_id_column, 
                                            attentioncheck_mp,
                                            right_answer
                                                )
                file =  mylist[0]
                messagebox.showinfo("Success!", f"{mylist[2]} participants/rows removed based on a multiple choice attention check. Here are their IDs:{mylist[1]}")
                print(f"{mylist[2]} participants/rows removed based on a multiple choice attention check. Here are their IDs")
                print(mylist[1])
                
            
            ## Attention Check Text Entry ##
            # Update the 'acte statemachine' variable based on checkbox state
            attentioncheckTESM = var_acte.get()
            if attentioncheckTESM == 1:
                acte_checkbox_report.set(var_acte_report.get())
                # Get the text entries
                attentioncheck_text = entry_acmp_col.get()
                reportonly = acte_checkbox_report
                temp = str(entry_acte_answer.get())
                right_answer = [s.strip().strip("'") for s in temp.split(',')]
                # Check if any of the arguments are empty
                if not (attentioncheck_text and right_answer):
                    messagebox.showerror("Error", "Attention check column and right answer cannot be empty.")
                    return None
                # run the executioner
                mylist = exe.executioner_attentioncheck_text(file, 
                                            response_id_column, 
                                            attentioncheck_text,
                                            right_answer,
                                            reportonly
                                                )
                file =  mylist[0]
                messagebox.showinfo("Success!", f"{mylist[2]} participants/rows removed based on a text entry attention check. Here are their IDs:{mylist[1]}")
                print(f"{mylist[2]} participants/rows removed based on a text entry attention check. Here are their IDs")
                print(mylist[1])
            return file
        #### Interface ####

        ### General Paramters ###
        # Create an input text entry for response id
        label_id = tk.Label(scrollable_frame, text="Enter the column name for response id column.\nYou must have this parameter for any function on this page.\nIf you are unsure, please go to the output tab and print out the CSV to check")
        label_id.pack()
        entry_id = tk.Entry(scrollable_frame)
        entry_id.pack()

        ### Suvery Preview Removal ###
        # Initialize the variable 'previewSM' as a BooleanVar.
        # This indicates whether we should remove rows that were survey preview
        previewSM = tk.BooleanVar()
        ## Create Label
        label_preview = ttk.Label(scrollable_frame, text='##### Suvery Preview Removal #####')
        label_preview.pack(padx=10, pady=10)

        # Create a checkbox
        var_preview_checkbox = tk.BooleanVar()
        preview_checkbox = tk.Checkbutton(scrollable_frame, text="Do you want to remove rows that are previews?", variable=var_preview_checkbox)
        preview_checkbox.pack()

        # Create an input text entry for status
        label_previewtext_status = tk.Label(scrollable_frame, text="Enter the column name for the stauts column. ")
        label_previewtext_status.pack()
        entry_previewtext_status = tk.Entry(scrollable_frame)
        entry_previewtext_status.pack()

        ### Completion Removal ###
        # Initialize the variable 'completionSM' as a BooleanVar
        # This indicates whether we should remove rows that were incomplete
        completionSM = tk.BooleanVar()

        ## Create Label
        label_finished = ttk.Label(scrollable_frame, text='##### Unfinished Participants Removal #####')
        label_finished.pack(padx=10, pady=10)

        # Create a checkbox
        var_finished_checkbox = tk.BooleanVar()
        finished_checkbox = tk.Checkbutton(scrollable_frame, text="Do you want to remove unfinished rows/participants?", variable=var_finished_checkbox)
        finished_checkbox.pack()

        # Create an input text entry for the finished column
        label_finished = tk.Label(scrollable_frame, text="Enter the column name for the 'finished' column. It should have TRUE and FALSE as values. ")
        label_finished.pack()
        entry_finished = tk.Entry(scrollable_frame)
        entry_finished.pack()

        ### Recaptcha Removal ###
        # Initialize the variable 'recaptchaSM' as a BooleanVar
        # This indicates whether we should remove rows based on recaptcha scores
        recaptchaSM = tk.BooleanVar()
        recaptchaequalSM = tk.BooleanVar()
        recaptchamissingSM = tk.BooleanVar()
        ## Create Label
        label_recap = ttk.Label(scrollable_frame, text='##### Participant Removal Based on Recaptcha Scores #####')
        label_recap.pack(padx=10, pady=10)

        # Create a checkbox for whether to do this function
        var_recap = tk.BooleanVar()
        recap_checkbox = tk.Checkbutton(scrollable_frame, text="Do you want to remove rows/participants based on recaptcha scores?", variable=var_recap)
        recap_checkbox.pack()

        # Create a checkbox for the equal value argument
        var_equal = tk.BooleanVar()
        recap_checkbox_equal = tk.Checkbutton(scrollable_frame, text="Do you want to keep participants with scores equal to the threshold?\nBy default only those above the threshold will be kept.", variable=var_equal)
        recap_checkbox_equal.pack()

        # Create a checkbox for the missing value argument
        var_missing = tk.BooleanVar()
        recap_checkbox_missing = tk.Checkbutton(scrollable_frame, text="Do you want to keep participants who do not have a score?", variable=var_missing)
        recap_checkbox_missing.pack()

        # Create an input text entry for the recaptcha score column
        label_recap_col = tk.Label(scrollable_frame, text="Enter the column name for the 'recaptcha score' column. ")
        label_recap_col.pack()
        entry_recap_col = tk.Entry(scrollable_frame)
        entry_recap_col.pack()
        
        # Create an input text entry for the threshold
        # First enables validation
        validate_func = executioner_tab.register(self.validate_input)
        label_recap_threshold = tk.Label(scrollable_frame, text="Enter the recaptcha threshold above which participants/rows will be kept.\nMust be a number between 0 and 1. For example: 0.5")
        label_recap_threshold.pack()
        entry_recap_threshold = tk.Entry(scrollable_frame, validate="key", validatecommand=(validate_func, '%P'))
        entry_recap_threshold.pack()

        ### Attention Check Multiple Choice Removal ###
        # Initialize the variable 'attentioncheckMPSM' as a BooleanVar
        # This indicates whether we should remove rows based on a multiple choice attention check
        attentioncheckMPSM = tk.BooleanVar()

        ## Create Label
        label_acmp = ttk.Label(scrollable_frame, text='##### Participant Removal Based on Multiple Choice Attention Check #####')
        label_acmp.pack(padx=10, pady=10)

        # Create a checkbox for whether to do this function
        var_acmp = tk.BooleanVar()
        acmp_checkbox = tk.Checkbutton(scrollable_frame, text="Do you want to remove rows/participants based on a multiple choice attention check?\nIf you have more than one multiple choice attention check, you can submit this tab more than once.", variable=var_acmp)
        acmp_checkbox.pack()

        # Create an input text entry for the attention check column
        label_acmp_col = tk.Label(scrollable_frame, text="Enter the column name for the attention check column. ")
        label_acmp_col.pack()
        entry_acmp_col = tk.Entry(scrollable_frame)
        entry_acmp_col.pack()

        # Create an input text entry for the right answer
        label_acmp_answer = tk.Label(scrollable_frame, text="Enter the right answer(s) as numbers, not text.\nSelect 'Use Numeric Values' when downloading from qualtrics.\nSeperate each number with a coma with no space after, like this:\n1,2,3")
        label_acmp_answer.pack()
        entry_acmp_answer = tk.Entry(scrollable_frame)
        entry_acmp_answer.pack()

        ### Attention Check Text Entry Removal ###
        # Initialize the variable 'attentioncheckMPSM' as a BooleanVar
        # This indicates whether we should remove rows based on a multiple choice attention check
        attentioncheckTESM = tk.BooleanVar()
        attentioncheckTESM_reportonly = tk.BooleanVar()

        ## Create Label
        label_acte = ttk.Label(scrollable_frame, text='##### Participant Removal Based on Text Entry Attention Check #####')
        label_acte.pack(padx=10, pady=10)

        # Create a checkbox for whether to do this function
        var_acte = tk.BooleanVar()
        acte_checkbox = tk.Checkbutton(scrollable_frame, text="Do you want to remove rows/participants based on a text entry attention check?\nIf you have more than one text entry attention check, you can submit this tab more than once.", variable=var_acte)
        acte_checkbox.pack()

        # Create a checkbox for report only argument
        var_acte_report = tk.BooleanVar()
        acte_checkbox_report = tk.Checkbutton(scrollable_frame, text="Do you want to only report the participants with mismatch answers instead of removing them? You can manually check and remove them based on the report.", variable=var_acte_report)
        acte_checkbox_report.pack()

        # Create an input text entry for the attention check column
        label_acte_col = tk.Label(scrollable_frame, text="Enter the column name for the attention check column. ")
        label_acte_col.pack()
        entry_acte_col = tk.Entry(scrollable_frame)
        entry_acte_col.pack()

        # Create an input text entry for the right answer
        label_acte_answer = tk.Label(scrollable_frame, text="Enter the right answer(s). Each answer should be covered by single quote marks and seperated with comma, like this:\n'apple','orange','banana'")
        label_acte_answer.pack()
        entry_acte_answer = tk.Entry(scrollable_frame)
        entry_acte_answer.pack()

        #### At the end ####
        # Create a Button to submit the tab
        button_submit = tk.Button(scrollable_frame, text="Submit", command=submit)
        button_submit.pack()

        # return file so that other tabs can do something with it.
        return file

    def validate_input(self, new_value):
        if new_value == "":
            return True

        try:
            float(new_value)
            return True
        except ValueError:
            return False