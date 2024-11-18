"""
-------------------------------------------------------
[Lab 10, Task 4]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import customer_first

fh = open("customers.txt", "r", encoding="utf-8")

print("Find customer with earliest sign-in: \n",
      customer_first(fh))
