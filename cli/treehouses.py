import click
import os

plugin_folder = os.path.join(os.path.dirname(__file__), 'modules')

# credit to yu-iskw https://github.com/yu-iskw/click-custom-multi-commands-example
class treehousesCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and not filename.startswith('__init__'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

# No documented way to change from option to command for Help. 
# These options will have to be a compromise 
# Note throwing 'help' in there didn't work this likely uses getopt
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help', '--h'])
@click.command(context_settings=CONTEXT_SETTINGS, cls=treehousesCLI)
def cli():
    """gives you a more detailed info about the command or will output this"""
    pass

	
if __name__ == '__main__':
    cli()
