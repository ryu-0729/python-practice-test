from pathlib import Path, PurePath, PureWindowsPath


def main():
    print(Path())
    print(PurePath("spam.txt"))
    print(PurePath("spam", "ham", "eggs.txt"))
    print(PurePath("spam/ham", "eggs.txt"))

    p = Path("/user")
    print(p)
    print(p / "bin" / "python3")
    q = Path("hosts")
    print(p / q)

    p = PurePath("/spam/ham/eggs.tar.gz")
    print(p.parts)
    wp = PureWindowsPath("c:/Program Files/spam/ham.exe")
    print(wp.parts)
    print(p.root)
    print(wp.root)
    for parent in p.parents:
        print(parent)
    print(p.name)
    print(p.suffix)
    print(p.suffixes)
    print(p.stem)

    p1 = PurePath("/spam/ham/eggs.txt")
    p2 = PurePath("eggs.txt")
    print(p1.is_absolute())
    print(p2.is_absolute())
    print(p1.is_relative_to("/spam"))
    print(p1.is_relative_to("/ham"))
    print(p1.match("*.txt"))
    print(p1.with_name("hoge.txt"))
    print(p1.with_stem("fuga"))
    print(p1.with_suffix(".py"))

    print(Path.cwd())
    print(Path.home())
    p = Path("spam.txt")
    print(p.exists())
    print(p.stat().st_mode)
    p.chmod(0o600)
    print(p.stat().st_mode)
    print(p.is_file())
    with p.open(encoding="utf-8") as f:
        print(f.read())
    p.write_text("ハムハムハムハム", encoding="utf-8")
    print(p.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
