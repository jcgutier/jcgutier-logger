#!/usr/bin/env python

"""Test for logger"""

import logging

from jcgutier_logger import Logger


def test_logger_debug_mode():
    """Test logger in DEBUG mode"""
    # Create a Logger instance with debug mode enabled
    logger_instance = Logger(debug=True)

    # Capture the logger's configuration
    logger = logger_instance.get_logger()

    # Check if the root logger's level is set to DEBUG
    assert logging.getLogger().level == logging.DEBUG

    # Check if the handler's level is set to DEBUG
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            assert handler.level == logging.DEBUG


def test_logger_non_debug_mode():
    """Test logger on NON DEBUG mode"""
    # Create a Logger instance with debug mode disabled
    logger_instance = Logger(debug=False)

    # Capture the logger's configuration
    logger = logger_instance.get_logger()

    # Check if the handler's level is set to INFO
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            assert handler.level == logging.INFO
