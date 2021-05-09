"""Brain-game calc_game functional module."""

import random

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT, operations
from brain_games.out import base_play

start_msg = 'What is the result of the expression?'


def play():
    """Play a calculation game with the User.

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
    """Return quiz numbers for calc-game.

    Returns:
        question: '10 + 5'
        args: (10, 5, '+')
    """
    a, b = (random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))
    operator = random.choice(tuple(operations))
    question = '{a} {operator} {b}'.format(a=a, operator=operator, b=b)
    args = a, b, operator
    return question, args


def calculate_answer(args):
    """Calculate correct answer for even-game.

    Args:
        args: (a, b, operator)

    Returns:
        evaluation 'a operator b'
    """
    a, b, operator = args
    return str(operations.get(operator)(a, b))
