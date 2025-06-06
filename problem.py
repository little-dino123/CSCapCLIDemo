import click
import math
from scipy.stats import norm
# sets up a group so you can have multiple commands
@click.group()
def cli():
    pass

# YOUR CODE






def calc(num1, num2, op, neg):
    # nums should be arguments
    # op should be an option with the default of "add"
    # neg should be a flag, with a short of "-n"
    result = 0
    if op == "add":
        result = (num1 + num2)
    elif op == "sub":
        result = (num1 - num2)
    elif op == "mult":
        result = (num1 * num2)
    elif op == "div":
        result = (num1 / num2)
    elif op == "mod":
        result = (num1 % num2)
    elif op == "floor":
        result = (num1 // num2)
    elif op == "exp":
        result = (num1 ** num2)
    elif op == "log":
        result = (math.log(num1, num2))
    else:
        result = ("invalid operation")
    
    if neg:
        result = -result

    click.echo(result)

# YOUR CODE







def write(text, cap, low, pre, post):
    # text shoulb be an argument
    # cap and low should be flags, with -c and -l shorts respectively
    # pre and post should be options
    if cap: text = text.upper()
    if low: text = text.lower()
    click.echo(pre + text + post)

# YOUR CODE






def normalcdf(min, max, mean, sd):
    # max is an argument
    # min, mean, and sd are options, with default values of -1000000, 0, and 1 respectively
    click.echo(norm.cdf(max, mean, sd) - norm.cdf(min, mean, sd))

# YOUR CODE





def convert(temp, startunit, both):
    # temp and startunit are arguments
    # --both/-b is a flag
    if startunit=="c":
        other = temp*9/5+32
        if both: click.echo(f"{temp} degrees celcius is {other} degrees farenheit")
        else: click.echo(f"{other}F°")
    elif startunit=="f":
        other = (temp-32)*5/9
        if both: click.echo(f"{temp} degrees farenheit is {other} degrees celcius")
        else: click.echo(f"{other}C°")
    
if __name__ == '__main__':
    cli()
"""
try testing if these work
python3 problem.py calc --op mult 6 3
python3 problem.py calc --op=sub -n 2048 512
python3 problem.py calc --op=log 1048576 2 --neg
python3 problem.py calc 3 4

python3 problem.py write -c heLLo
python3 problem.py write hEllO -l --post=" world"

python3 problem.py normalcdf 0
python3 problem.py normalcdf --min=100 23742397 --mean=100 --sd=347283

python3 problem.py convert 17 c
python3 problem.py convert 62.6 f -b
"""