#!/usr/bin/env python
"""Brain-even main module."""


from brain_games import even_game
from brain_games.cli import welcome_user


def main():
    """Brain-even main function."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    even_game.play(name)


if __name__ == '__main__':
    main()
