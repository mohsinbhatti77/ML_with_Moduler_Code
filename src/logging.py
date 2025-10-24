import logging
import os
from datetime import datetime

# Create a log directory if it doesn’t exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Optional: show where logs are being saved
print(f"Logging initialized. Log file: {LOG_FILE_PATH}")
