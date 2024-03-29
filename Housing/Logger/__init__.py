from cmath import log
import logging
from datetime import datetime
import os

LOG_DIR = "Housing_logs"
CURRENT_DATE_TIME = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
LOG_FILE_NAME = f"log_{CURRENT_DATE_TIME}.log"
print(LOG_FILE_NAME)

os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)