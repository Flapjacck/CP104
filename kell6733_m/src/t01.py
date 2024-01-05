"""
-------------------------------------------------------
Midterm B Task 1 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-12-08"
-------------------------------------------------------
"""
# Imports
from t01_functions import minimal_change, count_by_five

cents = int(input("Cents: "))
loonies, quarters, dimes, nickels = minimal_change(cents)
print(
    f"minimal_change({cents}) -> ({loonies}, {quarters}, {dimes}, {nickels})")
