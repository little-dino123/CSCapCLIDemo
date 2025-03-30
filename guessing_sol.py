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

# YOUR CODE
@cli.command()
@click.argument("max")
@click.option("--min", default = 0)
def newnum(min, max):
    # max should be an argument
    # min should be an option, with default 1
    # neg should be a flag, with a short of "-n"
    target = random.randint(min, int(max))
    guesses = 0
    click.echo("Number Generated!")

"""
command 2: guess
a num argument
prints if it is too high or too low
"""
def guess(num):
    num = int(num)
    if num<target:
        click.echo("Too low")
    elif num>target:
        click.echo("Too high")
    else:
        click.echo("Just right")
    guesses += 1
"""
command 3: numguesses
no options or arguments
prints guesses
"""
@cli.command()
def numguesses():
    click.echo(guesses)
"""
command 4: hint
a "-t"/"--type" option, default = "random"
gives a hint, like if the target is even, first digit, last digit, etc
"""
@cli.command()
@cli.option("-t", "--type", default = "random")
def hint(type):
    if type.equals("random"):
        type = random.choice(["oddness", "first digit", "last digit"])
    if type.equals("oddness"):
        click.echo("The target is even" if target%2==0 else "The target is odd")
    elif type.equals("first digit"):
        click.echo("The target's first digit is", target//(10**math.floor(math.log(target, 10))))
    elif type.equals("last digit"):
        click.echo("The target's last digit is", target%10)
    else:
        click.echo("Sorry, that is not a valid hint type")
    

"""
any other features you might want to add
"""

if __name__ == '__main__':
    cli()