"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Spencer Kelly
ID:     169066733
Email:  kell6733@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Constants

# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​​​​​​‌‌‌​‌‌​‌:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """
    # your code here
    DRY_DAY = 0
    DAMP_DAY = 0
    WET_DAY = 0
    daily_rainfall = int(input("Rainfall mm (-1 to quit): "))
    total_rainfall = 0
    count = 0
    while daily_rainfall != -1:
        daily_rainfall = int(input("Rainfall mm (-1 to quit): "))
        if daily_rainfall < 4:
            DRY_DAY += 1
        elif daily_rainfall >= 4 and daily_rainfall <= 8:
            DAMP_DAY += 1
        elif daily_rainfall > 8:
            WET_DAY += 1
        count += 1
        total_rainfall += daily_rainfall
    avg = total_rainfall / count
    return DRY_DAY, DAMP_DAY, WET_DAY, round(avg)
