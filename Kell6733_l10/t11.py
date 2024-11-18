"""
-------------------------------------------------------
[Lab 10, Task 11]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

fh = open("words.txt", "r", encoding="utf-8")

print(
    f"file 'words.txt' open for reading\n'{find_longest(fh)}' is the last longest word")

fh.close()
