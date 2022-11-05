from utils.przyklady import execute

commands = [
    "'{imie} {nazwisko}'.format(imie='Jan', nazwisko='Kowalski')"
]
execute(commands, globals(), 'Użycie parametrów nazwanych...')

commands = [
    "'{:{align}{prec}}'.format('abcd', align='^', prec=10)"
]
execute(commands, globals(), '\nMożna sparametryzować także szerokość i precyzję...')
