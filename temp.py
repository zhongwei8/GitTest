import click
from datetime import datetime, date, time


@click.command()
@command.argument('path')
def main(path):
    print(f'path = {path}')
