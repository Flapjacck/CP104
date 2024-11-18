"""
-------------------------------------------------------
Lab 3, Task 12
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""
# given assignment statements
first = 100
second = 34
third = 933

# calculations
total = first + second + third

# formating from int to str
first, second, third, total = str(first), str(second), str(third), str(total)

# formatted output
print(f"Values")
print(f"First: {first:_>6s}")
print(f"Second: {second:_>6s}")
print(f"Third: {third:_>6s}")
print(f"Total: {total:_>6s}")
