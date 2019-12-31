import click
from gpiozero import CPUTemperature

def print_cpu_temp(disp = 0):
	cpu = CPUTemperature()
	if disp is 1:
		click.echo(cpu.temperature + "°C")
	elif disp is 2:		
		click.echo((9.0/5.0 * cpu.temperature + 32) + "°F")
	else:
		click.echo(cpu.temperature)


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
	"""displays raspberry pi's CPU temperature
	
	Measures CPU temperature of Raspberry Pi
	
	\b
	Example(type this in your terminal):
		treehouses temperature
			47.2
		treehouses temperature celsius
			47.2°C
		treehouses temperature fahrenheit
			117.0°F
	"""
	if ctx.invoked_subcommand is None:
		print_cpu_temp()	
		
		
@cli.command()		
def celsius():
	"""display cpu temperature in degrees celsius"""
	print_cpu_temp(1)

	
@cli.command()
def fahrenheit():
	"""display cpu temperature in degrees fahrenheit"""
	print_cpu_temp(2)