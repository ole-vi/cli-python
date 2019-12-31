import click
import os.path

@click.command()
def cli():
	"""shows if reboot is required to apply changes
	
	Shows if a reboot is required to apply the configuration changes done by this command
	
	\b
	Example(type this in your terminal):
		treehouses rebootneeded
			output: True
	"""
	click.echo(os.path.isfile("/etc/reboot-needed"))