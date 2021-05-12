"""Brain-game calc_game functional module."""

import random

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.out import base_play

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}

start_msg = 'What is the result of the expression?'


def play():
    """Play a calculation game with the User.

    Returns:
        base play game function
    """
    return base_play(
        start_msg=start_msg,
        tries_limit=TRIES_LIMIT,
        get_question_answer=get_question_answer,
    )


def get_question_answer():
    """Return question and answer for calc-game.

    Returns:
        question: '10 + 5'
        answer: '15'
    """
    a, b = (random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))
    operator = random.choice(tuple(operations))
    question = '{a} {operator} {b}'.format(a=a, operator=operator, b=b)
    answer = str(operations.get(operator)(a, b))
    return question, answer
