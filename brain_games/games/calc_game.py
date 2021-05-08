"""Brain-game calc_game functional module."""

import random

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import get_user_answer, process_wrong_answer


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
        question = generate_question(tuple(operations))
        correct_answer = calculate_answer(question, operations)
        user_answer = get_user_answer(question)
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
        question like '1 + 5'
    """
    a, b = (random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))
    operator = random.choice(valid_operations)
    return '{a} {operator} {b}'.format(a=a, operator=operator, b=b)


def calculate_answer(question, operations):
    """Calculate correct answer for even-game.

    Args:
        question: question string
        operations: operation dict

    Returns:
        evaluation 'a operator b'
    """
    a, operator, b = question.split()
    a = int(a)
    b = int(b)
    return str(operations.get(operator)(a, b))
