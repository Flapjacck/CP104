"""
-------------------------------------------------------
[Assignment 9, task 1]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import file_top

file_handle = open("numbers.txt", "r", encoding="utf-8")

file_top(file_handle, 5)

file_handle.close()
