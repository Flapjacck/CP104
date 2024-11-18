"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports


def list_factors(number):
    """
    -------------------------------------------------------
    Determines the factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        factors - the number's factors (list of int)
    ------------------------------------------------------
    """
    divisor = 1
    factors = []
    while number > divisor:
        if (number % divisor) == 0:
            factors.append(divisor)

        divisor += 1
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    number = int(input("Enter a positive number: "))
    while number != 0:
        if number > 0:
            number_list.append(number)
        number = int(input("Enter a positive number: "))
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            index_list.append(i)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in subtrahend:
        while i in minuend:
            minuend.remove(i)
    return minuend


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index_num = -1
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            in_order = False
            index_num = i
    return in_order, index_num
