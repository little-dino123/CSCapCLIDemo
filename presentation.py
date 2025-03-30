import click  # Import the Click library

# This part sets up the basic structure of our CLI.  Think of it as the main container.
@click.group()
def cli():
    """This is a simple CLI application.  It can say hello and repeat words!"""
    pass  # This 'pass' doesn't do anything, but it's required here.

# This is a command called "hello".  It greets someone.
@cli.command()  # This tells Click that 'hello' is a command within the 'cli' group.
@click.option('--name', default='World', help='The name to say hello to.')  # This adds an option.
def hello(name):
    click.echo(f"Hello, {name}!")  # This prints the greeting.  f-strings are cool!

# This is another command, called "repeat".  It repeats a word.
@cli.command()  # This makes 'repeat' a command.
@click.option('--count', default=1, help='Number of times to repeat.')  # This is an option for how many times to repeat.
@click.argument('word')  # This is a *required* argument: the word to repeat.
def repeat(word, count):
    """Repeats a word a certain number of times."""
    for _ in range(count):  # This is a loop that runs 'count' times.
        click.echo(word)  # This prints the word each time through the loop.

# This is the special part that makes our CLI run when we type 'python my_cli.py'.
if __name__ == '__main__':
    cli()  # This calls the 'cli' function, which starts the whole thing.

# To run this:
# 1.  Save it as a file (e.g., 'my_cli.py').
# 2.  Open your terminal or command prompt.
# 3.  Navigate to the directory where you saved the file (using the 'cd' command).
# 4.  Run it using:
#     python my_cli.py  # This will show the help message.
#     python my_cli.py hello --name Alice  # This will say "Hello, Alice!".
#     python my_cli.py repeat hello --count 3 # This will print hello 3 times
#     python my_cli.py repeat bye # this will print bye once
