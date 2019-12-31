import click
import subprocess

@click.command()
def cli():
	"""tests internet download and upload speed
	
	Tests internet download and upload speed
	
	Example(type this in your terminal):
		treehouses speedtest
			Outputs the speed of internet download and upload speed
	"""
	subprocess.run(["speedtest-cli"])