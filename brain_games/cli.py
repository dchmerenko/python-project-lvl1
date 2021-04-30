"""CLI functions module."""

import prompt


def welcome_user():
    """Prompt User name and print welcome message."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
