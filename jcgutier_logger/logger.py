#!/usr/bin/env python

"""
Set up logging for python script
"""

import inspect
import logging.config
import os

# Logging config
frm = inspect.stack()[1]
MODULE = os.path.basename(os.path.dirname(os.path.abspath(frm.filename)))
LOG_FILE_NAME = f"/var/tmp/{MODULE}"
LOG_LEVEL = os.getenv("LOGLEVEL", "INFO")
LOG_FILENAME = os.getenv("LOG_FILE_NAME", LOG_FILE_NAME)
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": (
                "%(asctime)s %(name)s %(filename)s:%(lineno)d %(levelname)-8s "
                " %(message)s"
            )
        },
        "long": {
            "format": (
                "%(asctime)s %(name)s %(module)s.%(funcName)s "
                "%(filename)s:%(lineno)d %(levelname)-8s  %(message)s"
            )
        },
    },
    "root": {"handlers": ["log_file", "console"], "level": LOG_LEVEL},
    "loggers": {
        "botocore": {
            "level": "CRITICAL",
            "handlers": ["log_file"],
            "propagate": "no",
        },
        "urllib3": {
            "level": "CRITICAL",
            "propagate": "no",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": LOG_LEVEL,
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "log_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "long",
            "filename": LOG_FILENAME,
            "maxBytes": 10485760,
            "backupCount": 2,
            "encoding": "utf8",
        },
    },
}


class Logger:
    """Logging configuration"""

    def __init__(self, debug: bool) -> None:
        self.debug = debug
        self.setup_logging()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel("DEBUG")

    def setup_logging(self) -> None:
        """Setup logging"""
        if self.debug:
            LOGGING_CONFIG["root"]["level"] = "DEBUG"
            LOGGING_CONFIG["handlers"]["console"]["level"] = "DEBUG"
        logging.config.dictConfig(LOGGING_CONFIG)

    def get_logger(self) -> logging.Logger:
        """Get logger

        Returns:
            logging.Logger: Logger
        """
        return self.logger


if __name__ == "__main__":
    log = Logger(False)
    logger = log.get_logger()
    logger.info("Info log")
    logger.warning("Warning log")
    logger.critical("Critical log")
    logger.error("Error log")
    logger.debug("Debug log")
