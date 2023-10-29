from dataclasses import asdict, astuple, dataclass


@dataclass
class User:
    name: str
    age: int
    address: str


@dataclass(frozen=True)
class FrozonUser:
    name: str
    age: int
    address: str


@dataclass
class User2:
    name: str
    age: int
    address: str
    active: bool = False


def main():
    user = User("baba", 26, "miyagi")
    print(user)
    print(asdict(user))
    print(astuple(user))
    frozen_user = FrozonUser("馬場", 26, "sendai")
    print(frozen_user)
    # 変更不可
    # frozen_user.age = 27

    user2 = User2("rb", 39, "Tokyo")
    print(user2)


if __name__ == "__main__":
    main()
