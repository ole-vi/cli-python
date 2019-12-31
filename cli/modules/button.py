import click


@click.group()
def cli():
	"""detects the hardware version of any device
	
	Detects and outputs the hardware info
	
	Example(type this in your terminal):
		treehouses detect
			Prints the hardware info
	"""
	click.echo('yolo swaggins')

	
def command1():
	click.echo('yolo swaggins')

@cli.command()
def create():
    click.echo('create is invoked in command1.')


@cli.command()
def delete():
    click.echo('delete is invoked in command1.')


@cli.command()
def update():
    click.echo('update is invoked in command1.')
