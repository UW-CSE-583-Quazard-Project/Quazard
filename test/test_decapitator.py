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
    
    # one shot test
    def test_decapitator_result(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        raw_df = pd.read_csv(raw_file_path, header=None)
        modified_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3_decapitator_one_shot_test.csv")
        modified_df = pd.read_csv(modified_file_path, header=None)
        raw_df = decapitator.decapitator(file=raw_df)
        self.assertIsInstance(modified_df, pd.DataFrame)
        self.assertTrue(raw_df.shape == modified_df.shape)
        comparison_result = raw_df.equals(modified_df)
        self.assertTrue(comparison_result)
    
    # one shot test
    def test_decapitator_result_2(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        raw_df = pd.read_csv(raw_file_path, header=None)
        modified_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3_decapitator_one_shot_test_2.csv")
        modified_df = pd.read_csv(modified_file_path, header=None)
        raw_df = decapitator.decapitator(file=raw_df, rows=[1, 3])
        self.assertIsInstance(modified_df, pd.DataFrame)
        self.assertTrue(raw_df.shape == modified_df.shape)
        comparison_result = raw_df.equals(modified_df)
        self.assertTrue(comparison_result)
    
    # edge test
    def test_decapitator_edge(self):
        with self.assertRaises(ValueError):
            decapitator.decapitator(None)
    
    # edge test
    def test_decapitator_edge_2(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        raw_df = pd.read_csv(raw_file_path, header=None)
        with self.assertRaises(ValueError):
            decapitator.decapitator(raw_df, 1)

    # edge test
    def test_decapitator_edge_3(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        raw_df = pd.read_csv(raw_file_path, header=None)
        with self.assertRaises(ValueError):
            decapitator.decapitator(raw_df, [1, 2, 3])

suite = unittest.TestLoader().loadTestsFromTestCase(TestDecapitator)
_ = unittest.TextTestRunner().run(suite)
