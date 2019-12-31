import click
import subprocess

@click.command()
def cli():
	"""expands the partition of the RPI image to the maximum of the SDcard
	
	Expands the partition of the raspberry pi image to use the whole disk
	
	\b
	Example(type this in your terminal):
		treehouses expandfs
			The partition of the SD card in which the raspberry pi image is stored will be expanded to match the available space on the SD card after a reboot
	"""
	subprocess.run(["raspi-config", "--expand-rootfs", ">/dev/null", "2>/dev/null"])
	click.echo('Success: the filesystem will be expanded on the next reboot')