"""Brain-game even_game functional module."""

from random import randint

import prompt
from brain_games.config import MAX_NUMBER, TRIES_LIMIT
from brain_games.lib import is_even


def play(user):
    """
    Play an even-odd game with the User.

    Args:
        user: User name
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(TRIES_LIMIT):
        question = generate_question()
        correct_answer = calculate_answer(question)
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
    """Return quiz number for even-game.

    Returns:
        random integer number
    """
    return randint(0, MAX_NUMBER)


def calculate_answer(number):
    """Calculate correct answer for even-game.

    Args:
        number: number

    Returns:
        yes or no if number is even
    """
    return 'yes' if is_even(number) else 'no'


def get_user_answer(question):
    """Print question and return user answer.

    Args:
        question: question

    Returns:
        user answer
    """
    print('Question: {question}'.format(question=question))
    return prompt.string('Your answer: ', empty=True)


def process_wrong_answer(wrong_answer, right_answer):
    """Print right and wrong answer.

    Args:
        wrong_answer: wrong answer
        right_answer: right_answer
    """
    print(
        "'{wrong_answer}' is wrong answer ;(.".format(
            wrong_answer=wrong_answer,
        ),
        end=' ',
    )
    print(
        "Correct answer was '{right_answer}'.".format(
            right_answer=right_answer,
        ),
    )
