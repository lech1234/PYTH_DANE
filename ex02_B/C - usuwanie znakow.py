from utils.przyklady import execute

commands = [
    "'tattoo'.lstrip('at')"
]
execute(commands, globals(), "z początku...")

commands = [
    "'tattoo'.strip('ot')"
]
execute(commands, globals(), "z początku i końca...")

commands = [
    "'tattoo'.rstrip('ot')"
]
execute(commands, globals(), "\nz końca...")
