#!/usr/bin/env python
"""Brain-even main module."""

from brain_games.games import even_game
from brain_games.lib import welcome_user


def main():
    """Brain-even main function."""
    user = welcome_user()
    even_game.play(user)


if __name__ == '__main__':
    main()
