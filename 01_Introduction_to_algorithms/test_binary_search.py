from unittest import TestCase, main
from binary_search import binary_search


class TestBinarySearch(TestCase):

    def test_target_at_beginning(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_target_at_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_target_in_middle(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_duplicate_values(self):
        self.assertEqual(binary_search([1, 2, 2, 3, 4, 5], 2), 2)

    def test_large_list(self):
        self.assertEqual(binary_search(list(range(10000)), 9999), 9999)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_target_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_negative_values(self):
        self.assertEqual(binary_search([-3, -2, -1, 0, 1, 2, 3], -1), 2)

    def test_float_values(self):
        self.assertEqual(binary_search([1.5, 2.5, 3.5, 4.5], 3.5), 2)


if __name__ == '__main__':
    main()
