import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables
VALID_PASSWORD = os.getenv('PASSWORD')
VALID_EMAIL = os.getenv('USERNAME')

if not VALID_PASSWORD or not VALID_EMAIL:
    raise ValueError("Environment variables for USERNAME and PASSWORD must be set")


test_credentials = {
    "empty_email": {
        "email": "",
        "password": VALID_PASSWORD
    },
    "empty_password": {
        "email": VALID_EMAIL,
        "password": ""
    },
    "non_existing_user": {
        "email": "non_existing_user@example.com",
        "password": VALID_PASSWORD
    },
    "existing_user_invalid_password": {
        "email": VALID_EMAIL,
        "password": "invalid_password"
    },
    "invalid_email_format": {
        "email": "invalid_email",
        "password": VALID_PASSWORD
    },
    "valid_email_with_spaces": {
        "email": " " + VALID_EMAIL + " ",
        "password": VALID_PASSWORD
    },
    "valid_password_with_spaces": {
        "email": VALID_EMAIL,
        "password": " " + VALID_PASSWORD + " "
    }
}
