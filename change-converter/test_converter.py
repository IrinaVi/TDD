import unittest
from converter import convert

class TestChangeConverter(unittest.TestCase):

    def test_notes(self):
        self.assertEqual(convert(50), ['£50'])

if __name__ == '__main__':
    unittest.main()