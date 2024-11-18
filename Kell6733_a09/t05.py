"""
-------------------------------------------------------
[Assignment 9, task 5]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports
from functions import student_stats

file_handle = open("students.txt", "r", encoding="utf-8")

print(student_stats(file_handle))

file_handle.close()
