import logging


def main():
    logformat = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig(
        filename="log/test.log",
        level=logging.DEBUG,
        format=logformat,
    )

    logging.debug("debug message")
    logging.warning("warning message")

    favorite_song = "bouldering"
    logging.error("I love %s", favorite_song)


if __name__ == "__main__":
    main()
