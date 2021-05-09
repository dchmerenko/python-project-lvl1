"""Brain-games config module."""

HIDDEN_MARK = '..'
TRIES_LIMIT = 3
MAX_NUMBER = 100
MIN_NUMBER = 0

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}
