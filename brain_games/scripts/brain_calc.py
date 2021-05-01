#!/usr/bin/env python
"""Brain-calc main module."""


from brain_games import calc_game
from brain_games.cli import welcome_user


def main():
    """Brain-calc main function."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    calc_game.play(name)


if __name__ == '__main__':
    main()
