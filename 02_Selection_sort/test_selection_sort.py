from unittest import TestCase, main
from selection_sort import selection_sort


class TestSelectionSort(TestCase):
    def test_random_array(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), sorted_arr)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), sorted_arr)

    def test_reversed_array(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), sorted_arr)

    def test_identical_elements_array(self):
        arr = [2, 2, 2, 2, 2]
        sorted_arr = [2, 2, 2, 2, 2]
        self.assertEqual(selection_sort(arr), sorted_arr)

    def test_empty_array(self):
        arr = []
        sorted_arr = []
        self.assertEqual(selection_sort(arr), sorted_arr)


if __name__ == '__main__':
    main()
