def main():
    number_list = [i**2 for i in range(10)]
    print(number_list)

    number_list = [i**2 for i in range(10) if i % 2 == 0]
    print(number_list)

    drinks = ["coffee", "tea", "Espresso"]
    sizes = ["S", "M", "L"]

    menu = [(drink, size) for drink in drinks for size in sizes]
    print(menu)

    # 集合
    set_number = {i**2 % 10 for i in range(10)}
    print(set_number)

    # 辞書
    dict_number = {i: i**2 for i in range(10)}
    print(dict_number)

    # ジェネレータ
    gene = (i**2 for i in range(10))
    print(type(gene))
    print(gene)
    for num in gene:
        print(num)

    arr = [1.4, 2.0, 3.5, 2.25, 1.98]
    print(list(map(round, arr)))
    arr_list = [round(n) for n in arr]
    print(arr_list)

    print(list(map(round, filter(lambda n: n > 2, arr))))
    arr_filter = [round(n) for n in arr if n > 2]
    print(arr_filter)


if __name__ == "__main__":
    main()
