"""
This module contains tests for the Reader component.
"""

import os
import unittest
import time
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

    def test_file_exists(self):
        """
        Test to ensure the file specified exists.
        """

        path = "imaginary_file.txt"

        with self.assertRaises(FileNotFoundError):
            reader.reader(path)

    def test_file_type(self):
        """
        Test to ensure file type is csv.
        """

        path = os.path.join(os.path.dirname(__file__), "data",
                            "readme.txt")

        with self.assertRaises(ValueError):
            reader.reader(path)

    def test_large_file_performance(self):
        """
        Test to ensure file is not too long and processing won't take
        too long.
        """

        # Create a temporary large CSV file for testing
        large_csv_file_path = "large_file.csv"

        # Generate a large CSV file (for demonstration purposes)
        # Adjust the number of rows and columns as needed
        num_rows = 100000
        num_columns = 10
        data = pd.DataFrame({'col{}'.format(i): range(num_rows) for i in range(num_columns)})
        data.to_csv(large_csv_file_path, index=False)

        # Measure the time it takes to process the large file
        start_time = time.time()
        result_df = reader.reader(large_csv_file_path)
        end_time = time.time()

        # Assert that the result is a DataFrame and the processing time is reasonable
        self.assertIsInstance(result_df, pd.DataFrame)
        processing_time = end_time - start_time
        print(f"Processing time: {processing_time:.2f} seconds")

        # Optionally, set a threshold for processing time based on your performance requirements
        threshold_time = 10.0  # Set your threshold time in seconds
        self.assertLess(processing_time, threshold_time)

        # Clean up: Remove the temporary file
        os.remove(large_csv_file_path)
