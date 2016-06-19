#!/usr/bin/env python

from .parser import SatParser
from .version import __version__
from satprocess.scene import Scene


'''
    This is a generic command line program for processing geospatial raster data.
    Use this as a template in data-specific sat-util based utilities.
'''


def main():
    parser = SatParser(title='sat-util')
    # no sarch or download defined for "nosensor"
    parser.add_process()
    args = parser.parse_args()

    # currently only option
    if args.command == 'process':
        # read scene from directory
        # path in place of scene id for now
        for id in args.ids:
            scene = Scene.create_from_directory(args.ids[0])
            # process products
            for p in scene.available_products():
                # check if product is requested
                if args[p]:
                    print 'Product requestd'
                else:
                    print 'Product not requested'
