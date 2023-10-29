import io


def main():
    stream = io.StringIO("this is test \n")
    print(stream.read(10))
    print(stream.tell())
    print(stream.seek(0, io.SEEK_END))
    print(stream.write("test"))
    print(stream.getvalue())
    stream.close()

    with io.StringIO() as stream:
        stream.write("test")

    the_zen_of_python = """The Zon of Python, by Tim Peters
    Beautiful is better than ugly
    Explicit is better than implicit
    """
    stream = io.StringIO(the_zen_of_python)
    for line in stream:
        print(line)

    stream = io.BytesIO(b"abcdefg")
    print(stream.read(5))
    print(stream.tell())
    print(stream.seek(0, io.SEEK_END))
    print(stream.write(b"test"))
    print(stream.getvalue())
    stream.close()

    with io.BytesIO() as bstream:
        bstream.write(b"test")

    stream = io.BytesIO(b"abcdefg")
    view = stream.getbuffer()
    view[2:4] = b"56"
    print(stream.getvalue())


if __name__ == "__main__":
    main()
