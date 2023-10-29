import unicodedata


def main():
    print(unicodedata.lookup("Latin Small Letter a"))
    print(unicodedata.lookup("BEER MUG"))

    chr_list = ["A", "a", "1", "あ", "🍣", "○"]
    for chr in chr_list:
        print(unicodedata.name(chr))

    print(unicodedata.normalize("NFKC", "ｱアA A！!＠@"))

    nfkc = unicodedata.normalize("NFKC", "ガ")
    nfkd = unicodedata.normalize("NFKD", "ガ")
    print(nfkc, nfkd)


if __name__ == "__main__":
    main()
