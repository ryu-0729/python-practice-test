import tempfile
from pathlib import Path


def main():
    with tempfile.TemporaryFile() as tmpf:
        print(tmpf.write(b"test test test\n"))
        print(tmpf.seek(0))
        print(tmpf.read())

    with tempfile.NamedTemporaryFile() as ntmpf:
        print(ntmpf.name)
        p = Path(ntmpf.name)
        print(p.exists())

    with tempfile.TemporaryDirectory() as tmpdirname:
        print(tmpdirname)
        p = Path(tmpdirname)
        print(p.exists())
        p2 = p / "hoge.txt"
        p2.touch()
        print(p2.exists())


if __name__ == "__main__":
    main()
