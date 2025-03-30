import click
import math
import random
# sets up a group so you can have multiple commands
@click.group()
def cli():
    pass

target = 0
guesses = 0

# Make a simple guessing game with CLIs
"""
command 1: newnum
a max argument, and a "--min" option
generates a random num in that range and set "target" to it
also resets the guesses to 0
"""

"""
command 2: guess
a num argument
prints if it is too high or too low
"""

"""
command 3: numguesses
no options or arguments
prints guesses
"""

"""
command 4: hint
a "-t"/"--type" option, default = "random"
gives a hint, like if the target is even, first digit, last digit, etc
"""


"""
any other features you may want to add
"""

if __name__ == '__main__':
    cli()