"""
-------------------------------------------------------
Lab 2, Task 10
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# Inputs
subtotal = float(input("Food Charge: $"))
sales_tax = float(input("Sales Tax in (%): "))
tip_percent = float(input("Tip in (%): "))

# Calculations
tax = (sales_tax / 100) * subtotal
tip = (tip_percent / 100) * subtotal
total = subtotal + tax + tip

# output
print("Cost of meal:")
print("Subtotal: $", subtotal)
print("     Tax: $", tax)
print("     Tip: $", tip)
print("------------------")
print("Total: $", total)
