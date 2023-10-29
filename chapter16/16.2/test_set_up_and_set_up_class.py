import unittest


class SetUpAndSetUpClassTest(unittest.TestCase):
    def setUp(self):
        print("setUp実行")

    @classmethod
    def setUpClass(cls):
        print("setUpClass実行")

    def test_example1(self):
        print("test_example1実行")

    def test_example2(self):
        print("test_example2実行")


if __name__ == "__main__":
    unittest.main()
