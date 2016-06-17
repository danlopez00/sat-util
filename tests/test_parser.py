import unittest
from satutil.parser import SatParser

class TestParser(unittest.TestCase):
    """ Test sat-util generic parser class """

    def test_noargs(self):
        parser = SatParser()
        args = parser.parse_args('')
        #self.assertTrue(args.a == 1)
