import pytest
import unittest

class TestClass(unittest.TestCase):
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert self.assertEqual(x, "hello")