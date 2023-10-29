import logging


def main():
    logger = logging.getLogger("hoge.fuga.piyo")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("log/test2.log")
    handler.setLevel(logging.INFO)

    logging_filter = logging.Filter("hoge.fuga")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)
    handler.addFilter(logging_filter)
    logger.addHandler(handler)
    logger.addFilter(logging_filter)

    logger.debug("debug message")
    logger.info("info message")


if __name__ == "__main__":
    main()
