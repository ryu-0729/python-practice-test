from typing import Literal, Optional, TypedDict, Union

FILE_TYPE = Literal["csv", "json", "xml"]


def access_file(file: str, file_type: FILE_TYPE):
    pass


def five_year_later_students(age: int = 7) -> int:
    return age + 5


def say_hello(name: str) -> None:
    print(f"こんにちは {name}")


def address_code(number: Union[int, str]) -> int:
    return number


class BoodDict(TypedDict):
    name: str
    author: str
    price: int


def main():
    print(five_year_later_students())
    print(five_year_later_students(9))

    say_hello("baba")

    hobby: list[str] = ["ゲーム", "漫画"]
    print(hobby)
    favorite: dict[str, str] = {"study": "プログラミング", "movie": "モンティ・パイソン"}
    print(favorite)
    like_num: set[str] = {1, 3, 5}
    print(like_num)

    hobby2: tuple[str, str] = ("ゲーム", "漫画")
    print(hobby2)

    hobby_name: tuple[str, ...] = ("ゲーム", "漫画", "映画", "ガンプラ")
    print(hobby_name)

    your_code: int = address_code(1000001)
    print(your_code)
    my_code: int = address_code("1000001")
    print(my_code)

    price: Optional[int]
    price = 100
    print(price)

    price: int | None
    price = None
    print(price)

    print(access_file(".test", "csv"))

    fav_book: BoodDict = {
        "name": "スタートブック",
        "author": "shingo",
        "price": 2750,
    }
    print(fav_book)


if __name__ == "__main__":
    main()
