"""
-------------------------------------------------------
[Assignment 9, task 4]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering

fh_read = open("wilde.txt", "r", encoding="utf-8")
fh_write = open("wilde_numbered.txt", "w", encoding="utf-8")

line_numbering(fh_read, fh_write)

fh_read.close()
fh_write.close()
