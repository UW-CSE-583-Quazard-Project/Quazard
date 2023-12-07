import os
import unittest
import pandas as pd
from src import outputer

class TestOutputer(unittest.TestCase):
    # smoke test:
    def test_outputer(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        csv_file_path = os.path.join(os.path.dirname(__file__), "data", "outputer_test_file.csv")
        test_df = pd.read_csv(raw_file_path, header=None)
        outputer.outputer(test_df, csv_file_path)
        os.remove(csv_file_path)
    
    # one shot test
    def test_outputer_result(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        test_df = pd.read_csv(raw_file_path, header=None)
        csv_file_path = os.path.join(os.path.dirname(__file__), "data", "outputer_test_file.csv")
        outputer.outputer(test_df, csv_file_path)
        stored_csv_df = pd.read_csv(csv_file_path, header=None)
        self.assertTrue(test_df.equals(stored_csv_df))
        os.remove(csv_file_path)

    # edge test
    def test_outputer_edge(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        test_df = pd.read_csv(raw_file_path, header=None)
        with self.assertRaises(ValueError):
            outputer.outputer(test_df, "random file name")

    # edge test
    def test_outputer_edge_2(self):
        with self.assertRaises(ValueError):
            outputer.outputer(None, "random file name")

    # edge test
    def test_outputer_edge_3(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        test_df = pd.read_csv(raw_file_path, header=None)
        with self.assertRaises(ValueError):
            outputer.outputer(test_df, None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestOutputer)
_ = unittest.TextTestRunner().run(suite)
