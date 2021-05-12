"""Brain-game progression_game functional module."""

import random

from brain_games.config import HIDDEN_MARK, MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import get_arithmetic_progression
from brain_games.out import base_play

start_msg = 'Find the missed element of Arithmetic progression.'


def play():
    """
    Play a guess missed element of the Arithmetic progression game with the User.

    Returns:
        base play game function
    """
    return base_play(
        start_msg=start_msg,
        tries_limit=TRIES_LIMIT,
        get_question_answer=get_question_answer,
    )


def get_question_answer():
    """Return question and answer for progression-game.

    Returns:
        question: random arithmetic progression with one hidden value
        answer: hidden value
    """
    first_term = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = get_arithmetic_progression(first_term, step)
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = HIDDEN_MARK
    return ' '.join(progression), hidden_value
