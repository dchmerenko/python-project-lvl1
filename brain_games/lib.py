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


def process_wrong_answer(wrong_answer, right_answer):
    """Print right and wrong answer.

    Args:
        wrong_answer: wrong answer
        right_answer: right_answer
    """
    print(
        "'{wrong_answer}' is wrong answer ;(.".format(
            wrong_answer=wrong_answer,
        ),
        end=' ',
    )
    print(
        "Correct answer was '{right_answer}'.".format(
            right_answer=right_answer,
        ),
    )


def gcd(a, b):
    """Calculate the Greatest Common Divisor.

    Args:
        a: integer number
        b: integer number

    Returns:
        gcd
    """
    while b:
        a, b = b, a % b
    return abs(a)


def arithmetic_progression(first, step, number=10):
    """Calculate an arithmetic progression.

    Args:
        first: first element
        step: step
        number: quantity of elements

    Returns:
        List of elements of arithmetic progression
    """
    last = first + step * number + 1
    return [str(_) for _ in range(first, last, step)]


def is_prime(number):
    """Return True if number is prime else False.

    Args:
        number: integer number

    Returns:
        Return True if number is prime else False
    """
    if number < 2:
        return False
    divisor = 2
    while divisor <= number ** 0.5:
        if number % divisor == 0:
            return False
        divisor += 1
    return True
