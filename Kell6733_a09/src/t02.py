"""
-------------------------------------------------------
[Assignment 9, task 2]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

file_handle = open("numbers.txt", "r", encoding="utf-8")

print(read_integers(file_handle))

file_handle.close()
