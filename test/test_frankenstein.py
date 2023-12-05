"""
This module contains necessary tests for the Frankenstein component
"""
import os
import numpy as np
import pandas as pd
import unittest
from src import frankenstein as fc
class TestFranken(unittest.TestCase):
    """
    Test class for Frankenstein component
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure function runs.
        """
        df = pd.DataFrame({'A': [1, 1, 2, 2],
                   'B': [1, 2, 3, 4],
                    'C': np.random.randn(4)})
        group_keys = ["A", "B"]
        applied_keys = ["C"]
        modes = ["mean", "mean"]
        fc.aggregate(dataframe=df, group_keys=group_keys, applied_keys=applied_keys, modes=modes)
    def test_one_shot_groupby_id_prob(self):
        """
        One-shot test to check if the funciton could correctly groupby then aggregate
        """
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vx3 data long format.csv")
        test_df = pd.read_csv(raw_file_path)
        group_keys = ["Response ID", "prob"]
        applied_keys = ["likelihood", "severity", "outcometrust"]
        modes = ["mean", "mean", "mean"]
        pairs = {"likelihood":"mean", "severity":"mean", "outcometrust":"mean"}
        result = fc.aggregate(dataframe=test_df, group_keys=group_keys, applied_keys=applied_keys, modes=modes)
        compared_df = test_df.groupby(group_keys).agg(pairs).reset_index()
        assert result.equals(compared_df)
    def test_edge(self):
        """
        Edge test to check if the funciton could handle unwanted data type
        """
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vx3 data long format.csv")
        test_df = pd.read_csv(raw_file_path)
        group_keys = ["Response ID", "prob"]
        applied_keys = ["likelihood", "severity", "decision"]
        modes = ["mean", "mean", "sum"]
        with self.assertRaises(ValueError):
            fc.aggregate(dataframe=test_df, group_keys=group_keys, applied_keys=applied_keys, modes=modes)