from config import BASE_URL

from tests.playwright.BasePage import BasePage


class SignUpPage(BasePage):
    SIGN_IN_BUTTON = "text=Sign In"
    MSP_BACKUP_LINK = "role=link[name='MSP360 Managed Backup Login']"
    SIGNUP_URL = f"{BASE_URL}/managed-backup/signup/"
    SIGNUP_FORM_TITLE = "form >> text=MSP360 Backup"

    def open(self):
        self.navigate(self.SIGNUP_URL)
        # self.page.pause()
        self.expect_visible(self.SIGNUP_FORM_TITLE)

    def msp360_login(self):
        self.click(self.SIGN_IN_BUTTON)
        self.click(self.MSP_BACKUP_LINK)
        
