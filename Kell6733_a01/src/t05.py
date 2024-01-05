"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# user Inputs
principal = float(input("Principal: $"))
interest_rate = float(input("Interest (%): "))
years = int(input("Number of years: "))
num_of_compounds = int(input("Number of times interest compounded per year: "))

# calculations/conversions
interest_rate /= 100
balance = principal * (1 + interest_rate /
                       num_of_compounds) ** (num_of_compounds * years)

# output
print(f"Balance: ${balance}")
