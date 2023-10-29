def sample_func(param1, param2, param3):
    print(f"{param1}, {param2}, {param3}")


def sample_func2(param1, param2=2, param3=3):
    print(f"{param1}, {param2}, {param3}")


def func_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


def sample_func3(param1, param2, *args):
    print(f"{param1=}")
    print(f"{param2=}")
    print(f"{args=}")


def sample_func4(name, **kwargs):
    print(f"{name=}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def sample_func5(param1, *args, default_arg=0, **kwargs):
    print(f"{param1=}")
    print(f"{args=}")
    print(f"{default_arg=}")
    print(f"{kwargs=}")


def sample_func6(param1, *, keyward1):
    print(f"{param1}, {keyward1}")


def add(x, y, /):
    return x + y


if __name__ == "__main__":
    # キーワード引数
    sample_func(param3=3, param2=2, param1=1)

    # 位置引数とキーワード引数の混在
    sample_func(1, param3=3, param2=2)

    # デフォルト値付き引数
    sample_func2(1)
    sample_func2(1, param2=20, param3=30)

    # 可変長位置引数
    num = [1, 2, 3, 4, 5]
    print(func_sum(*num))
    num2 = (1, 2, 3, 4, 5)
    print(func_sum(*num2))
    sample_func3(1, 2, 3, 4, 5, 6)

    # 可変長キーワード引数
    sample_func4("baba", age=26, email="baba@example.com")
    user_dict = {"first_name": "baba", "email": "baba@example.com"}
    sample_func4("test", **user_dict)

    # 混合
    sample_func5(1, 2, 3, default_arg=100, keyward1="keyward1", keyward2="keyward2")

    # キーワード専用引数
    sample_func6(1, keyward1=True)

    # 位置専用引数
    print(add(1, 4))
