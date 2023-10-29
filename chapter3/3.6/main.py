import sys


def multiplier(values):
    for i in values:
        yield 2**i


def multiplier2():
    """無限に繰り返されるジェネレーター"""

    num = 1
    while True:
        yield num
        num *= 2


def multiples256(values):
    for i in values:
        if i % 256 == 0:
            yield i


def main():
    values = [0, 1, 2, 3, 4, 5]
    ret = multiplier(values)
    print(type(ret))

    for i in ret:
        print(i)

    # listに変換
    ret2 = list(multiplier(values))
    print(ret2)

    gen = multiplier2()
    print(gen)
    print(next(gen))
    print(next(gen))

    # メモリサイズ確認
    multiplier_list = [i**2 for i in range(1_000_001)]
    print(sys.getsizeof(multiplier_list))

    multiplier_gen = (i**2 for i in range(1_000_001))
    print(sys.getsizeof(multiplier_gen))
    print(next(multiplier_gen))
    print(next(multiplier_gen))
    print(next(multiplier_gen))

    multiplier_gen2 = (i**2 for i in range(1_000_001))
    print(len(list(multiplier_gen2)))

    values = [1512, 384, 512, 2304, 768, 864, 1512, 1792]
    m256 = list(multiples256(values))
    print(max(m256))
    print(min(m256))


if __name__ == "__main__":
    main()
