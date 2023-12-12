"""
Longwide Converter component testing
"""
import os
import numpy as np
import pandas as pd
import unittest
import random as rand

#our components
from src import longwideconverter as convert

class TestExecutioner(unittest.TestCase):
    """
    Test class for executioner component
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure the functions run.
        """
        df = pd.DataFrame({
                            'ID': ["A", "B", "C", "D"],
                            'age': [np.random.randint(18, 50) for _ in range(4)],
                            'rating1': [np.random.randint(1, 100) for _ in range(4)],
                            'mp1': [np.random.choice(["Apple", "Cat", "Car"]) for _ in range(4)],
                            'rating2': [np.random.randint(1, 100) for _ in range(4)],
                            'mp2': [np.random.choice(["Apple", "Cat", "Car"]) for _ in range(4)],
                            'rating3': [np.random.randint(1, 100) for _ in range(4)],
                            'mp3': [np.random.choice(["Apple", "Cat", "Car"]) for _ in range(4)]
                        })
        df_origin = df
        # Get all necessary arguments
        trial_num = 3
        trial_length = 2
        
        # Run function
        df = convert.long_dataframe_maker(df, "ID", trial_num, trial_length, "rating1")

        print("test successful")
        print("Input")
        print(df_origin)
        print("Ouput")
        print(df)

    def test_one_shot(self):
        """
        One-shot test to check with a set of arguments
        """
        df = pd.DataFrame({
                            'ID': ["A", "B"],
                            'rating1': [1,2],
                            'mp1': ["Apple", "Cat"],
                            'rating2': [11,12],
                            'mp2': ["Banana", "Dog"],
                            'age': [25,35],
                        })
        df_expected = pd.DataFrame({
                            'ID': ["A","A", "B", "B"],
                            'trial': [1,2,1,2],
                            'Question 1': [1, 11, 2, 12],
                            'Question 2': ["Apple","Banana","Cat","Dog"],
                            'age': [25,25,35,35],
                        })
        # Get all necessary arguments
        trial_num = 2
        trial_length = 2
        
        # Run function
        df = convert.long_dataframe_maker(df, "ID", trial_num, trial_length, "rating1")

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
        In this case, the starting column argument is not in the dataframe
        """
        df = pd.DataFrame({
                            'ID': ["A", "B"],
                            'rating1': [1,2],
                            'mp1': ["Apple", "Cat"],
                            'rating2': [11,12],
                            'mp2': ["Banana", "Dog"],
                            'age': [25,35],
                        })
        # Get all necessary arguments
        trial_num = 2
        trial_length = 2
        
        # Run function
        df = convert.long_dataframe_maker(df, "ID", trial_num, trial_length, "rating3")

        with self.assertRaises(ValueError):
                    print(df)
