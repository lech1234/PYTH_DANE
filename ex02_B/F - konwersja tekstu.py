from utils.przyklady import execute

commands = [
    "'ananas'.replace('nana', 'loe')",
    "'Sodoma'.translate(str.maketrans('dmS', 'mrG'))",
    "'_'.join('Python')"
]
execute(commands, globals())
