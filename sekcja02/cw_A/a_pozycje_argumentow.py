"""
Moduł przedstawia przykłady formatowania danych, w których odwołujemy się do parametrów poprzez ich pozycję.
"""

from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'{} {}'.format('abc', 'xyz')"
    ]
    execute(commands, globals(), 'Argumenty są wstawiane w podanej kolejności...')

    commands = [
        "'{0} {1}'.format('abc', 'xyz')",
        "'{1} {0}'.format('abc', 'xyz')"
    ]
    execute(commands, globals(), 'Można wskazać pozycję argumentu...')

    commands = [
        "'{0} {1} {0}'.format('abc', 'xyz')"
    ]
    execute(commands, globals(), 'Do tego samego argumentu można się odwołać wielokrotnie...')
