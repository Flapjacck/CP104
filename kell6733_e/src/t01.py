"""
-------------------------------------------------------
Testing for Task 1: even_avg
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from t01_functions import even_avg

CASES = (
    [],
    [99],
    [1, 2, 4],
    [-5, 6, 0, 8],
)

for case in CASES:
    print(f'even_avg({case}) -> {even_avg(case)}')
    print()
