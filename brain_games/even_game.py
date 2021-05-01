"""Brain-game even_game functional module."""

from random import randint

import prompt
from brain_games.config import MAX_NUMBER, TRIES_LIMIT
from brain_games.lib import is_even


def play(name):
    """
    Play an even-odd game with the User.

    Args:
        name: User name
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(TRIES_LIMIT):
        number = randint(0, MAX_NUMBER)
        correct_answer = 'yes' if is_even(number) else 'no'
        user_answer = prompt.string(
            'Question: {number}\nYour answer: '.format(number=number),
            empty=True,
        )
        if user_answer == correct_answer:
            print('Correct!')
            continue
        print(
            "'{user_answer}' is wrong answer ;(.".format(
                user_answer=user_answer,
            ),
            end=' ',
        )
        print(
            "Correct answer was '{correct_answer}'.".format(
                correct_answer=correct_answer,
            ),
        )
        print("Let's try again, {name}!".format(name=name))
        break
    else:  # for - else. Run if no break occurs in cycle for.
        print('Congratulations, {name}!'.format(name=name))
