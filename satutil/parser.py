import click

# allow -h for help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--home', envvar='SATUTILS_HOME', default='~/sat-utils',
              help='Directory of sat-utils data directories')
@click.option('--verbose', '-v', default=1, type=click.IntRange(0,4),
              help='Verbosity level')
@click.option('--ids',
             help='Provide full scene IDs, based on sensor (e.g.,LC81660392014196LGN00)')
def cli(home, verbose, ids):
    pass


@click.command()
# date/time
@click.option('-s', '--start', help='Start Date - Most formats are accepted '
                           'e.g. Jun 12 2014 OR 06/12/2014')
@click.option('-e', '--end', help='End Date - Most formats are accepted '
                           'e.g. Jun 12 2014 OR 06/12/2014')
@click.option('--latest', default=-1, type=int, help='return N latest images within last 365 days')
@click.option('-l', '--limit', type=int, default=10, help='Search results limit')
# geospatial
@click.option('--lat', type=float, help='The latitude')
@click.option('--lon', type=float, help='The longitude')
@click.option('--address', type=str, help='The address')

@click.option('--save', default=False, help='Save query to disk with provided filename')
@click.option('-c', '--cloud', type=float, default=100.0, help='Maximum cloud percentage')
def search(**kwargs): #start, end, latest, limit, lat, lon, address, save, cloud):
    """ Search sensor metadata for matching scenes """
    click.echo('search')
    click.echo(kwargs)


@click.command()
@click.option('-q', '--query', help='Filename to a saved query')
@click.option('-b', '--bands', nargs="+", help='Specific bands to download')
@click.option('-d', '--dest', help='Destination path (defaults to sat-util data path)', default=None)
def download(**kwargs):
    """ Download image scenes """
    click.echo('download')
    click.echo(kwargs)

@click.command()
@click.option('-q', '--query', help='Filename to a saved query')
def process(**kwargs):
    """ Process scenes into products """
    click.echo('process')
    click.echo(kwargs)
