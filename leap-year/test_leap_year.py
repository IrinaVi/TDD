import unittest
from leap_year import leap_year

class TestStringMethods(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(leap_year(2000))

if __name__ == '__main__':
    unittest.main()