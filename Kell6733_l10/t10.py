"""
-------------------------------------------------------
[Lab 10, Task 10]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word


fh = open("words.txt", "r", encoding="utf-8")

word = str(input("file 'words.txt' open for reading \nWord to count: "))

print(f"'{word}' appears {count_frequency_word(fh, word)} time(s)")

fh.close()
