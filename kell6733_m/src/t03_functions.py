"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Spencer Kelly
ID:     169066733
Email:  kell6733@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants

# your constants here
BASE_COST = 125
DISCOUNT = 0.9
EXTRA_FEE = 25


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​​​​​​‌‌‌​‌‌​‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    extra_services = int(input("How many extra services are you purchasing? "))

    if extra_services > 1:
        vip = input("Are you a VIP member (Y/N)? ")
        if vip == "Y":
            cost = (BASE_COST + (extra_services * EXTRA_FEE)) * DISCOUNT
        elif vip == "N":
            cost = BASE_COST + (extra_services * EXTRA_FEE)
        else:
            print("Error")
    elif extra_services == 1:
        cost = BASE_COST + EXTRA_FEE
    else:
        cost = "error"

    return cost
