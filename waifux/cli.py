import click
from .ascii_waifus import get_random_waifu

@click.command()
def main():
    """Print a random waifu ASCII art"""
    print(get_random_waifu())
