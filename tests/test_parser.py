import unittest
from satutil.parser import SatParser


class TestParser(unittest.TestCase):
    """ Test sat-util generic parser class """

    def parse(self, args='', search=False, download=False, process=False):
        parser = SatParser()
        if search:
            parser.add_search()
        if download:
            parser.add_download()
        if process:
            parser.add_process()
        return parser.parse_args(args.split())

    def test_basic_noargs(self):
        """ Casic parser with no arguments """
        args = self.parse()
        self.assertTrue(args.ids is None)
        self.assertTrue(args.verbose == 1)

    def test_basic_ids(self):
        """ Casic parser with ids """
        args = self.parse('--ids 0')
        self.assertEqual(args.ids, ['0'])

    def test_basic_verbose(self):
        """ Basic parser with varying verbosity level """
        for v in range(0, 4):
            args = self.parse('-v %s' % v)
            self.assertEqual(args.verbose, v)

    def test_subcommands_noargs(self):
        """ Parser with search, download, process subcommands and no args """
        for arg in ['search', 'download', 'process']:
            args = self.parse('', search=True, download=True, process=True)
            self.assertEqual(args.cmd, None)
            args = self.parse(arg, search=True, download=True, process=True)
            self.assertEqual(args.cmd, arg)

    def test_search(self):
        """ Search parser """
        args = self.parse('search', search=True)
        self.assertEqual(args.cmd, 'search')

    def test_download(self):
        """ Download parser """
        args = self.parse('download', download=True)
        self.assertEqual(args.cmd, 'download')

    def test_process(self):
        """ Download parser """
        args = self.parse('process', process=True)
        self.assertEqual(args.cmd, 'process')
