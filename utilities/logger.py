
import logging
import os


def get_logger(name):

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # Write logs into a file
        file_handler = logging.FileHandler(
            "logs/automation.log",
            encoding="utf-8"
        )

        # Display logs in console
        console_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# import logging

 
# def get_logger():
 
#     logger = logging.getLogger(__name__)
 
#     logger.setLevel(logging.INFO)
 
#     formatter = logging.Formatter(
#         "%(asctime)s : %(levelname)s : %(message)s"
#     )
 
#     file_handler = logging.FileHandler("automation.log")  # ,mode="w"
 
#     file_handler.setFormatter(formatter)
 
#     if not logger.handlers:
#         logger.addHandler(file_handler)
 
#     return logger