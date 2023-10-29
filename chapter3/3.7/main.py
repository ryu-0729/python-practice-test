import random
from functools import wraps

from retrying import retry


@retry(stop_max_attempt_number=2)
def my_func():
    if random.randint(0, 10) == 5:
        print("5です")
    else:
        print("raise ValuError")
        raise ValueError("5ではありません。")


def my_decorator(func):
    def wrap_function():
        func()
        print(f"function: {func.__name__} called")

    return wrap_function


def greeting():
    print("こんにちは")


@my_decorator
def greeting2():
    print("こんにちは2")


def my_decorator2(func):
    def wrap_function(val):
        """wrap_functionのドキュメント"""
        func(val)

    return wrap_function


@my_decorator2
def greeting3(name):
    """greeting3のドキュメント"""
    print(f"こんにちは、{name}")


def my_decorator3(func):
    @wraps(func)
    def wrap_function(val):
        """wrap_functionのドキュメント"""
        func(val)

    return wrap_function


@my_decorator3
def greeting4(name):
    """greeting4のドキュメント"""
    print(f"こんにちは、{name}")


def main():
    # my_func()
    greet = my_decorator(greeting)
    greet()

    greeting2()

    greeting3("baba")
    print(greeting3.__name__)
    print(greeting3.__doc__)

    greeting4("baba")
    print(greeting4.__name__)
    print(greeting4.__doc__)


if __name__ == "__main__":
    main()
