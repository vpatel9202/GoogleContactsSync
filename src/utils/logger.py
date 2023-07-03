"""
logger.py
Created on: Jul 3, 2023
Author: vpatel9202, Assisted by: OpenAI Chatbot

This module sets up a customized logger to be used in the application.
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import date

LOG_DIR = "./logs"
LOG_FILE = f"{LOG_DIR}/{date.today():%Y-%m-%d}.log"
LOG_LEVEL = logging.DEBUG

# Create log directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Create the log handlers
file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight", backupCount=30)
console_handler = logging.StreamHandler()

# Configure the log handlers
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(filename)s - %(funcName)s (%(lineno)d): %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Create the logger
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)  # This could be an environment variable
logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__ == "__main__":
    logger.debug("This is a debug log message")
    logger.info("This is an info log message")
    logger.warning("This is a warning log message")
    logger.error("This is an error log message")
    logger.critical("This is a critical log message")
