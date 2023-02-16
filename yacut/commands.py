import click

from . import app, db


@app.cli.command()
def create_all():
    """Create all defined tables."""
    db.create_all()
    click.echo("Tables created.")
