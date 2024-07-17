from config import BASE_URL_CONSOLE

from tests.playwright.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = "input[placeholder='Email address']"
    PASSWORD_FIELD = "input[placeholder='Password']"
    LOGIN_BUTTON = "role=button[name='Login']"
    LOGIN_URL = f"{BASE_URL_CONSOLE}/Admin/Login.aspx"
    REQUIRED_FIELD_ERROR = "text='Some of the required fields are blank'"
    INVALID_EMAIL_PASSWORD_ERROR = "text ='Invalid email address or password'"

    def __init__(self, page):
        self.page = page  

    def open(self):
        self.navigate(self.LOGIN_URL)
        # self.page.pause()  

    def validate(self):
        # Get the current page URL
        current_url = self.page.url
        # Check if 'login' is a substring of the current URL
        if 'login' not in current_url.lower():  # using lower() to make the check case-insensitive
            raise AssertionError(f"Expected URL to contain 'login', but got {current_url}")    

    def login(self, username, password):
        self.fill(self.EMAIL_FIELD, username)
        self.fill(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def check_required_field_error(self):
        self.expect_visible(self.REQUIRED_FIELD_ERROR)  

    def check_invalid_email_password_error(self):
        self.expect_visible(self.INVALID_EMAIL_PASSWORD_ERROR)            

