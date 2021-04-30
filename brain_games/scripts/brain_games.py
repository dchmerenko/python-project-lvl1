#!/usr/bin/env python
"""Brain-games main module."""

from brain_games.cli import welcome_user


def main():
    """Brain-game main function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
