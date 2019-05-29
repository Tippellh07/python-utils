"""Example test case."""

# standard library imports
import unittest


# =============================================================================#
# public classes


class ExampleTestCase(unittest.TestCase):
    """Example test case class taking an argument"""
    def __init__(self, testname: str, example_arg: str):
        super(ExampleTestCase, self).__init__(testname)
        self.example_arg = example_arg

    def test_example(self):
        self.assertTrue(True)
