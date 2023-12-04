import os
import unittest
import pandas as pd
from src import decapitator

class TestDecapitator(unittest.TestCase):
    # smoke test:
    def test_decapitator(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        df = pd.read_csv(raw_file_path)
        decapitator.decapitator(file=df)
    
    def test_decapitator_result(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        raw_df = pd.read_csv(raw_file_path)
        modified_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3_decapitator_one_shot_test.csv")
        modified_df = pd.read_csv(modified_file_path)
        decapitator.decapitator(file=raw_df)
        self.assertIsInstance(modified_df, pd.DataFrame)
        self.assertFalse(raw_df.shape == modified_df.shape)
        self.assertFalse(raw_df.columns.equals(modified_df.columns))
        comparison_result = raw_df.equals(modified_df)
        self.assertTrue(comparison_result)
        
    def test_decapitator_result_2(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        raw_df = pd.read_csv(raw_file_path)
        modified_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3_decapitator_one_shot_test_2.csv")
        modified_df = pd.read_csv(modified_file_path)
        decapitator.decapitator(file=raw_df, rows=[1, 3])
        self.assertIsInstance(modified_df, pd.DataFrame)
        self.assertFalse(raw_df.shape == modified_df.shape)
        self.assertFalse(raw_df.columns.equals(modified_df.columns))
        comparison_result = raw_df.equals(modified_df)
        self.assertTrue(comparison_result)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDecapitator)
_ = unittest.TextTestRunner().run(suite)
