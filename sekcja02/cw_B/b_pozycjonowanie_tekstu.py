"""
Moduł prezentuje działanie metod justujących tekst.
"""
from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'Python'.ljust(10)",
        "'Python'.ljust(10, '-')",
        "'Python'.center(10)",
        "'Python'.center(10, '-')",
        "'Python'.rjust(10)",
        "'Python'.rjust(10, '-')",
        "'Python'.zfill(10)"
    ]
    execute(commands, globals(), 'Pozycjonowanie tekstu...')
