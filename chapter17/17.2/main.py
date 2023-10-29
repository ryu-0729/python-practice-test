import timeit


def foo():
    pass


def main():
    print(timeit.timeit("'test' in 'This is a test'"))
    print(timeit.repeat("'test' in 'This is a test'"))

    t = timeit.Timer("char in text", setup="text = 'This is a test.'; char = 'test'")
    print(t.timeit())

    # ↓インデントエラーになる原因不明
    # s = """try:
    #     "This is a test".__bool__
    # except AttributeError:
    #     pass"""
    # print(timeit.timeit(stmt=s))

    print(timeit.timeit("foo()", globals=globals()))


if __name__ == "__main__":
    main()
