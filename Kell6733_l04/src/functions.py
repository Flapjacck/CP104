"""
-------------------------------------------------------
functions
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-09-19"
-------------------------------------------------------
"""
import math


def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    # constants
    PI = 3.14159265359
    # calculations
    circ = 2 * PI * radius
    # return
    return float(circ)


def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, circumference, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, circ, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        circ - circumference of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    # calc
    hyp = math.sqrt((adjacent ** 2) + (opposite ** 2))
    circ = adjacent + opposite + hyp
    area = (1/2) * opposite * adjacent

    return hyp, circ, area


def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    # calc/conversions
    pre_commission_cost = computer_cost * computers_bought
    commission = (commission_percent / 100)
    total_cost = pre_commission_cost * (1 + commission)

    # output
    return pre_commission_cost, total_cost
    # return f"{pre_commission_cost:.2f}", f"{total_cost:.2f}"


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    # constant
    FAHRENHEIT_FREEZE = 32
    F_C_RATIO = 9 / 5
    # calc
    fahrenheit = F_C_RATIO * celsius + FAHRENHEIT_FREEZE
    # return
    return fahrenheit


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    # constants
    MIN_TO_SEC = 60
    HOUR_TO_SEC = 60 * 60
    # calc
    days = initial_seconds // (24 * HOUR_TO_SEC)
    remaining_seconds = initial_seconds % (24 * HOUR_TO_SEC)
    hours = remaining_seconds // HOUR_TO_SEC
    remaining_seconds %= HOUR_TO_SEC
    minutes = remaining_seconds // MIN_TO_SEC
    seconds = remaining_seconds % MIN_TO_SEC

    return days, hours, minutes, seconds
