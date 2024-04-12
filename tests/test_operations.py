import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from operations import sub, sum


class TestOperations(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(1, 2), -1)


if __name__ == "__main__":
    unittest.main()
