import os

from dotenv import load_dotenv

load_dotenv()  # Load .env file

# Defining base URL and other user credentials from environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
BASE_URL = os.getenv('BASE_URL')
BASE_URL_CONSOLE = os.getenv('BASE_URL_CONSOLE')
playwright_browser_headless = os.getenv('PLAYWRIGHT_BROWSER_HEADLESS', default='False').lower() in ("true", "1", "t", "y", "yes")
