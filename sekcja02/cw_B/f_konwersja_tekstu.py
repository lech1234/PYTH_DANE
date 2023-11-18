"""
Moduł prezentuje działanie metod umożliwiających konwersję tekstu.
"""
from utils.przyklady import execute

if __name__ == '__main__':

    commands = [
        "'ananas'.replace('nana', 'loe')",
        "'Sodoma'.translate(str.maketrans('dmS', 'mrG'))",
        "'_'.join('Python')"
    ]
    execute(commands, globals())
