#!/usr/bin/env python
"""Brain-prime main module."""

from brain_games.games import prime_game
from brain_games.out import welcome_user


def main():
    """Brain-prime main function."""
    user = welcome_user()
    prime_game.play(user)


if __name__ == '__main__':
    main()
