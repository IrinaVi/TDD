import unittest
from converter import converter

class TestConverter(unittest.TestCase):

    def test(self):
        self.assertEqual(converter([60]),[60])



if __name__ == '__main__':
    unittest.main()