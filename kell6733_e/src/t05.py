"""
-------------------------------------------------------
Testing for Task 5: fill_matrix
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports
from t05_functions import fill_matrix

CASES = (
    ("numbers.txt", 2, 2),
    ("numbers.txt", 5, 3),
    ("numbers.txt", 6, 8),
)

for case in CASES:
    f_in = open(case[0], "r", encoding="utf-8")
    matrix = fill_matrix(f_in, case[1], case[2])
    print(f'fill_matrix(f_in, {case[1]}, {case[2]})  -> ')
    print(matrix)
    f_in.close()
    print()
