"""
-------------------------------------------------------
Lab 3, Task 8
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-13"
-------------------------------------------------------
"""
# user input
dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

# calculations
total = dirt + gravel + sand

# formatted output
print(
    "Material   Cubic Metres\n"f"Dirt       {dirt: 6.1f}\n"f"Gravel     {gravel: 6.1f}\n"f"Sand       {sand: 6.1f}\n"f"Total      {total: 6.1f}")
