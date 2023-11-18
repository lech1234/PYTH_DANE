"""
Moduł prezentuje opcje formatowania tekstów.
"""
from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'{:10}'.format('abc')",  # dosunięcie do lewej
        "'{:>10}'.format('abc')",  # dosunięcie do prawej
        "'{:^10}'.format('abc')"  # wyśrodkowanie (ew. nadmiarowy znak jest umieszczany z prawej strony)
    ]
    execute(commands, globals(), 'Min. szerokość argumentu i justowanie...')

    commands = [
        "'{:.<10}'.format('abc')"
    ]
    execute(commands, globals(), 'Znaki uzupełnienia...')

    commands = [
        "'{:.2}'.format('abc')",
        "'{:10.2}'.format('abc')"
    ]
    execute(commands, globals(), 'Przycięcie...')
