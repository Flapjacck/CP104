"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Constants
date = int(input("Enter a date in the format YYYYMMDD: "))

# calculations
year = date // 10000
month = (date // 100) % 100
day = date % 100

# formatted output
print(f"\nThe reformatted date: {year}/{month}/{day}")
