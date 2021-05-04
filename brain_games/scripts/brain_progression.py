#!/usr/bin/env python
"""Brain-progression main module."""

from brain_games.games import progression_game
from brain_games.lib import welcome_user


def main():
    """Brain-even main function."""
    user = welcome_user()
    progression_game.play(user)


if __name__ == '__main__':
    main()
