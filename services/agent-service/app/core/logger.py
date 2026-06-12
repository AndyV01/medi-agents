import logging
import sys


def setup_logger(service_name: str) -> logging.Logger:

    logger = logging.getLogger(service_name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            f"{service_name} | "
            "%(levelname)s | "
            "%(filename)s:%(lineno)d | "
            "%(message)s"
        )
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger