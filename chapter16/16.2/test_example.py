import unittest

from example import add


class AddTest(unittest.TestCase):
    def test_get_the_sum_of_integers(self):
        """add()関数のテストコード"""
        actual = add(1, 3)
        excepted = 4
        self.assertEqual(actual, excepted)

    def test_assert_is_not_none(self):
        """assertInNotNoneメソッドの使用例"""
        actual = add(1, 2)
        self.assertIsNotNone(actual)


if __name__ == "__main__":
    unittest.main()
