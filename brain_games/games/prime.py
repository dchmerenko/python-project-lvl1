"""Brain-game prime_game functional module."""

import random

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.core import base_play

start_msg = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play():
    """Play an 'Is it prime number?' game with the User.

    Returns:
        base play game function
    """
    return base_play(
        start_msg=start_msg,
        tries_limit=TRIES_LIMIT,
        get_question_answer=get_question_answer,
    )


def get_question_answer():
    """Return question and answer for prime-game.

    Returns:
        question: random integer number
        answer: 'yes' if the number is prime else 'no'
    """
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer


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
