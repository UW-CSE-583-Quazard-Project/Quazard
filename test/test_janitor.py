""" 
This module contains necessary tests for the Janitor component
"""
import os
import unittest
import pandas as pd
from src import janitor as fc
class TestJanitor(unittest.TestCase):
    """
    Test class for Frankenstein component
    """
    def test_smoke(self):
        """
        Simple test to check if the function could run normally
        """
        dataframe = pd.read_csv(os.getcwd() + "/test/cleaned_data.csv")
        cols = ["Q_RecaptchaScore"]
        fc.drop_cols(dataframe, cols)
    def test_one_shot_drop_one_col(self):
        """
        One-shot test to check if the function could drop the given single column
        """
        dataframe = pd.read_csv(os.getcwd() + "/test/cleaned_data.csv")
        cols = ["Q_RecaptchaScore"]
        dataframe = fc.drop_cols(dataframe, cols)
        for _ in cols:
            self.assertNotIn(_, dataframe.columns, "The columns have not been successfully dropped")
    def test_one_shot_drop_two_cols(self):
        """
        One-shot test to check if the function could drop the given multiple columns
        """
        dataframe = pd.read_csv(os.getcwd() + "/test/cleaned_data.csv")
        cols = ["Q_RecaptchaScore", "Duration (in seconds)"]
        dataframe = fc.drop_cols(dataframe, cols)
        for _ in cols:
            self.assertNotIn(_, dataframe.columns, "The columns have not been successfully dropped")
    def test_edge_on_not_existing_cols(self):
        """
        Edge test to check if the function could drop a column that does not exist in the dataframe
        """
        dataframe = pd.read_csv(os.getcwd() + "/test/cleaned_data.csv")
        cols = ["Q_RecaptchaScore", "Duration (in seconds)"]
        dataframe = fc.drop_cols(dataframe, cols)
        with self.assertRaises(ValueError):
            fc.drop_cols(dataframe, cols)
    def test_edge_on_invalid_dataframe(self):
        """
        Edge test to check if the function could drop a column that does not exist in the dataframe
        """
        dataframe = None
        cols = ["Q_RecaptchaScore"]
        with self.assertRaises(ValueError):
            fc.drop_cols(dataframe, cols)
