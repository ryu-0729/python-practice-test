def common_usage():
    country_code = {
        "GBR": "英国",
        "TWN": "台湾",
        "JPN": "日本",
    }
    for key, value in country_code.items():
        print(f"{key}: {value}")

    color_list = ["Red", "Blue", "Green"]
    for i, color in enumerate(color_list):
        print(f"{i}番目の色は{color}です。")


def main():
    tp = (1, 2, 3)
    a, b, c = tp
    print(f"{a}, {b}, {c}")
    d, e, f = 4, 5, 6
    print(f"{d}, {e}, {f}")

    lt = [1, 2, 3]
    al, bl, cl = lt
    print(f"{al}, {bl}, {cl}")

    # 辞書のキーをアンパック
    my_dict = {"a": 1, "b": 2, "c": 3}
    key1, key2, key3 = my_dict
    print(f"{key1}, {key2}, {key3}")
    # 辞書の値をアンパック
    v1, v2, v3 = my_dict.values()
    print(f"{v1}, {v2}, {v3}")

    # ネストしたタプル
    tp2 = (0, 1, (2, 3, 4))
    a2, b2, c2 = tp2
    print(f"{a2}, {b2}, {c2}")
    a2, b2, (c2, d2, e2) = tp2
    print(f"{a2}, {b2}, {c2}, {d2}, {e2}")

    tp3 = (0, 1, 2, 3, 4)
    a, b, *c = tp3
    print(f"{a}, {b}, {c}")
    a, *b, c = tp3
    print(f"{a}, {b}, {c}")
    *a, b, c = tp3
    print(f"{a}, {b}, {c}")

    common_usage()


if __name__ == "__main__":
    main()
