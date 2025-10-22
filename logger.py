# logger.py
import logging
import sys


def get_logger(name: str = __name__, level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level.upper())

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger
