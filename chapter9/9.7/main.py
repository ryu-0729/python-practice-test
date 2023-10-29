import copy


def main():
    value = ["a", "b", "c", "d"]
    val_cp = copy.copy(value)
    print(val_cp)
    val_cp[1] = "e"
    print(value)
    print(val_cp)
    value = [[0, 1], [2, 3], [4, 5]]
    val_cp = copy.copy(value)
    print(val_cp)
    val_cp[0][1] = 8
    print(val_cp)
    print(value)

    value2 = [[0, 1], [2, 3], [4, 5]]
    val_cp2 = copy.deepcopy(value2)
    print(val_cp2)
    val_cp2[0][1] = 8
    print(val_cp2)
    print(value2)


if __name__ == "__main__":
    main()
