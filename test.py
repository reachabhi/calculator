import cal_functions
import unittest


class TestSum(unittest.TestCase):

    def test_Sum(self):
        r = cal_functions.add(12, 30)
        print(r)
        self.assertEqual(r, 402)