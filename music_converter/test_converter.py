import unittest
from converter import converter

class TestConverter(unittest.TestCase):

    def test(self):
        self.assertEqual(converter([60]),[60])
        self.assertEqual(converter([60, 100]), [60, 100])
        self.assertEqual(converter([30]),[40])
        self.assertEqual(converter([1500]), [1000])



if __name__ == '__main__':
    unittest.main()