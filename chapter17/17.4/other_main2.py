import logging
from logging.config import dictConfig

config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "example": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "filters": {"hoge-filter": {"name": "hoge.fuga"}},
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "log/test3.log",
            "formatter": "example",
            "filters": ["hoge-filter"],
        }
    },
    "loggers": {
        "hoge": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}

dictConfig(config)
logger = logging.getLogger("hoge.fuga.piyo")
logger.debug("debug message")
logger.info("info message")
