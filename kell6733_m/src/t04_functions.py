"""
-------------------------------------------------------
Midterm B Task 4 Function Definitions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""


def get_it(response):
    """
    DO NOT CHANGE THE CONTENTS OF THIS FUNCTION
    -------------------------------------------------------
    Determines how a response should be classified.
    Use: classification = get_it(response)
    -------------------------------------------------------
    Parameters:
        response - a response to classify (str)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​​​​‌‌‌​‌‌​‌:
        classification - the response classification (str)
    -------------------------------------------------------
    """
    if response == 'Y':
        classification = 'Yes'
    elif response == 'N':
        classification = 'No'
    else:
        classification = 'Unknown'
    return classification
