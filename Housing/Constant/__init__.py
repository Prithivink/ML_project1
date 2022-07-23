from distutils.command.config import config
import os
from datetime import datetime

ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE = "config.yaml"
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR,CONFIG_FILE)
CURRENT_TIME_STAMP = datetime.now().strftime(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))