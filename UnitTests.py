import unittest
from lib import *

class GrayCodeTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Gray2bin(0b1101), 0b1001)
        self.assertEqual(bin2Gray(0b1001), 0b1101)
        self.assertEqual(Gray2bin(0b1110), 0b1011)
        self.assertEqual(bin2Gray(0b1011), 0b1110)
        self.assertEqual(Gray2bin(0b10000000), 0b11111111)
        self.assertEqual(bin2Gray(0b11111111), 0b10000000)
        self.assertEqual(Gray2bin(0b11111111), 0b10101010)
        self.assertEqual(bin2Gray(0b10101010), 0b11111111)

class GriewankTestCase(unittest.TestCase):
    def test_something(self):
        from math import pi
        self.assertEqual(Griewank([0]), 0)
        self.assertAlmostEqual(Griewank([pi]), 2 + pi * pi / 4000)
        self.assertAlmostEqual(Griewank([pi / 2, 0]), 1 + pi * pi / 16000)

class GetChromosomeIndexTestCase(unittest.TestCase):
    def test_something(self):
        a = [0.1, 0.25, 0.5, 0.55, 0.65, 0.81, 0.93, 1]
        self.assertEqual(getChromIdx(a, 0.5), 2)
        self.assertEqual(getChromIdx(a, 0.75), 5)
        self.assertEqual(getChromIdx(a, 0), 0)
        self.assertEqual(getChromIdx(a, 1), len(a) - 1)

if __name__ == '__main__':
    unittest.main()
