import sys
import unittest as ut
from Padovan import Padovan

class TestPadovan(ut.TestCase):
    def setUp(self):
        self.answer_15 = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49]
        self.alt_15 = [1, 1, 1, 2, 2]
        self.answer_2 = [1, 1, 1]
        for i in range(5, 16):
            self.alt_15.append(self.alt_15[i - 1] + self.alt_15[i - 5])

    def test_Padovan_2(self):
        ''' P(n) = P(n - 2) + P(n - 3)  '''
        self.assertEqual(list(Padovan(2)), self.answer_2)

    def test_Padovan_15(self):
        ''' P(n) = P(n - 2) + P(n - 3)  '''
        self.assertEqual(list(Padovan(15)), self.answer_15)

    def test_alternative_recurrent_relations(self):
        ''' P(n) = P(n - 1) + P(n - 5)  '''
        self.assertEqual(list(Padovan(15)), self.alt_15)

    def test_lazy_calculations(self):
        self.assertEqual(sys.getsizeof(Padovan(10)), sys.getsizeof(Padovan(10000)))

if __name__ == '__main__':
    ut.main()