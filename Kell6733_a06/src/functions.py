"""
-------------------------------------------------------
Assignment 6, functions
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports


def total_wins():
    """
    -------------------------------------------------------
    takes no parameters and asks the user to enter a series 
    of strings that represent the output of a game with a 
    loop. The user should enter an empty string to signal 
    the end of the series. After all strings have been 
    entered, the function returns two numbers representing 
    how many times the string "purple" appeared in the input
    and how many times the string "gold" appeared in the input.
    Use: wins = total_wins()
    -------------------------------------------------------
    Parameters:
        None - none (none)
    Returns:
        purple_wins - how many times the string "purple" 
        appeared in the input(int)
        gold_wins - how many times the string "gold" 
        appeared in the input(int)
    ------------------------------------------------------
    """
    user = str(input("Enter the winning team: "))
    gold_wins = 0
    purple_wins = 0

    while user != "":
        if user == "gold":
            gold_wins += 1
        elif user == "purple":
            purple_wins += 1
        user = str(input("Enter the winning team: "))

    return purple_wins, gold_wins


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    div = 2
    while number > 1:
        if (number % div) == 0:
            prime = False
        else:
            prime = True
        div += 1
        return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 0
    balance = principal_amount

    print(
        f"Principal:   ${principal_amount} \nInterest interest_rate : {interest_rate}% \nMonthly payment: ${payment}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while balance > 0:
        interest = (balance * (interest_rate/100)) / 12
        if balance < payment:
            payment = balance + interest
            balance = 0
        else:
            balance = balance - payment + interest
        month += 1
        print(
            f"    {month}     {interest:.2f}    {payment:.2f}    {balance:.2f}")
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    if number < 0:
        number *= -1

    while number > 0:
        number = number // 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    divisor = 1
    total = 0
    while number > divisor:
        if (number % divisor) == 0:
            total += divisor

        divisor += 1
    return total
