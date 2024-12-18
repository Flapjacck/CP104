"""
-------------------------------------------------------
Lab 2, Task 7
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# user input
num_flyers = int(input("Number of flyers: "))
num_volunteers = int(input("Number of volunteers: "))

# calculations
flyers_per_volunteer = num_flyers // num_volunteers
left_over_flyers = num_flyers % num_volunteers

# output
print("Flyers per volunteer:", flyers_per_volunteer)
print("Flyers left over:", left_over_flyers)
