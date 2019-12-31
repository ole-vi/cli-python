import click
import subprocess

@click.command()
@click.argument('password')
def cli(password):
	"""changes the password for 'pi' user
	
	Changes the password for 'pi' user

	Example(type this in your terminal):
		treehouses password ABC
			Sets the password for 'pi' user to 'ABC'
	"""
	p = subprocess.Popen([ "/usr/sbin/chpasswd" ], universal_newlines=True, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(stdout, stderr) = p.communicate("pi:" + password + "\n")
	assert p.wait() == 0
	click.echo('Success: the password has been changed')
	if stdout or stderr:
		raise Exception("Error encountered changing the password!")
	