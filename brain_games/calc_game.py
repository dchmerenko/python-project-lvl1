"""Brain-game calc_game functional module."""

import random

import prompt
from brain_games.config import MAX_NUMBER, TRIES_LIMIT


def play(name):
    """
    Play a calculation game with the User.

    Args:
        name: User name
    """
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }

    print('What is the result of the expression?')

    for _ in range(TRIES_LIMIT):
        a, b = (random.randint(0, MAX_NUMBER) for _ in range(2))
        operator = random.choice(tuple(operations))
        correct_answer = str(operations.get(operator)(a, b))
        user_answer = prompt.string(
            'Question: {a} {operator} {b}\nYour answer: '.format(
                a=a,
                b=b,
                operator=operator,
            ),
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
