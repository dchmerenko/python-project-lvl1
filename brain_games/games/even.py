"""Brain-game even_game functional module."""

from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import is_even
from brain_games.out import base_play

start_msg = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    """Play an even-odd game with the User.

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
    """Return quiz number for even-game.

    Returns:
        random integer number
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    return str(number), number


def calculate_answer(number):
    """Calculate correct answer for even-game.

    Args:
        number: number

    Returns:
        yes or no if number is even
    """
    return 'yes' if is_even(number) else 'no'
