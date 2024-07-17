from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def expect_visible(self, selector, timeout=40000):
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)


