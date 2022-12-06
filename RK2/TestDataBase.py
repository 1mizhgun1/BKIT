import unittest as ut
from main import *

class TestDB(ut.TestCase):
    def setUp(self):
        self.langs = [
            Language(1, "Python"),  Language(10, "Python v0"),
            Language(2, "C++"),     Language(20, "C++ v0"),
        ]

        self.libs = [
            Library(11, "random", 30, 1),
            Library(12, "math", 50, 1),
            Library(21, "vector", 40, 2)
        ]

        self.links = [
            Link(11, 1),    Link(11, 10),
            Link(12, 1),    Link(12, 10),
            Link(21, 2),    Link(21, 20)
        ]

        self.one_to_many, self.many_to_many = get_db_links(self.langs, self.libs, self.links)

        self.ans_1 = {'C++' : ['vector']}
        self.ans_2 = {'C++' : 40, 'Python' : 50}
        self.ans_3 = [('C++', 'vector'), ('C++ v0', 'vector'), ('Python', 'random'), ('Python', 'math'), ('Python v0', 'random'), ('Python v0', 'math')]

    def test_task_1(self):
        self.assertEqual(task_1(self.one_to_many, 'C'), self.ans_1)

    def test_task_2(self):
        self.assertEqual(task_2(self.one_to_many), self.ans_2)

    def test_task_3(self):
        self.assertEqual(task_3(self.many_to_many), self.ans_3)

if __name__ == '__main__':
    ut.main()