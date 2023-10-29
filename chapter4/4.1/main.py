class User:
    user_type = None

    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self) -> str:
        return f"<User id: {id(self)} name: {self.name}>"

    def __len__(self) -> int:
        return len(self.name)

    def increment_age(self):
        self.age += 1

    @property
    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ""


class User2:
    user_type = None

    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self) -> str:
        return f"<User id: {id(self)} name: {self.name}>"

    def __len__(self) -> int:
        return len(self.name)

    def __eq__(self, other: object) -> bool:
        return self.age == other.age

    def increment_age(self):
        self.age += 1


def main():
    user1 = User("馬場", 26, "test@email.com")
    user2 = User2("テスト", 25, "test@email.com")
    print(user1)
    print(len(user1))
    print(user1.name)
    print(user1.age)
    print(user1.address)

    print(user1 == user2)
    user2.increment_age()
    print(user1 == user2)

    user1.increment_age()
    print(user1.age)

    # print(user1.start_name())
    print(user1.start_name)


if __name__ == "__main__":
    main()
