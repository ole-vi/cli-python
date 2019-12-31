import click
import os


def print_bluetooth_id(number = 0):
	try:
		f = open("/etc/bluetooth-id", "r")
		bid = f.read()		
		f.close()	
		nname = platform.node()				
		if (number == 0):
			click.echo(bid)
		else:
			click.echo(nname + "-" + bid)	
	except:
		click.echo('No ID. Bluetooth service is not on.')
		
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
	"""displays the bluetooth network name with the 4 random digits attached
	
	Optionally displays Bluetooth ID individually with the use of argument [number]
	
	\b
	Example(type this in your terminal):
		treehouses bluetoothid
			treehouses-9012
		treehouses bluetoothid number
			9012
	"""	
	if ctx.invoked_subcommand is None:
		print_bluetooth_id()
	
@cli.command()		
def number():
	"""display only the bluetooth id"""
	print_bluetooth_id(1)