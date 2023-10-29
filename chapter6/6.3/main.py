import re


def main():
    print(re.search("a.c", "abcd"))
    print(re.search(".c", "abcde"))
    print(re.match(".c", "abcde"))

    print(re.search("\w", "あいうえおABCD", flags=re.A))
    print(re.search("[abc]+", "ABC"))
    print(re.search("[abc]+", "ABC", flags=re.I))
    print(re.search("a.c", "A\nC", flags=re.I | re.S))

    pattern = re.compile("a.c")
    print(pattern.search("abcde"))

    regex = re.compile("[a-n]+")
    print(type(regex))
    print(regex.search("python"))
    print(regex.match("python"))
    print(regex.fullmatch("python"))
    print(regex.fullmatch("eggs"))
    print(regex.fullmatch("egg"))

    regex2 = re.compile("[-+()]")
    print(regex2.split("080-1234-5678"))
    print(regex2.split("(080)1234-5678"))
    print(regex2.sub("", "+080-1234-5678"))

    regex3 = re.compile("\d+")
    print(regex3.findall("080-1234-5678"))
    i = regex3.finditer("+080-1234-5678")
    print(type(i))
    for m in i:
        print(m)

    m = re.match(r"(\d+)-(\d+)-(\d+)", "080-1234-5678")
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(1, 2, 3))
    print(m[0])

    m2 = re.match(r"(?P<last>\w+) (?P<first>\w+)", "馬場 龍大")
    print(m2.group(0))
    print(m2.group("last"))
    print(m2.group("first"))
    print(m2["first"])

    print(m2.groups())
    print(m2.groupdict())
    print(m2.expand(r"名前: \1\2"))
    print(m2.expand(r"名字(\g<last>) 名前(\g<first>)"))


if __name__ == "__main__":
    main()
