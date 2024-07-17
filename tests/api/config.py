import logging
import os

from dotenv import load_dotenv


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter( logging.Formatter('%(asctime)s - [%(name)s] [%(levelname)s] - %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# Import environment variables from .env file.
load_dotenv()
setup_logger()

API_BASE_URL = "https://api.mspbackups.com/api"

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
BASE_URL = os.getenv('BASE_URL')
BASE_URL_CONSOLE = os.getenv('BASE_URL_CONSOLE')
