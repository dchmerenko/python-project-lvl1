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
    Prompt User user and print welcome message. Return User user.

    Returns:
         User user
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your user? ')
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
