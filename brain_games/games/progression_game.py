"""Brain-game progression_game functional module."""

import random

import prompt
from brain_games.config import HIDDEN_MARK, MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import arithmetic_progression, process_wrong_answer


def play(user):
    """
    Play a guess missed element of Arithmetic progression game with the User.

    Args:
        user: User name
    """
    print('Find the missed element of Arithmetic progression.')

    for _ in range(TRIES_LIMIT):
        hidden_value, progression = generate_question()
        correct_answer = calculate_answer(hidden_value)
        user_answer = get_user_answer(progression)
        if user_answer == correct_answer:
            print('Correct!')
            continue
        process_wrong_answer(user_answer, correct_answer)
        print("Let's try again, {user}!".format(user=user))
        break
    else:  # for - else. Run if no break occurs in cycle for.
        print('Congratulations, {user}!'.format(user=user))


def generate_question():  # noqa: WPS210 Found too many local variables
    """Return progression and hidden value for progression-game.

    Returns:
        progression: random arithmetic progression with one hidden value
        hidden_value: hidden value of arithmetic progression
    """
    first, step = (random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2))
    progression = arithmetic_progression(first, step)
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = HIDDEN_MARK
    return hidden_value, ' '.join(progression)


def calculate_answer(hidden_value):
    """Calculate correct answer for progression-game.

    Args:
        hidden_value: hidden value of arithmetic progression

    Returns:
        hidden_value: hidden value of arithmetic progression
    """
    return hidden_value


def get_user_answer(progression):
    """Print question and return user answer.

    Args:
        progression: arithmetic progression with one hidden value

    Returns:
        user answer
    """
    print('Question: {progression}'.format(progression=progression))
    return prompt.string('Your answer: ', empty=True)
