"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 0
    guess = 0
    number = randint(1, high)

    while guess != number:
        guess = int(input("Guess: "))
        count += 1
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")
            print(f"You made {count} guesses.")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    BASE_NUMBER = 2
    power = 1
    while power < target:
        power *= BASE_NUMBER

    return power


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    number = float(input("First positive value: "))
    total = 0
    average = 0
    min = number
    max = number

    while number >= 0:
        average += 1
        total += number
        if number > max:
            max = number
        if number < min:
            min = number
        number = float(input("Next positive value: "))
    average = total / average
    return min, max, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    monthly_expenses = float(input("Enter an expense (0 to quit): $"))
    expenses = 0

    while monthly_expenses != 0:
        expenses += monthly_expenses
        monthly_expenses = float(input("Enter another expense (0 to quit): $"))

    balance = available - expenses
    if balance < 0:
        status = "Deficit"
    elif balance > 0:
        status = "Surplus"
    else:
        status = "Balanced"

    return expenses, balance, status


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    OVERTIME_RATE = 1.5
    TAX_RATE = 0.03625
    OVERTIME = 40
    total = 0
    average_num = 0
    id = int(input("Employee ID: "))

    while id != 0:
        hr_rate = float(input("Hourly wage rate: "))
        hr_worked = float(input("Hours worked: "))
        if hr_worked > 40:
            gross = (hr_rate * OVERTIME) + (hr_rate *
                                            OVERTIME_RATE * (hr_worked - OVERTIME))
        else:
            gross = (hr_worked * hr_rate)
        paid = gross * (1 - TAX_RATE)
        print(f"Net payment for employee {id}: ${paid:.2f}\n")
        total += paid
        average_num += 1
        id = int(input("Employee ID: "))
    average = total / average_num
    return total, average
