import click
import math
# sets up a group so you can have multiple commands
@click.group()
def cli():
    pass

# YOUR CODE
@cli.command()
@click.argument("num1")
@click.argument("num2")
@click.option("--op", default = "add")
@click.optoion("-n", "--neg", is_flag = True, default = False)
def calc(num1, num2, op, neg):
    # nums should be arguments
    # op should be an option with the default of "add"
    # neg should be a flag, with a short of "-n"

    result = 0
    if op == "add":
        result = (num1 + num2)
    elif op == "sub":
        result = (num1 - num2)
    elif op == "mul":
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
@cli.command()
@click.argument("text")
@click.option("-c", "--cap", default = False, is_flag = True)
@click.option("-l", "--low", default = False, is_flag = True)
@click.option("pre", default = "")
@click.option("post", default = "")
def write(text, cap, low, pre, post):
    # text shoulb be an argument
    # cap and low should be flags, with -c and -l shorts respectively
    # pre and post should be options
    if cap: text = text.upper()
    if low: text = text.lower()
    click.echo(pre + text + post)






if __name__ == '__main__':
    cli()
"""
try testing if these work
python3 solution.py calc --op mult 6 3
python3 solution.py calc --op=sub -n 2048 512
python3 solution.py calc --op=log 1048576 2 --neg
python3 solution.py calc 3 4
"""
