"""Brain-game calc_game functional module."""

import random

import prompt
from brain_games.config import MAX_NUMBER, TRIES_LIMIT
from brain_games.lib import process_wrong_answer


def play(user):
    """
    Play a calculation game with the User.

    Args:
        user: User name
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }
    print('What is the result of the expression?')

    for _ in range(TRIES_LIMIT):
        a, b, operator = generate_question(tuple(operations))
        correct_answer = calculate_answer(a, b, operator, operations)
        user_answer = get_user_answer(a, b, operator)
        if user_answer == correct_answer:
            print('Correct!')
            continue
        process_wrong_answer(user_answer, correct_answer)
        print("Let's try again, {user}!".format(user=user))
        break
    else:  # for - else. Run if no break occurs in cycle for.
        print('Congratulations, {user}!'.format(user=user))


def generate_question(valid_operations):
    """Return quiz numbers for calc-game.

    Args:
        valid_operations: tuple of valid operation signs, i.e '+', '-', '*'

    Returns:
        a: random integer number
        b: random integer number
        operator: operator sign
    """
    a, b = (random.randint(0, MAX_NUMBER) for _ in range(2))
    operator = random.choice(valid_operations)
    return a, b, operator


def calculate_answer(a, b, operator, operations):
    """Calculate correct answer for even-game.

    Args:
        a: number
        b: number
        operator: operator sign
        operations: operation dict

    Returns:
        evaluation 'a operator b'
    """
    return str(operations.get(operator)(a, b))


def get_user_answer(a, b, operator):
    """Print question and return user answer.

    Args:
        a: number
        b: number
        operator: operator sign

    Returns:
        user answer
    """
    print('Question: {a} {operator} {b}'.format(a=a, b=b, operator=operator))
    return prompt.string('Your answer: ', empty=True)
