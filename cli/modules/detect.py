import click

@click.command()
def cli():
	"""detects the hardware version of any device
	
	Detects and outputs the hardware info
	
	Example(type this in your terminal):
		treehouses detect
			Prints the hardware info
	"""
	