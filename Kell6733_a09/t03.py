"""
-------------------------------------------------------
[Assignment 9, task 3]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")

print(file_statistics(file_handle))

file_handle.close()
