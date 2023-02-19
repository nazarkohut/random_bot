"""
Has method for silent int casting.
"""


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
