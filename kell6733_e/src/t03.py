"""
-------------------------------------------------------
Testing for Task 3: upper_vowels
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports
from t03_functions import upper_vowels

CASES = ('', 'ABC', 'abc', '123', 'a#b!e', 'This is the 3rd sentence.')

for case in CASES:
    altered = upper_vowels(case)
    print(f'upper_vowels("{case}") -> {altered}')
    print()
