from utils.przyklady import execute

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
