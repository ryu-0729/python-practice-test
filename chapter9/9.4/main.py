import enum


@enum.unique
class Nengo(enum.Enum):
    SHOWA = enum.auto()
    HEISEI = enum.auto()
    REIWA = enum.auto()


class Spam(enum.Enum):
    HAM = 1
    EGG = 2
    BECON = 2


class OtherSpam(enum.Enum):
    HAM = 1
    EGG = 2
    BECON = 2


def print_nengo(value: Nengo):
    print(value.name)
    print(value.value)


def main():
    print(Nengo.SHOWA)
    print(Nengo["HEISEI"])
    reiwa = Nengo.REIWA
    print(reiwa.name)
    print(reiwa.value)

    print(isinstance(Spam.HAM, Spam))
    print(Spam.EGG == Spam.BECON)

    print(Spam.HAM == OtherSpam.HAM)
    print(Spam.HAM == 1)

    print_nengo(Nengo.REIWA)


if __name__ == "__main__":
    main()
