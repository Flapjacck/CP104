"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Inputs
f_length = float(input("Foundation length (m): "))
f_width = float(input("Foundation width (m): "))
f_height = float(input("Foundation height (m): "))
w_height = float(input("Wall height (m): "))
conc_cost = float(input("Cost of concrete ($/m^3): $"))
brick_cost = float(input("Cost of bricks ($/m^2): $"))

# calculations
# foundation
conc_for_f = f_height * f_length * f_width
total_conc_cost = conc_for_f * conc_cost
# brick
total_brick = ((w_height * f_length) * 2) + ((w_height * f_width) * 2)
total_brick_cost = total_brick * brick_cost

total_cost = total_brick_cost + total_conc_cost

# formatted output
print(
    f"\nConcrete needed for foundation (m^3): {conc_for_f} \nCost of concrete: ${total_conc_cost} \nBricks needed for walls (m^2): {total_brick} \nCost of bricks: {total_brick_cost} \nTotal cost: ${total_cost}")
