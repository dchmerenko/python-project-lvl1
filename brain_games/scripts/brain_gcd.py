#!/usr/bin/env python
"""Brain-gcd main module."""

from brain_games.games import gcd_game
from brain_games.lib import welcome_user


def main():
    """Brain-gcd main function."""
    user = welcome_user()
    gcd_game.play(user)


if __name__ == '__main__':
    main()
