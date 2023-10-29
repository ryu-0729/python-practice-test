import pprint
import sys


def print_hello():
    print("Hello")


sys.breakpointhook = print_hello


def main():
    print(sys.argv)
    pprint.pprint(sys.path)

    # sys.exit("プログラムを終了します。")

    sys.stdout.write("standard output message\n")
    sys.stderr.write("standard error message\n")
    sys.stdin.read()
    print(sys.version_info)
    breakpoint()

    try:
        sys.exit("sys.exit()")
    finally:
        print("finally")


if __name__ == "__main__":
    print("start")
    main()
    print("end")
