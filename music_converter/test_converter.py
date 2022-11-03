import unittest
from converter import converter

class TestConverter(unittest.TestCase):

    def test(self):
        self.assertEqual(converter([60]),[60])
        self.assertEqual(converter([60, 100]), [60, 100])
        self.assertEqual(converter([30]),[40])
        self.assertEqual(converter([1500]), [1000])
        self.assertEqual(converter([10,2000,50,70,150]), [40,1000,50,70,150])

    def test_with_user_inputted_upper_lower_limits(self):
        self.assertEqual(converter([60,10,45,60,1500],5), [60,10,45,60,1000])



if __name__ == '__main__':
    unittest.main()