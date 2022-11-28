from functions.field import field
import unittest as ut

class TestField(ut.TestCase):
    def setUp(self):
        self.goods = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]
        self.answer_1 = ['Ковер', 'Диван для отдыха']
        self.answer_2 = [
            {'title': 'Ковер', 'price': 2000},
            {'title': 'Диван для отдыха', 'price': 5300}
        ]

    def test_1(self):
        self.assertEqual(field(self.goods, 'title'), self.answer_1)

    def test_2(self):
        self.assertEqual(field(self.goods, 'title', 'price'), self.answer_2)

if __name__ == '__main__':
    ut.main()