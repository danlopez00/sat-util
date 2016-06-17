import unittest
from satutil.parser import SatParser

class TestParser(unittest.TestCase):
    """ Test sat-util generic parser class """

    def test_basic_noargs(self):
        parser = SatParser()
        with self.assertRaises(SystemExit):
            args = parser.parse_args('')
        #self.assertTrue(args.a == 1)
