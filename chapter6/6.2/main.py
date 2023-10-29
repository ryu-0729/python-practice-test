import math
from datetime import datetime


def test_func():
    print("test")
    return "test"


def main():
    print(f"{test_func()=}")

    text = "text align"
    print(f"|{text:<30}|")
    print(f"|{text:>30}|")
    print(f"|{text:^30}|")
    print(f"|{text:-^30}|")

    number = 1000
    print(f"{number:b} {number:o} {number:d} {number:x} {number:X}")

    print(f"{math.pi} {math.pi:f}")

    number = 0.045
    print(f"{number:%}")

    number = 10000000
    print(f"{number:,}")

    print(f"{math.pi:3.2f}")
    print(f"{math.pi:>5.2f}")

    now = datetime.now()
    print(f"{now:%Y-%m-%d}")

    print("Hello %s!" % "Taro")

    print("1 + 3 = %d" % 4)

    a = 2
    b = 3
    print("%d * %d = %d" % (a, b, a * b))

    value_dict = {"name": "baba", "language": "Python"}
    print("%(name)s likes %(language)s" % value_dict)


if __name__ == "__main__":
    main()
