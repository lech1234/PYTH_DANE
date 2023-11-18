"""
Moduł prezentuje działanie metod usuwających znaki z tekstu.
"""
from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'tattoo'.lstrip('at')"
    ]
    execute(commands, globals(), "z początku...")

    commands = [
        "'tattoo'.strip('ot')"
    ]
    execute(commands, globals(), "z początku i końca...")

    commands = [
        "'tattoo'.rstrip('ot')"
    ]
    execute(commands, globals(), "\nz końca...")
