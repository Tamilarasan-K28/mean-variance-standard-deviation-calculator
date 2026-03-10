import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):

    def test_calculate(self):
        result = calculate([0,1,2,3,4,5,6,7,8])
        self.assertEqual(result['mean'][2],4.0)

if __name__ == "__main__":
    unittest.main()