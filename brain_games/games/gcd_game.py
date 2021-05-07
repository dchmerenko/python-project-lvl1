"""Brain-game gcd_game functional module."""

import random

import prompt
from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import gcd, process_wrong_answer


def play(user):
    """
    Play a guess Greatest Common Divisor game with the User.

    Args:
        user: User name
    """
    print('Find the greatest common divisor of given numbers.')

    for _ in range(TRIES_LIMIT):
        a, b = generate_question()
        correct_answer = calculate_answer(a, b)
        user_answer = get_user_answer(a, b)
        if user_answer == correct_answer:
            print('Correct!')
            continue
        process_wrong_answer(user_answer, correct_answer)
        print("Let's try again, {user}!".format(user=user))
        break
    else:  # for - else. Run if no break occurs in cycle for.
        print('Congratulations, {user}!'.format(user=user))


def generate_question():
    """Return two numbers for gcd-game.

    Returns:
        random integer number generator
    """
    return (random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))


def calculate_answer(a, b):
    """Calculate correct answer for gcd-game.

    Args:
        a: number
        b: number

    Returns:
        the greatest common divisor
    """
    return str(gcd(a, b))


def get_user_answer(a, b):
    """Print question and return user answer.

    Args:
        a: number
        b: number

    Returns:
        user answer
    """
    print('Question: {a} {b}'.format(a=a, b=b))
    return prompt.string('Your answer: ', empty=True)
