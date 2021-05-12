"""Brain-game prime_game functional module."""

import random

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import is_prime
from brain_games.out import base_play

start_msg = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play():
    """Play an 'Is it prime number?' game with the User.

    Returns:
        base play game function
    """
    return base_play(
        start_msg=start_msg,
        tries_limit=TRIES_LIMIT,
        generate_question=generate_question,
        calculate_answer=calculate_answer,
    )


def generate_question():
    """Return numbers for prime-game.

    Returns:
        random integer number
    """
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    return str(number), number


def calculate_answer(number):
    """Calculate correct answer for prime-game.

    Args:
        number: integer number

    Returns:
        'yes' if the number is prime else 'no'
    """
    return 'yes' if is_prime(number) else 'no'
