"""Brain-game progression_game functional module."""

import random

from brain_games.config import HIDDEN_MARK, MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import arithmetic_progression
from brain_games.out import base_play

start_msg = 'Find the missed element of Arithmetic progression.'


def play():
    """
    Play a guess missed element of Arithmetic progression game with the User.

    Returns:
        base play game function
    """
    return base_play(
        start_msg=start_msg,
        tries_limit=TRIES_LIMIT,
        generate_question=generate_question,
        calculate_answer=calculate_answer,
    )


def generate_question():  # noqa: WPS210 Found too many local variables
    """Return progression and hidden value for progression-game.

    Returns:
        progression: random arithmetic progression with one hidden value
        hidden_value: hidden value of arithmetic progression
    """
    first, step = (random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))
    progression = arithmetic_progression(first, step)
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = HIDDEN_MARK
    return ' '.join(progression), hidden_value


def calculate_answer(hidden_value):
    """Calculate correct answer for progression-game.

    Args:
        hidden_value: hidden value of arithmetic progression

    Returns:
        hidden_value: hidden value of arithmetic progression
    """
    return hidden_value
