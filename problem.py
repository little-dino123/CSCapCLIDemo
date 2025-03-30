import click
import math

@click.group()
def cli():
    pass

# try coding this portion given the funtion below







def calc(num1, num2, op, neg):
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

if __name__ == '__main__':
    cli()
"""
try testing if these work
python3 problem.py calc --op mult 6 3
python3 problem.py calc --op=sub -n 2048 512 
python3 problem.py calc --op=log 19683 3 --neg
python3 problem.py calc 3 9 --op exp

as you can see, where the option goes doesn't really matter, but the order of the arguments do matter
you can also choose to use = or not, but using it does make it look neater
"""