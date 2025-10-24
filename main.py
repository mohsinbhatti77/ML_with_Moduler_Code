from src.exception import CustomException
from src.logging import logging
import sys

logging.info("Pipeline started...")

try:
    a = 10 / 0
except Exception as e:
    raise CustomException(e, sys)
