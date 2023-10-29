import argparse


def main():
    parser = argparse.ArgumentParser(description="Example command")
    parser.add_argument(
        "-s",
        "--string",
        type=str,
        help="string to display",
        required=True,
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        help="number of times repeatedly display the string",
        default=2,
    )
    parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType("r"),
        required=True,
    )
    args = parser.parse_args()
    print(args.string * args.num)
    print(args.file.read())


if __name__ == "__main__":
    main()
