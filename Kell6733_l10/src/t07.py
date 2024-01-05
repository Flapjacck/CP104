"""
-------------------------------------------------------
[Lab 10, Task 7]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num


fh = open("numbers.txt", "r+", encoding="utf-8")

print(
    f"file 'numbers.txt' open for reading and writing \n{append_max_num(fh)} is appended")
fh.close()
