"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# constants
FAHRENHEIT_FREEZE = 32
F_C_RATIO = 9 / 5

# User input
celsius = int(input("Temperature (C): "))

# formula for celsius to fahrenheit
fahrenheit = F_C_RATIO * celsius + FAHRENHEIT_FREEZE

# Output
print("Temperature (F):", fahrenheit)
