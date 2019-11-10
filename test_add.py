from unittest import TestCase
from demo1 import add

class TestAdd(TestCase):
    def test_add(self):
        self.assertEqual(add(3,5),8)
        #self.assertEqual('foo'.upper(),'FOO')
