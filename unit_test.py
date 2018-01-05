# coding=utf-8
import unittest


class MyTest(unittest.TestCase):

    # 必须以test开头
    def test_simply(self):
        self.assertEquals(1 + 1, 2)

    def test_failure(self):
        self.assertEquals(1 + 1, 3)     


if __name__ == '__main__':
    unittest.main()
