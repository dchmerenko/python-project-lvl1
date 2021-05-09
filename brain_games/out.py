"""Brain-games print-out function module."""


import prompt


def welcome_user():
    """
    Prompt User name and print welcome message. Return User name.

    Returns:
         User name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def base_play(*, start_msg, tries_limit, generate_question, calculate_answer):
    """Return Base play function.

    Args:
        start_msg: start game message
        tries_limit: tries limit
        generate_question: question generating function
        calculate_answer: answer calculating function
    """
    user = welcome_user()
    print(start_msg)

    for _ in range(tries_limit):
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


def get_user_answer(question):
    """Print question and return user answer.

    Args:
        question: user question

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
