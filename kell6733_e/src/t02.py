"""
-------------------------------------------------------
Testing for Task 2: rainfall
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""
# Imports
from t02_functions import rainfall

print("dry_days, damp_days, wet_days, avg = rainfall()")
dry_days, damp_days, wet_days, avg = rainfall()
print()
print(f"Dry days: {dry_days}")
print(f"Damp days: {damp_days}")
print(f"Wet days: {wet_days}")
print(f"Average rainfall (mm): {avg}")
