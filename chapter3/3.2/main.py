import contextlib
import traceback
from time import sleep, time


class MyOpenContextManager:
    """自作のコンテキストマネージャー"""

    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def __enter__(self):
        print("ファイルを開きます")
        self.file_obj = open(self.file_name, "r")
        return self.file_obj

    def __exit__(self, type, value, trback):
        print("ファイルを閉じます")
        self.file_obj.close()


@contextlib.contextmanager
def my_open_context_manager(file_name):
    file_obj = open(file_name, "r")
    try:
        print("ファイルを開きます")
        yield file_obj
    except Exception as e:
        print(f"{type(e)}")
        print(f"{e}")
        print(f"{list(traceback.TracebackException.from_exception(e).format())}")
        raise
    finally:
        file_obj.close()
        print("ファイルを閉じます")


@contextlib.contextmanager
def timed(func_name):
    start = time()
    try:
        yield
    finally:
        end = time()
        print(f"{func_name}: (total: {end - start})")


if __name__ == "__main__":
    with MyOpenContextManager("python.txt") as f:
        print(f.read())

    with my_open_context_manager("python.txt") as f:
        print(f.read())

    with timed("sleep processing"):
        sleep(2)
