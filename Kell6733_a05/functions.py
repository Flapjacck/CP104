"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
from itertools import product


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    prints a table of the number of calories burned every 
    five minutes given the number of calories burned per 
    minute an the total number of minutes run.
    Use: cals_burned = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - Cals burned per min(float)
        minutes - Total minutes ran(int)
    Returns:
        None
    ------------------------------------------------------
    """
    total_cal_burned = 0
    for i in range(5, minutes + 1, 5):
        total_cal_burned += 5 * per_min
        print(f" {i:2}  {total_cal_burned:.1f}")
    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    takes an integer parameter and prints a arrow of # 
    characters pointing up
    Use: arrow = arrow_up(rows)
    -------------------------------------------------------
    Parameters:
       rows - number of rows in arrow(int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            print(spaces + "#")
        else:
            print(spaces + "#" + " " * (2 * i - 3) + "#")
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start_num, stop_num + 1):
        if i == start_num:
            print("\t", end="")
            for k in range(start_num, stop_num + 1):
                print(k, end="\t")
            print("\n\t" + "-" * 25)
        for k in range(start_num, stop_num + 1):
            if k == start_num:
                print(i, "|", end="\t")
            result = i * k
            print(result, end="\t")
        print()
    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total += start
        start += increment
    return total
