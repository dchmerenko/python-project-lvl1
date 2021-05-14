"""Brain-game even_game functional module."""

from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.core import base_play

start_msg = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    """Play an even-odd game with the User.

    Returns:
        base play game function
    """
    return base_play(
        start_msg=start_msg,
        tries_limit=TRIES_LIMIT,
        get_question_answer=get_question_answer,
    )


def get_question_answer():
    """Return question and answer for even-game.

    Returns:
        question: random integer number
        answer: 'yes' or 'no' if number is even
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(number) else 'no'
    return str(number), answer


def is_even(number):
    """
    Check if number is even.

    Args:
        number: this is a first param

    Returns:
        True if number is even, else False
    """
    return number % 2 == 0
