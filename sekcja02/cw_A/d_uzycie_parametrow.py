"""
Moduł prezentuje opcje odwoływania się do parametrów formatowania poprzez nazwy symboliczne.
"""
from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'{imie} {nazwisko}'.format(imie='Jan', nazwisko='Kowalski')"
    ]
    execute(commands, globals(), 'Użycie parametrów nazwanych...')

    commands = [
        "'{:{align}{prec}}'.format('abcd', align='^', prec=10)"
    ]
    execute(commands, globals(), '\nMożna sparametryzować także szerokość i precyzję...')
