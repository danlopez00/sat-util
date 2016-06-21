import unittest
import click
from click.testing import CliRunner
from satutil.parser import cli


class TestParser(unittest.TestCase):
    """ Test sat-util generic parser class """

    def setUp(self):
    	self.runner = CliRunner()

    def test_basic_noargs(self):
    	result = self.runner.invoke(cli, 'blah')


