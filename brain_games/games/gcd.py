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
        get_question_answer=get_question_answer,
    )


def get_question_answer():
    """Return question and answer for gcd-game.

    Returns:
        question: two random integer numbers
        answer: the greatest common divisor
    """
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{a} {b}'.format(a=a, b=b)
    answer = str(gcd(a, b))
    return question, answer
