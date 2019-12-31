import click
import os
import subprocess

@click.command()
@click.argument("timezone")
def cli(timezone):
	"""sets the timezone of the system
	
	Sets the system timezone
	
	\b
	Example(type this in your terminal):
		treehouses timezone Etc/GMT-3
			This will set the raspberry pi time to GMT-3
			When using Etc/GMT you can specify the offset, from GMT-14 up to GMT+12
			Available timezones are inside /usr/share/zoneinfo/
	"""
	if os.path.isfile("/usr/share/zoneinfo/" + timezone):
		try:
			os.remove("/etc/localtime")
		except:
			pass
		try:
			f = open("/etc/timezone", "w+")
			f.write(timezone)		
			f.close()	
			click.echo('Success: the timezone has been set')
			subprocess.run(["dpkg-reconfigure", "-f", "noninteractive", "tzdata", "2>/dev/null"])
		except:  		
			click.echo('Error: trying to set timezone')		
	else:
		click.echo('Error: the timezone is not supported')
		