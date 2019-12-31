import click


@click.group()
def cli():
	"""switches between bluetooth hotspot mode / regular bluetooth and starts the service
	
	Switches between hotspot / regular bluetooth mode, or displays the bluetooth mac address
	
	\b
	Example(type this in your terminal):
		treehouses bluetooth on
			This will start the bluetooth server, which lets 
			the user control the raspberry pi using the mobile app.
		treehouses bluetooth off
			This will stop the bluetooth server, and 
			bring everything back to regular mode.
			This will also remove the bluetooth device id.
		treehouses bluetooth pause
			Performs the same as treehouses bluetooth off
			The only difference is that this command 
			will not remove the bluetooth device id.
		treehouses bluetooth mac
			This will display the bluetooth MAC address
	"""


@cli.command()
def on():
    click.echo('create is invoked in command1.')


@cli.command()
def off():
    click.echo('delete is invoked in command1.')


@cli.command()
def pause():
    click.echo('update is invoked in command1.')

	
@cli.command()
def mac():
    try:
		f = open("/sys/kernel/debug/bluetooth/hci0/identity","r")
		macadd = f.read()
		f.close()	
		click.echo(macadd[0:17])		
	except:  		
		click.echo('Error: trying to read mac address')		