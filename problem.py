import click
import math

@click.group()
def cli():
    pass

# try coding this portion given the funtion below







def calc(num1, num2, op):
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
python3 problem.py calc --op mult 6 3
python3 problem.py calc --op=sub 2048 512
python3 problem.py calc --op = log 19683 3
python3 problem.py calc 3 9 --op exp

as you can see, where the option goes doesn't really matter, but the order of the arguments do matter
you can also choose to use = or not, but using it does make it look neater
"""