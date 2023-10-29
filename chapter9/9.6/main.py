import itertools


def is_odd(num):
    return num % 2 == 1


def main():
    it = itertools.chain(["A", "B"], "ab", range(3))
    for el in it:
        print(el)

    for val, group in itertools.groupby("aaaabbbcccddaabbcc"):
        print(f"{val}: {list(group)}")

    sorted_text = "".join(sorted("aaaabbbcccddaabbcc"))
    print(sorted_text)
    for val, group in itertools.groupby(sorted_text):
        print(f"{val}: {list(group)}")

    numbers = [10, 20, 31, 11, 3, 4]
    for val, group in itertools.groupby(numbers, is_odd):
        print(f"{val}: {list(group)}")

    li = list(range(10))
    islice_object = itertools.islice(li, 5)
    print(islice_object)
    print(list(islice_object))

    it1 = (1, 2, 3, 4, 5)
    it2 = ["abc", "ABC", "123"]
    # fillvalueのデフォルトはNone
    for v in itertools.zip_longest(it1, it2, fillvalue="-"):
        print(v)

    product_list = list(itertools.product("abc", [1, 2, 3]))
    print(product_list)
    product_list = [r[0] + r[1] for r in itertools.product("ABC", repeat=2)]
    print(product_list)
    permute_list = list(itertools.permutations("ABC"))
    print(permute_list)
    result = itertools.permutations("ABCD", 2)
    result_list = [r[0] + r[1] for r in result]
    print(result_list)
    comb_list = list(itertools.combinations("ABC", 2))
    print(comb_list)
    comb_list = itertools.combinations("ABCDEF", 3)
    print([r[0] + r[1] + r[2] for r in comb_list])
    print(list(itertools.combinations_with_replacement("ABC", 2)))


if __name__ == "__main__":
    main()
