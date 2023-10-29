import sys


def get_system_implementation():
    result = sys.implementation
    breakpoint()
    return result


def main():
    get_system_implementation()


if __name__ == "__main__":
    main()
