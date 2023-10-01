import unittest
import pytest

class TestSimpleTestScripts(unittest.TestCase):
    """Class for testing iterating stocks for analysis"""
    def __init__(self):
        self.try_out()

    def test_try_out(self):
        x = 4
        y = 5
        z = x + y
        assert z == 9
        print('this is a tryout')