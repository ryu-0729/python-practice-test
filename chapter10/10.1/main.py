import os


def main():
    print(os.environ["HOME"])
    print(os.getcwd())
    # os.chdir("../../chapter10/")
    # os.mkdir("10.2")
    # print(os.listdir("."))
    # os.rmdir("10.2")
    # print(os.urandom(10))


if __name__ == "__main__":
    main()
