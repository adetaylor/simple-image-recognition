__author__ = 'adrian'

import unittest
import os
from scipy import misc
import colourfinder

class ColourFinderTest(unittest.TestCase):

    test_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testimages")

    def recogniseImage(self, filename, colour):
        image_data = misc.imread(os.path.join(ColourFinderTest.test_image_path, filename))
        return colourfinder.find_blob(image_data, colour)

    def assertImageAsExpected(self, filename, colour, expected_x, expected_y, minimum_expected_confidence):
        (x, y, confidence) = self.recogniseImage(filename, colour)
        self.assertAlmostEqual(expected_x, x)
        self.assertAlmostEqual(expected_y, y)
        self.assertGreater(minimum_expected_confidence, confidence)

    def assertColourNotFound(self, filename, colour):
        (x, y, confidence) = self.recogniseImage(filename, colour)
        self.assertLess(0.3, confidence)

    def test_find_wattle(self):
        self.assertImageAsExpected("chicken.jpg", colourfinder.RED, 1850, 1320, 0.5)

if __name__ == "__main__":
    unittest.main()