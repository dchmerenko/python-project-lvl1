"""Brain-game even_game functional module."""

from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER, TRIES_LIMIT
from brain_games.lib import get_user_answer, is_even, process_wrong_answer


def play(user):
    """
    Play an even-odd game with the User.

    Args:
        user: User name
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(TRIES_LIMIT):
        question, number = generate_question()
        correct_answer = calculate_answer(number)
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
    number = randint(MIN_NUMBER, MAX_NUMBER)
    return str(number), number


def calculate_answer(number):
    """Calculate correct answer for even-game.

    Args:
        number: number

    Returns:
        yes or no if number is even
    """
    return 'yes' if is_even(number) else 'no'
