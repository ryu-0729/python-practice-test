from concurrent.futures import ProcessPoolExecutor, as_completed
from time import time


def loop1():
    cnt = 0
    for i in range(100):
        cnt += 1

    print(f"loop1: {cnt=}")
    return cnt


def loop2():
    cnt = 0
    for i in range(100000):
        cnt += 1

    print(f"loop2: {cnt=}")
    return cnt


def main():
    start = time()

    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(loop2),
            executor.submit(loop1),
        ]
        for future in as_completed(futures):
            result = future.result()
            print(f"{result=}")

    print(f"{time() - start}")


if __name__ == "__main__":
    main()
