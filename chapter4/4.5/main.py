def func():
    """docstring"""
    return ""


def main():
    li = []
    print(id(li))
    li.append(1)
    print(id(li))

    print(isinstance(1, int))
    print(isinstance(1, str))

    print(isinstance([], (list, tuple)))
    print(isinstance("1.0", (int, float)))

    print(isinstance(True, int))
    print(isinstance(True, float))
    print(issubclass(bool, int))

    print(isinstance([], object))

    # print(help(func))
    print(dir("test"))  # オブジェクトが持つメソッドの確認


if __name__ == "__main__":
    main()
