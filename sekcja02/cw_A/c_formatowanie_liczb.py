"""
Moduł prezentuje opcje formatowania liczb.
"""
from utils.przyklady import execute
import locale

if __name__ == '__main__':

    commands = [
        "'{:d}'.format(123)",
        "'{:6d}'.format(123)",
        "'{:06d}'.format(123)",
        "'{:06d}'.format(-123)",
        "'{:+d}'.format(123)",  # obowiązkowo znak (minus lub plus)
        "'{: d}'.format(123)",  # obowiązkowo znak (minus lub spacja)
        "'{:=6d}'.format(-123)",  # znak na początku
        "'{:=+6d}'.format(123)",  # obowiązkowo znak na początku
        "'{:c}'.format(123)"  # konwersja na znak
    ]
    execute(commands, globals(), 'Liczby całkowite...')

    commands = [
        "'{:,d}'.format(1234567890)",
        "'{:_d}'.format(1234567890)",
        "locale.setlocale(locale.LC_ALL, 'pl.utf8')",
        "'{:n}'.format(1234567890)"
    ]
    execute(commands, globals(), 'Grupowanie cyfr...')

    commands = [
        "'{:d}'.format(123)",
        "'{:b}'.format(123)",
        "'{:o}'.format(123)",
        "'{:x}'.format(123)",
        "'{:X}'.format(123)",
    ]
    execute(commands, globals(), 'Różne systemy pozycyjne...')

    commands = [
        "'{:f}'.format(12.3456)",
        "'{:12f}'.format(12.3456)",
        "'{:12.2f}'.format(12.3456)",
        "'{:.2f}'.format(12.3456)"
    ]
    execute(commands, globals(), 'Liczby zmiennoprzecinkowe...')
