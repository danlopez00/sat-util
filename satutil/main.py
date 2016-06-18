from .parser import SatParser
from .version import __version__
#

'''
    This is a generic command line program for processing geospatial raster data.
    Use this as a template in data-specific sat-util based utilities.
'''


def main():
    #title = 'Sat-util CLI'

    parser = SatParser()
    args = parser.parse_args()
    
    print args

    #if args.subs == 'search':
    #    results = Search.query(**args)
    #elif args.subs == 'download':
    #    results = Search.query(**args)

    #if args.indir is not None:
        # read scene from directory
    #    scene = Scene.create_from_directory(args.indir)
        # 1 - collect product arguments
        # 2 - generate output filenames
        # 3 - call scene.process(products)
    #else:
    #    for sid in args.sceneids:
    #        fname = os.path.join(args.indir, sid)
    #        scene = Scene(fname)