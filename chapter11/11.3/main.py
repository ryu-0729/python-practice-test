import shutil


def main():
    shutil.copyfile("a.txt", "b.txt")
    shutil.copy("a.txt", "c.txt")
    shutil.copy2("a.txt", "d.txt")
    shutil.copy("a.txt", "e/")

    # ignore = shutil.ignore_patterns("*.pyc", "*.swp")
    # shutil.copytree("./e/", "./d/", ignore=ignore)

    # shutil.rmtree("./d/")


if __name__ == "__main__":
    main()
