import click

# sets up a group so you can have multiple commands
@click.group()
def cli():
    pass

# tells the click library that the following is a new command
@cli.command()
# sets up options and arguments
@click.option("-t", "--times", default = 1)
@click.option("-f", "--french", is_flag = True, default = False)
@click.argument("name")
# the actual function of the command, the arguments passed in are automatically parsed by the library
def hello(times, name, french):
    for i in range(times):
        click.echo(("hello " + name) if not french else ("Bonjour, " + name+"!")) 
        # echo is used  because it is more consistent than print, but it doesnt really matter here

# this is just needed to make it work without packaging it
if __name__ == '__main__':
    cli()

"""
example usage: many ways to do the exact same thing
python3 example.py hello --times=3 --french yourname
python3 example.py hello -t 3 -f "Billy Bob Joe"
python3 example.py hello "Billy Bob Joe" -t3 --french 
python3 example.py hello -t3 "Billy Bob Joe" -f
"""
