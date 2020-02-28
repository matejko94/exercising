import unittest
from unittest.mock import patch
from find_subsequence import *


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        import pathlib
        print(pathlib.Path().absolute())

        file = os.path.join(os.path.dirname(__file__), 'data/input_1.txt')
        contents = open(file).read()
        self.sequence1 = [int(x) for x in contents.strip().split(" ")]

        file = os.path.join(os.path.dirname(__file__), 'data/input_2.txt')
        contents = open(file).read()
        self.sequence2 = [int(x) for x in contents.strip().split(" ")]

        file = os.path.join(os.path.dirname(__file__), 'data/input_3.txt')
        contents = open(file).read()
        self.sequence3 = [int(x) for x in contents.strip().split(" ")]

    def test_subsequance_1_values(self):
        result =find_max_sum_subsiquence(self.sequence1, 9, Type.values)
        self.assertEqual(result, 6)

    def test_subsequance_1_differences(self):
        result =find_max_sum_subsiquence(self.sequence1, 4, Type.differences)
        self.assertEqual(result, 16)

    def test_subsequance_2_values(self):
        result =find_max_sum_subsiquence(self.sequence2, 10, Type.values)
        self.assertEqual(result, 27)

    def test_subsequance_2_differences(self):
        result =find_max_sum_subsiquence(self.sequence2, 5, Type.differences)
        self.assertEqual(result, 58)

    def test_subsequance_3_values(self):
        result =find_max_sum_subsiquence(self.sequence3, 30, Type.values)
        self.assertEqual(result, 44)

    def test_subsequance_3_differences(self):
        result =find_max_sum_subsiquence(self.sequence3, 10, Type.differences)
        self.assertEqual(result, 40)

    def test_parse_args(self):
        testargs = ["prog", 'data/input_1.txt', "5", "differences"]
        with patch.object(sys, 'argv', testargs):
            sequence, n, type = parse_attributes()
            self.assertEqual(len(sequence), 9)
            self.assertEqual(n, 5)
            self.assertEqual(type, Type.differences)
if __name__ == '__main__':
    unittest.main()