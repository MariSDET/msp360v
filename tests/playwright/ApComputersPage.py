from config import username

from tests.playwright.BasePage import BasePage


class ApComputersPage(BasePage):
    NAVBAR = "#navbarSupportedContent"
    LOG_OFF_BUTTON = "role=button[name=' Log off']"
    USER_INFO_NAVBAR = "role=button[name='']"
    USERNAME = F"text={username}"

    def verify_user_logged_in(self):
        self.expect_visible(self.NAVBAR)
        self.click(self.USER_INFO_NAVBAR) 
        self.expect_visible(self.USERNAME)

    def log_off(self):
        self.click(self.LOG_OFF_BUTTON)
        

