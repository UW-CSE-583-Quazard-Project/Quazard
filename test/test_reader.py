"""
This module contains tests for the Reader component.
"""

import os
import unittest
import pandas as pd
from src import reader

class TestReader(unittest.TestCase):
    """
    This is a class of tests to evaluate the Reader module
    """

    def test_smoke(self):
        """
        Test to check if function runs normally.
        """

        path = os.path.join(os.path.dirname(__file__), "data",
                            "vt3 raw data.csv")
        reader.reader(path)

    def test_oneshot(self):
        """
        One shot test to make sure two dataframes are equal.
        """

        path = os.path.join(os.path.dirname(__file__), "data",
                            "vt3 raw data.csv")

        df1 = pd.read_csv(os.path.join(os.path.dirname(__file__),
                                       "data", "vt3 raw data.csv"), 
                                       header=None)
        df2 = reader.reader(path)

        result = df1.equals(df2)
        self.assertTrue(result)
