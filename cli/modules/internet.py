import click
from urllib.request import urlopen

@click.command()
def cli():
	"""checks if the rpi has access to internet
	
	Outputs true if the rpi can reach internet, or false if it doesn't
	
	\b
	Example(type this in your terminal):
		treehouses internet
			the rpi has access to internet -> output: true
			the rpi doesn't have access to internet -> output: false
	"""		
	try:
		urlopen("https://www.google.com/", timeout=3)
		click.echo('true')
	except:
		click.echo('false')