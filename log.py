import logging
from config import Config


logging.basicConfig(filename=Config.logs_file_name, filemode="w", level=Config.log_level)