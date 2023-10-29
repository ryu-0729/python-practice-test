class MyObject:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"MyObject: {self.name}"


def main():
    obj = MyObject("test")
    print(obj)


if __name__ == "__main__":
    main()
