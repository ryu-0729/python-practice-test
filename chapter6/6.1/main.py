import string
from uuid import uuid4


class Profile:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


def main():
    print("こんにちは\nいいお天気ですね。")
    print(r"こんにちは\nいいお天気ですね。")
    # TODO: blackのフォーマットで複数行に分けれない。。
    print(("1行が長い文字列リテラルを" "扱いたい場合は" "このように複数行に分ける" "テストテストテスト" "テストテスト"))

    value = uuid4()
    print(value)
    print(str(value))

    profile = Profile(first_name="baba", last_name="ryudai")
    print(str(profile))

    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.ascii_letters)
    print(string.digits)

    text = "Python"
    print("P" in text)
    print("p" in text)


if __name__ == "__main__":
    main()
