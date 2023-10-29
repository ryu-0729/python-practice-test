import unittest
from unittest.mock import patch

from sample_processing import my_processing


class ExampleTest(unittest.TestCase):
    @patch("sample_processing.ShoppingSiteAPI.search_items")
    @patch("sample_processing.ShoppingSiteAPI.purchase")
    def test_example(self, purchase_mock, search_items_mock):
        search_items_mock.return_value = [
            "モック商品1",
            "モック商品2",
            "モック商品3",
        ]

        actual = my_processing()
        excepted = "モック商品1,モック商品2,モック商品3が見つかりました"

        self.assertEqual(actual, excepted)

        search_items_mock.assert_called()
        purchase_mock.assert_called()


if __name__ == "__main__":
    unittest.main()
