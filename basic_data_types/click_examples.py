import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def cli(verbose):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")