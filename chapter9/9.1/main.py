from datetime import date
from operator import attrgetter, itemgetter


def main():
    print(sorted((5, 4, 3, 2, 1, 0)))
    print(type(sorted((5, 4, 3, 2, 1, 0))))

    print(sorted({"c": 3, "b": 2, "a": 1}))
    print(sorted({"c": 3, "b": 2, "a": 1}.items()))

    print(sorted({3, 3, 5, 5, 4, 4}))
    print(sorted("初めてのPython"))

    reversed_list = [1, 2, 3, 4, 5]
    print(reversed(reversed_list))
    print(list(reversed(reversed_list)))
    print(reversed_list)
    print(list(reversed((0, 1, 2, 3, 4, 5))))
    print(list(reversed("初めてのPython")))

    seq_str = ["B", "D", "a", "c"]
    print(sorted(seq_str))
    print(sorted(seq_str, key=str.lower))

    data = [(1, 40, 200), (3, 10, 100), (2, 20, 300), (1, 30, 300)]
    print(sorted(data))
    print(sorted(data, key=itemgetter(2)))
    print(sorted(data, key=itemgetter(2, 0)))

    dic = {"a": 2, "c": 1, "b": 3}
    print(sorted(dic.items(), key=itemgetter(1)))

    users = [
        {"name": "terada", "age": 35},
        {"name": "suzuki", "age": 25},
        {"name": "sugita", "age": 38},
    ]
    print(sorted(users, key=itemgetter("age")))

    dates = [
        date(1989, 1, 4),
        date(1970, 11, 28),
        date(1984, 3, 4),
    ]
    print(sorted(dates, key=attrgetter("month", "day")))


if __name__ == "__main__":
    main()
