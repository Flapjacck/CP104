"""
-------------------------------------------------------
Testing for Task 6: multiply_list
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""
# Imports
from copy import copy

from t06_functions import multiply_list

CASES = (
    [],
    [99],
    [1, 2, 3, 4, 5],
)

for case in CASES:
    # Make copy of testing list for printing purposes.
    values = copy(case)
    print(f"before function: {values}")
    multiply_list(values)
    print(f"multiply_list({case})")
    print(f"after function: {values}")
    print()
