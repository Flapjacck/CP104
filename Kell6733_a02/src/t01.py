"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Constants
ANNUAL_TAX = 18.5

# user input
total_sales = int(input("Enter the total sales: $"))

# calculations
taxes = total_sales * (ANNUAL_TAX / 100)

# output
print(
    f"Projected Tax Report \n-------------------------- \nTotal sales:   ${total_sales} \nAnnual tax:    %{ANNUAL_TAX} \n-------------------------- \nTax:           ${taxes}")
