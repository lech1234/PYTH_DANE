from utils.przyklady import execute

commands = [
    "'{:d}'.format(123)",
    "'{:6d}'.format(123)",
    "'{:06d}'.format(123)",
    "'{:06d}'.format(-123)",
    "'{:+d}'.format(123)",  # obowiązkowo znak (minus lub plus)
    "'{: d}'.format(123)",  # obowiązkowo znak (minus lub spacja)
    "'{:=6d}'.format(-123)",  # znak na początku
    "'{:=+6d}'.format(123)"  # obowiązkowo znak na początku
]
execute(commands, globals(), 'Liczby całkowite...')

commands = [
    "'{:f}'.format(12.3456)",
    "'{:12f}'.format(12.3456)",
    "'{:12.2f}'.format(12.3456)",
    "'{:.2f}'.format(12.3456)"
]
execute(commands, globals(), 'Liczby zmiennoprzecinkowe...')
