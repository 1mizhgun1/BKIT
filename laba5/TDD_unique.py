from functions.unique import Unique
import unittest as ut

class TestUnique(ut.TestCase):
    def setUp(self):
        self.symbols = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        self.numbers = [1, 2, 2, 1, 1, 3, 2, 3, 5, 4, 1]
        self.answer_1 = [1, 2, 3, 4, 5]
        self.answer_2 = ['a', 'A', 'b', 'B']
        self.answer_3 = ['a', 'b']

    def test_1(self):
        self.assertEqual(set(Unique(self.numbers)), set(self.answer_1))

    def test_2(self):
        self.assertEqual(set(Unique(self.symbols)), set(self.answer_2))

    def test_3(self):
        self.assertEqual(set(Unique(self.symbols, ignore_case=True)), set(self.answer_3))

if __name__ == '__main__':
    ut.main()
