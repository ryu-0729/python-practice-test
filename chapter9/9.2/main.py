import random
from collections import Counter, OrderedDict, defaultdict, namedtuple


def value():
    return "default-value"


def main():
    c = Counter("supercalifragilisticexpialidocious")
    print(c)
    li = ["spam"] * 100 + ["ham"] * 90 + ["egg"] * 110
    print(li)
    print(len(li))
    random.shuffle(li)
    print(li)
    print(Counter(li))
    c = Counter()
    print(c)
    for num in [1, 3, 2, 1, 2, 2, 1]:
        c[num] += 1
    print(c)
    print(c[5])
    print(1 in c)
    print(5 in c)
    c = Counter(a=4, b=1, c=-2, d=2)
    print(c)
    print(list(c.elements()))
    print(c.most_common(2))
    c2 = Counter(a=1, b=3, e=1)
    c.subtract(c2)
    print(c)
    c.update(c2)
    print(c)
    c1 = Counter(a=2, b=1)
    c2 = Counter(a=1, b=3)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 & c2)
    print(c1 | c2)

    dd = defaultdict(value, spam=100)
    print(dd)
    print(dd["ham"])

    dd_int = defaultdict(int)
    print(dd_int["spam"])
    dd_int["spam"] += 1
    print(dd_int["spam"])
    dd_list = defaultdict(list)
    print(dd_list["spam"])
    dd_list["spam"].append("ham")
    print(dd_list["spam"])

    dataset = [
        ("IPA", "Punk"),
        ("Ale", "YONAYONA"),
        ("IPA", "Stone"),
        ("Ale", "Sierra Nevada"),
    ]
    d = defaultdict(list)
    for category, name in dataset:
        d[category].append(name)
    print(list(d.items()))

    d = OrderedDict(one=1, two=2, three=3)
    print(d)
    d.move_to_end("two")
    print(d)
    d.move_to_end("two", last=False)
    print(d)
    print(d.popitem())
    print(d.popitem(last=False))

    order_dict = OrderedDict(one=1, two=2, three=3)
    for key, item in order_dict.items():
        print(f"{key=}: {item=}")

    Pet = namedtuple("Pet", "animal, name, age")
    seven = Pet("fettet", "セブン", 3)
    print(seven)
    print(seven.age)
    print(seven[1])
    animal, name, age = seven
    print(animal, name, age)


if __name__ == "__main__":
    main()
