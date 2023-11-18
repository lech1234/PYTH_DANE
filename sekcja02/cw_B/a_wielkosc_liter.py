"""
Moduł prezentuje działanie metod wpływających na wielkość liter w tekście.
"""
from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'Jan Kowalski junior'.capitalize()",
        "'Jan Kowalski junior'.lower()",
        "'Jan Kowalski junior'.upper()",
        "'Jan Kowalski junior'.swapcase()",
        "'Jan Kowalski junior'.title()"
    ]
    execute(commands, globals(), 'Zarządzanie wielkością liter...')
