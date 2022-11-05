from utils.przyklady import execute

commands = [
    "'Jan Kowalski junior'.capitalize()",
    "'Jan Kowalski junior'.lower()",
    "'Jan Kowalski junior'.upper()",
    "'Jan Kowalski junior'.swapcase()",
    "'Jan Kowalski junior'.title()"
]
execute(commands, globals(), 'Zarządzanie wielkością liter...')
