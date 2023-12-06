import os
import unittest
import pandas as pd
from src import outputer

class TestOutputer(unittest.TestCase):
    # smoke test:
    def test_outputer(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        test_df = pd.read_csv(raw_file_path)
        outputer.outputer(test_df, raw_file_path)
    
    # one shot test
    def test_outputer_result(self):
        raw_file_path = os.path.join(os.path.dirname(__file__), "data", "vt3 raw data.csv")
        test_df = pd.read_csv(raw_file_path, header=None)
        csv_file_path = os.path.join(os.path.dirname(__file__), "data", "outputer_test_file.csv")
        outputer.outputer(test_df, csv_file_path)
        print(test_df)
        stored_csv_df = pd.read_csv(csv_file_path, header=None)
        print(stored_csv_df)
        self.assertTrue(test_df.equals(stored_csv_df))

    
    # one shot test
    def test_outputer_result_2(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestOutputer)
_ = unittest.TextTestRunner().run(suite)