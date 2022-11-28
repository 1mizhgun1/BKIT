from functions.sort import my_sort_with_lambda, my_sort_without_lambda
import unittest as ut

class TestSort(ut.TestCase):
    def setUp(self):
        self.data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
        self.answer = [0, 1, -1, 4, -4, -30, 30, 100, -100, 123]

    def test_1(self):
        self.assertEqual(my_sort_with_lambda(self.data), self.answer)

    def test_2(self):
        self.assertEqual(my_sort_without_lambda(self.data), self.answer)

if __name__ == '__main__':
    ut.main()
