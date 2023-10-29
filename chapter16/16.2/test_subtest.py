import unittest

from example import add


class AddTest(unittest.TestCase):
    def test_get_the_sum_of_two_integers(self):
        """2つの整数の合計値を取得できる"""
        examples = [
            [1, 2, 3],
            [1, 3, 4],
            [3, 3, 6],
        ]
        for i, example in enumerate(examples):
            a, b, expected = example
            with self.subTest(f"{a} + {b} = {expected}", idx=i):
                self.assertEqual(add(a, b), expected)


if __name__ == "__main__":
    unittest.main()
