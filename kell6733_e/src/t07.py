"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Spencer Kelly
ID:     169066733
Email:  kell6733@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# your imports here
from t07_functions import line_lengths
# Your code here
f_in = open("source.txt", "r", encoding="utf-8")
f_short = open("short.txt", "w", encoding="utf-8")
f_long = open("long.txt", "w", encoding="utf-8")
lines = line_lengths(f_in, f_short, f_long, 16)
print(lines)

f_in.close()
f_short.close()
f_long.close()
