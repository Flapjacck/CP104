"""
-------------------------------------------------------
[Lab 10, Task 13]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import file_copy

fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open('new_words.txt', 'w', encoding="utf-8")

print("Copying 'words.txt' to 'new_words.txt'")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()
