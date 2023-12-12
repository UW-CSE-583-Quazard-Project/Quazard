"""
Executioner component testing
"""
import os
import numpy as np
import pandas as pd
import unittest
import random as rand

#our components
from src import executioner as exe

class TestExecutioner(unittest.TestCase):
    """
    Test class for executioner component
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure the functions run.
        """
        df = pd.DataFrame({'ID': ["A", "B", "C", "D"],
                    'status':   [np.random.choice(["Survey Preview", "IP","IP"]), 
                                np.random.choice(["Survey Preview", "IP","IP"]), 
                                 np.random.choice(["Survey Preview", "IP","IP"]), 
                                 np.random.choice(["Survey Preview", "IP","IP"])],
                    'recaptcha':[np.random.rand(), 
                                np.random.rand(), 
                                np.random.rand(), 
                                np.random.rand()],
                    'finished':[np.random.choice(["TRUE", "FALSE"]), 
                                np.random.choice(["TRUE", "FALSE"]), 
                                np.random.choice(["TRUE", "FALSE"]), 
                                np.random.choice(["TRUE", "FALSE"])],
                    'mp': [np.random.randint(1, 5), 
                           np.random.randint(1, 5), 
                           np.random.randint(1, 5), 
                           np.random.randint(1, 5)],
                    'te': [np.random.choice(["apple", "cat","car"]), 
                           np.random.choice(["apple", "cat","car"]), 
                           np.random.choice(["apple", "cat","car"]), 
                           np.random.choice(["apple", "cat","car"])]})
        df_origin = df
        # Get all necessary arguments
        threshold = np.random.rand()
        equal_score = bool(np.random.choice([True, False]))
        missing_score = bool(np.random.choice([True, False]))
        num_right_mp = np.random.randint(1, 2)
        right_answer_mp = np.random.randint(1, 5, size = num_right_mp)
        if type(right_answer_mp) != list:
            right_answer_mp = right_answer_mp.tolist()
        num_right_te = np.random.randint(1, 2)
        right_answer_te = np.random.choice(["apple", "cat","car"], size = num_right_te, replace = False)
        if type(right_answer_te) != list:
            right_answer_te = right_answer_te.tolist()
        reportonly = False
        
        # Run functions one by one
        exe.executioner_preview(df, 'ID', 'status')
        exe.executioner_completion(df, 'ID', 'finished')
        exe.executioner_recaptcha(df, 'ID', 'recaptcha', threshold, equal_score, missing_score)
        exe.executioner_attentioncheck_multiplechoice(df, 'ID', 'mp',right_answer_mp)
        exe.executioner_attentioncheck_text(df, 'ID', 'te',right_answer_te, reportonly)
        
        print("test successful")

    def test_one_shot(self):
        """
        One-shot test to check with a set of arguments
        """
        df = pd.DataFrame({'ID': ["A", "B", "C", "D"],
                    'status':   ["Survey Preview", 
                                "IP", 
                                "IP", 
                                "IP"],
                    'recaptcha':[0.1, 
                                0.5, 
                                np.nan, 
                                0.8],
                    'finished':["TRUE", 
                                "TRUE", 
                                "TRUE", 
                                "FALSE"],
                    'mp': [1, 
                           2, 
                           3, 
                           4],
                    'te': ["apple", 
                           "apple", 
                           "cat", 
                           "car"]})
        df_expected = pd.DataFrame({'ID': ["C"],
                    'status':   ["IP"],
                    'recaptcha':[np.nan],
                    'finished':["TRUE"],
                    'mp': [3],
                    'te': ["cat"]})
        # Get all necessary arguments
        threshold = 0.5
        equal_score = False
        missing_score = True
        right_answer_mp = [3,4]
        right_answer_te = ["cat","car"]
        reportonly = False
        
        # Run functions one by one
        temp = exe.executioner_preview(df, 'ID', 'status')
        df = temp[0]
        print(f'preview removed {temp[1]}')
        temp = exe.executioner_completion(df, 'ID', 'finished')
        df = temp[0]
        print(f'completion removed {temp[1]}')
        temp = exe.executioner_recaptcha(df, 'ID', 'recaptcha', threshold, equal_score, missing_score)
        df = temp[0]
        print(f'recaptcha removed {temp[1]}')
        temp = exe.executioner_attentioncheck_multiplechoice(df, 'ID', 'mp',right_answer_mp)
        df = temp[0]
        print(f'attention check multiple choice removed {temp[1]}')
        temp = exe.executioner_attentioncheck_text(df, 'ID', 'te',right_answer_te, reportonly)
        df = temp[0]
        print(f'attention check text entry removed {temp[1]}')

        # Reset index
        df = df.reset_index(drop=True)

        print('This is the output dataset')
        print(df)
        print('This is the expected dataset')
        print(df_expected)

        assert df.equals(df_expected), "DataFrames are not equal"
    
    def test_edge(self):
        """
        Edge test to check if the funciton could handle unwanted data type
        """
        df = pd.DataFrame({'ID': ["A", "B", "C", "D"],
                    'status':   ["Survey Preview", 
                                "IP", 
                                "IP", 
                                "IP"],
                    'recaptcha':[0.1, 
                                0.5, 
                                np.nan, 
                                0.8],
                    'finished':["TRUE", 
                                "hahaha", 
                                "TRUE", 
                                "FALSE"],
                    'mp': [1, 
                           2, 
                           3, 
                           4],
                    'te': ["apple", 
                           "apple", 
                           "cat", 
                           "car"]})
        df_expected = pd.DataFrame({'ID': ["C"],
                    'status':   ["IP"],
                    'recaptcha':[np.nan],
                    'finished':["TRUE"],
                    'mp': [3],
                    'te': ["cat"]})
        # Get all necessary arguments
        threshold = 0.5
        equal_score = False
        missing_score = True
        right_answer_mp = [3,4]
        right_answer_te = ["cat","car"]
        reportonly = False

        # Run functions one by one
        temp = exe.executioner_preview(df, 'ID', 'status')
        df = temp[0]
        print(f'preview removed {temp[1]}')
        temp = exe.executioner_completion(df, 'ID', 'finished')
        df = temp[0]
        print(f'completion removed {temp[1]}')
        temp = exe.executioner_recaptcha(df, 'ID', 'recaptcha', threshold, equal_score, missing_score)
        df = temp[0]
        print(f'recaptcha removed {temp[1]}')
        temp = exe.executioner_attentioncheck_multiplechoice(df, 'ID', 'mp',right_answer_mp)
        df = temp[0]
        print(f'attention check multiple choice removed {temp[1]}')
        temp = exe.executioner_attentioncheck_text(df, 'ID', 'te',right_answer_te, reportonly)
        df = temp[0]
        print(f'attention check text entry removed {temp[1]}')

        with self.assertRaises(ValueError):
                    exe.executioner_preview(df, 'ID', 'status')
                    exe.executioner_completion(df, 'ID', 'finished')
                    exe.executioner_recaptcha(df, 'ID', 'recaptcha', threshold, equal_score, missing_score)
                    exe.executioner_attentioncheck_multiplechoice(df, 'ID', 'mp',right_answer_mp)
                    exe.executioner_attentioncheck_text(df, 'ID', 'te',right_answer_te, reportonly)
