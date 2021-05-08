"""Brain-game gcd_game functional module."""

import random

import prompt
from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import gcd, get_user_answer, process_wrong_answer


def play(user):
    """
    Play a guess Greatest Common Divisor game with the User.

    Args:
        user: User name
    """
    print('Find the greatest common divisor of given numbers.')

    for _ in range(TRIES_LIMIT):
        question, args = generate_question()
        correct_answer = calculate_answer(args)
        user_answer = get_user_answer(question)
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
        string of two random integer number
    """
    a, b = tuple(random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))
    question = '{a} {b}'.format(a=a, b=b)
    args = (a, b)
    return question, args


def calculate_answer(args):
    """Calculate correct answer for gcd-game.

    Args:
        args: (a, b)

    Returns:
        the greatest common divisor
    """
    a, b = args
    return str(gcd(a, b))
