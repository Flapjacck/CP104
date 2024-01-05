"""
-------------------------------------------------------
Testing for Task 4: draw_x
-------------------------------------------------------
Author:  David Brown
ID:      123456789    
Email:   dbrown@wlu.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from t04_functions import draw_x

CASES = list(range(3, 10))

for case in CASES:
    print(f'draw_x({case}) ->')
    draw_x(case)
    print()
