import argparse


class SatParser(argparse.ArgumentParser):
    """ Extends argparse """

    def __init__(self, title='', **kwargs):
        super(SatParser, self).__init__(**kwargs)
        self.title = title
        self.formatter_class = argparse.ArgumentDefaultsHelpFormatter

        # basic options
        self.add_argument('-v', '--verbose', type=int, help='Verbosity level (0-3)', default=1)
        # TODO - logging options

        # generic scene ID argument
        self.add_argument('--ids', nargs="+",
                          help="Provide full scene IDs, based on the sensor (e.g. LC81660392014196LGN00)")

        self.subparsers = self.add_subparsers(dest='command')

    def error(self, message):
        self.print_help()

    def add_search(self):
        """ Add search options """
        parser = self.subparsers.add_parser('search', help='Search metadata')

        group = parser.add_argument_group('search options')

        group.add_argument('--save', action='store_true', default=False,
                           help='Save query to disk with provided filename')
        group.add_argument('-l', '--limit', default=10, type=int, help='Search results limit')
        group.add_argument('--latest', default=-1, type=int, help='return N latest images within last 365 days')

        # dates
        group.add_argument('-s', '--start', help='Start Date - Most formats are accepted '
                           'e.g. Jun 12 2014 OR 06/12/2014')
        group.add_argument('-e', '--end', help='End Date - Most formats are accepted '
                           'e.g. Jun 12 2014 OR 06/12/2014')

        # goospatial
        # TODO - consider replace with single location arg: check for lat/lon, then JSON, then address
        group.add_argument('--lat', type=float, help='The latitude')
        group.add_argument('--lon', type=float, help='The longitude')
        group.add_argument('--address', type=str, help='The address')
        group.add_argument('--geojson', type=str, help='GeoJSON polygon (EPSG:4326) for area of interest')

        # other filters
        group.add_argument('-c', '--cloud', type=float, default=100.0, help='Maximum cloud percentage')

        # replace with single var that is format of response?
        #group.add_argument('--json', action='store_true', help='Returns a bare JSON response')
        #group.add_argument('--geojson', action='store_true', help='Returns a geojson response')
        # this is sensor specific - add  to subclass
        # parser.add_argument('--gids', '--pathrow',
        #                    help='Paths and Rows in order separated by comma. Use quotes ("001").'
        #                    'Example: path,row,path,row 001,001,190,204')
        return group

    def add_download(self):
        """ Add download options """
        parser = self.subparsers.add_parser('download', help='Download data')
        group = parser.add_argument_group('download options')

        group.add_argument('-q', '--query', help='Filename to a saved query')

        group.add_argument('-b', '--bands', nargs="+", help='Specific bands to download')

        group.add_argument('-d', '--dest', help='Destination path (defaults to sat-util data path)', default=None)

        # data specific
        #parser = self.subparsers.add_parser('download', help='Download images from Google Storage')
        #group.add_argument('--username', help='USGS Eros account Username (only works if the account has' +
        #                           ' special inventory access). Username and password as a fallback if the image' +
        #                           'is not found on AWS S3 or Google Storage')
        #group.add_argument('--password', help='USGS Eros username, used as a fallback')
        #group.add_argument('--force-unzip', help='Force unzip tar file', action='store_true')
        #group.add_argument('--force-unzip', help='Force unzip tar file', action='store_true')
        return group

    def add_process(self, products={}):
        """ Add processing options """
        parser = self.subparsers.add_parser('process', help='Process data into products')
        group = parser.add_argument_group('process options')

        group.add_argument('-q', '--query', help='Filename to a saved query')

        # this would be the data specific util path, which should be from a cfg file  ~/.sat-utils
        group.add_argument('-d', '--dest', help='Destination path (defaults to sat-util process path)', default=None)

        # products
        for p in products:
            # TODO - determine if product accepts arguments
            group.add_argument('--%s' % p, help=products[p].description)

        return group
