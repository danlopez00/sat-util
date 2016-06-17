import unittest
from satutil.parser import SatParser


class TestParser(unittest.TestCase):
    """ Test sat-util generic parser class """

    def parse(self, args=''):
        parser = SatParser()
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
