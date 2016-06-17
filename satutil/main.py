from .parser import SatParser
from .version import __version__
from ssearch import Search

def main():
    title = 'Sat-util CLI'
    try:
        parser = SatParser(description=title)
        if args.subs == 'search':
            results = Search.query(**args)
        elif args.subs == 'download:'
            results = Search.query(**args)
