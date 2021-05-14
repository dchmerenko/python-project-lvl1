"""Brain-games print-out function module."""


import prompt


def welcome_user():
    """Prompt User name and print welcome message.

    Returns:
         User name
    """
    print('Welcome to the Brain Games!')
    user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user))
    return user


def base_play(*, start_msg, tries_limit, get_question_answer):
    """Return Base play function.

    Args:
        start_msg: start game message
        tries_limit: tries limit
        get_question_answer: question-answer generator
    """
    user = welcome_user()
    print(start_msg)

    for _ in range(tries_limit):
        question, answer = get_question_answer()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ', empty=True)
        if user_answer == answer:
            print('Correct!')
            continue
        wrong_answer_msg = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
        print(wrong_answer_msg.format(user_answer, answer))
        print("Let's try again, {0}!".format(user))
        break
    else:  # for - else. Run if no break occurs in cycle for.
        print('Congratulations, {0}!'.format(user))
