import unittest


class TearDownAndTearDownClassTest(unittest.TestCase):
    def tearDown(self):
        print("tearDown実行")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass実行")

    def test_example1(self):
        print("test_example1実行")

    def test_example2(self):
        print("test_example2実行")


if __name__ == "__main__":
    unittest.main()
