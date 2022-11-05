from utils.przyklady import execute

commands = [
    "'to be or not to be'.split()",
    "'to be or not to be'.split(sep='be')",
    "'to be or not to be'.split(maxsplit=2)",
    "'to be or not to be'.rsplit(maxsplit=2)",
    "'to be\\nor\\nnot to be'.splitlines()",
    "'to be\\nor\\nnot to be'.splitlines(True)",
    "'to be or not to be'.partition('be')",
    "'to be or not to be'.rpartition('be')"
]
execute(commands, globals())
