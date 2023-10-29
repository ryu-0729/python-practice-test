"""
与えられた引数について、a / bを行う関数です。

>>> div(5, 2)
2.5
"""


def div(a, b):
    """
    答えは少数で返ってきます

    >>> [div(n, 2) for n in range(5)]
    [0.0, 0.5, 1.0, 1.5, 2.0]

    第二引数がゼロだった場合はゼロ除算エラーが発生します。

    >>> div(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """

    return a / b


def main():
    import doctest

    doctest.testmod()
    doctest.testfile("sample_doctest.txt")


if __name__ == "__main__":
    main()
