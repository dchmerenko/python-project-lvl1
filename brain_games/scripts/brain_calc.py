#!/usr/bin/env python
"""Brain-calc main module."""

from brain_games.games import calc_game
from brain_games.out import welcome_user


def main():
    """Brain-calc main function."""
    user = welcome_user()
    calc_game.play(user)


if __name__ == '__main__':
    main()
