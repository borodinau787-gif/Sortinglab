import unittest
from main import bubble_sort, binary_insertion_sort

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.data = [64, 34, 25, 12, 22, 11, 90]
        self.expected = [11, 12, 22, 25, 34, 64, 90]

    def test_bubble(self):
        self.assertEqual(bubble_sort(self.data.copy()), self.expected)

    def test_binary(self):
        self.assertEqual(binary_insertion_sort(self.data.copy()), self.expected)

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(binary_insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(binary_insertion_sort([1]), [1])

    def test_negative_numbers(self):
        arr = [3, -1, 0, -5, 2]
        exp = [-5, -1, 0, 2, 3]
        self.assertEqual(bubble_sort(arr.copy()), exp)
        self.assertEqual(binary_insertion_sort(arr.copy()), exp)

if __name__ == "__main__":
    unittest.main()