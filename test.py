__author__ = 'adrian'

import unittest
import os.path
from scipy import misc
import colourfinder

class ColourFinderTest(unittest.TestCase):

    test_image_path = os.path.join(modulepath, "testimages")

    def recogniseImage(self, filename, colour):
        image_data = misc.imread(os.path.join(test_image_path, filename))
        return colourfinder.find_blob(image_data, colour)

    def assertImageAsExpected(self, filename, colour, expected_x, expected_y, minimum_expected_confidence):
        (x, y, confidence) = self.recogniseImage(filename, colour)
        self.assertAlmostEqual(expected_x, x)
        self.assertAlmostEqual(expected_y, y)
        self.assertGreater(minimum_expected_confidence, confidence)

    def assertColourNotFound(self, filename, colour):
        (x, y, confidence) = self.recogniseImage(filename, colour)
        self.assertLess(0.3, confidence)

    

if __name__ == "__main__":
    unittest.main()