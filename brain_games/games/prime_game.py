"""Brain-game prime_game functional module."""

import random

import prompt
from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import is_prime, process_wrong_answer


def play(user):
    """
    Play an Is it prime number game with the User.

    Args:
        user: User name
    """
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(TRIES_LIMIT):
        number = generate_question()
        correct_answer = calculate_answer(number)
        user_answer = get_user_answer(number)
        if user_answer == correct_answer:
            print('Correct!')
            continue
        process_wrong_answer(user_answer, correct_answer)
        print("Let's try again, {user}!".format(user=user))
        break
    else:  # for - else. Run if no break occurs in cycle for.
        print('Congratulations, {user}!'.format(user=user))


def generate_question():
    """Return numbers for prime-game.

    Returns:
        random integer number
    """
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def calculate_answer(number):
    """Calculate correct answer for prime-game.

    Args:
        number: integer number

    Returns:
        'yes' if the number is prime else 'no'
    """
    return 'yes' if is_prime(number) else 'no'


def get_user_answer(number):
    """Print question and return user answer.

    Args:
        number: integer number

    Returns:
        user answer
    """
    print('Question: {number}'.format(number=number))
    return prompt.string('Your answer: ', empty=True)
