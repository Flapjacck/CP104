"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# user input
pos_num = int(input("Enter a positive digit number: "))

# calculations
d1 = pos_num // 10
d2 = pos_num % 10
difference = d1 - d2

# output
print(f"\nThe difference of the digits of {pos_num} is {difference}")
