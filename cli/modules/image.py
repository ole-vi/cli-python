import click

@click.command()
def cli():
	"""Returns version of the system image installed
	
	\b
	Example(type this in your terminal):
		treehouses image
			Prints the current version of the system image.
	"""
	f = open("/boot/version.txt", "r")
	text = f.read()
	click.echo(text)
	f.close()