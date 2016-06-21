#from .parser import SatParser
#from .version import __version__
#from ssearch import Search

import click
from satutil.parser import cli, search, download, process

# collection of 
#CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# group of subcommands
#@click.group(context_settings=CONTEXT_SETTINGS)
#def cli():
#    title = 'Sat-util CLI'
    #try:
    #    parser = SatParser(description=title)
    #    if args.subs == 'search':
    #        results = Search.query(**args)
    #    elif args.subs == 'download:'
    #        results = Search.query(**args)


# add the subcommands
cli.add_command(search)
cli.add_command(download)
cli.add_command(process)

