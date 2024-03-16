import numpy as np
import pandas as pd
import unittest
import os
from activation_fit import extract_seconds, linear_func, r_squared, activation_mechanism, main

def test_extract_seconds():
    assert extract_seconds("5 min 30 s") == 330
    assert extract_seconds("3 min") == 180
    assert extract_seconds("1 min 40 s") == 100
    assert extract_seconds("Invalid format") == 0

def test_linear_func():
    assert linear_func(2, 3, 4) == 10
    assert linear_func(0, 2, 1) == 1

def test_r_squared():
    y_true = np.array([3, -0.5, 2, 7])
    y_pred = np.array([2.5, 0.0, 2, 8])
    assert round(r_squared(y_true, y_pred), 2) == 0.95

def test_activation_mechanism():
    assert activation_mechanism(2, 3, 4) == 1.1956442831215972

class TestExcelFile(unittest.TestCase):
    def test_excel_file_exists(self):
        # Define the path to the Excel file
        excel_file_path = "example.xlsx"

        # Check if the Excel file exists
        file_exists = os.path.exists(excel_file_path)

        # Assert that the file exists
        self.assertTrue(file_exists, f"Excel file '{excel_file_path}' does not exist.")

if __name__ == "__main__":
    unittest.main()