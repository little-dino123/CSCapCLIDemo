import click
import math
# sets up a group so you can have multiple commands
@click.group()
def cli():
    pass

# try coding this portion given the funtion below
@cli.command()
@click.argument("num1")
@click.argument("num2")
@click.option("--op", default = "add")
def calc(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)
    if op == "add":
        click.echo(num1 + num2)
    elif op == "sub":
        click.echo(num1 - num2)
    elif op == "mul":
        click.echo(num1 * num2)
    elif op == "div":
        click.echo(num1 / num2)
    elif op == "mod":
        click.echo(num1 % num2)
    elif op == "floor":
        click.echo(num1 // num2)
    elif op == "exp":
        click.echo(num1 ** num2)
    elif op == "log":
        click.echo(math.log(num1, num2))
    else:
        click.echo("invalid operation")

if __name__ == '__main__':
    cli()
"""
try testing if these work
python3 solution.py calc --op mult 6 3
python3 solution.py calc --op=sub 2048 512
python3 solution.py calc --op=log 1048576 2
python3 solution.py calc 3 4
"""
