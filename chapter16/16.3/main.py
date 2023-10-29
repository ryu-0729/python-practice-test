from unittest.mock import MagicMock

from sample_processing import ShoppingSiteAPI


def main():
    api = ShoppingSiteAPI()
    api.search_items = MagicMock()
    print(api.search_items)
    api.search_items.return_value = [
        "モック商品1",
        "モック商品2",
        "モック商品3",
    ]
    print(api.search_items("商品"))
    api.search_items.side_effect = Exception("例外を設定します。")
    print(api.search_items("商品"))


if __name__ == "__main__":
    main()
