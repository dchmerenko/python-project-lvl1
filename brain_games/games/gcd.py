"""Brain-game gcd_game functional module."""

import random

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import gcd
from brain_games.out import base_play

start_msg = 'Find the greatest common divisor of given numbers.'


def play():
    """Play a guess Greatest Common Divisor game with the User.

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
    """Return two numbers for gcd-game.

    Returns:
        string of two random integer number
    """
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{a} {b}'.format(a=a, b=b)
    args = (a, b)
    return question, args


def calculate_answer(args):
    """Calculate correct answer for gcd-game.

    Args:
        args: (a, b)

    Returns:
        the greatest common divisor
    """
    a, b = args
    return str(gcd(a, b))
