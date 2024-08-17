import pytest
import unittest

class TestClass(unittest.TestCase):
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        self.assertEqual(x, "hello", f"{x} does not equal hello")