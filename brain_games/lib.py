"""Brain-games support function library module."""

import prompt


def is_even(number):
    """
    Check if number is even.

    Args:
        number: this is a first param

    Returns:
        True if number is even, else False
    """
    return number % 2 == 0


def welcome_user():
    """
    Prompt User name and print welcome message. Return User name.

    Returns:
         User name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name
