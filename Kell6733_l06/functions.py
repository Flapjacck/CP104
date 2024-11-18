"""
-------------------------------------------------------
functions lab 6
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# Constants


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, finish + 1, increment):
        total += i
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(0, height + 1):
        print(f"{' ' * (height - i)}{char * (2 * i - 1)}")
    return


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(0, width + 1):
        print(f"{char * i}")

    for i in range(width - 1, 0, -1):
        print(f"{char * i}")
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    rate_percent = (rate / 100)
    final_value = 0
    for i in range(0, years + 1):
        if i == 0:
            value
        else:
            value += (rate_percent) * value
        formatted_value = f"{value:,.2f}"
        print(f"{i:>2}{formatted_value:>18}")
        final_value = value
    return final_value


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    WEEK_LENGHT = 6
    total_hours = 0
    for i in range(1, WEEK_LENGHT + 1):
        print(f"Week {i}")
        for d in range(1, ia_count + 1):
            hours_worked = float(input(f"  Marking hours for IA {d}: "))
            total_hours += hours_worked
    return total_hours
