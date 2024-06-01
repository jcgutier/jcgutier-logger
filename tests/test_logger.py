#!/usr/bin/env python

"""Test for logger"""

from unittest.mock import patch

from jcgutier_logger.logger import Logger


class TestLogger:
    """Test for Logger class"""

    @patch("jcgutier_logger.logger.Logger.setup_logging")
    def test_logger(self, mock):
        """Test for looger"""
        logger = Logger(False)
        assert not logger.debug
        mock.assert_called()
