"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Spencer Kelly
ID:     169066733
Email:  kell6733@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​​​​‌‌‌​‌‌​‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """

    # your code here
    ea = 0
    count = 0
    for i in values:
        if i % 2 == 0:
            ea += i
            count += 1
    if count == 0:
        ea = 0
    else:
        ea = ea / count

    return round(ea)
