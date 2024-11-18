"""
-------------------------------------------------------
lab 2, Task 6
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# user Inputs
principal = float(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
interest_rate = float(input("Yearly interest rate (%): "))

# calculations/conversions
monthly_interest_rate = interest_rate / 12 / 100
total_payments = years * 12
monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)
                               ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

# output
print("The monthly payments are: $", monthly_payment)
