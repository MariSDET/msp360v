import pytest
from playwright.sync_api import sync_playwright

from tests.playwright.ApComputersPage import ApComputersPage
from tests.playwright.config import (password, playwright_browser_headless, username)
from tests.playwright.data.test_data import test_credentials
from tests.playwright.LoginPage import LoginPage


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=playwright_browser_headless)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_msp_login_and_logout(page):
    # Verifying that existing user can login with valid credentials
    login_page = LoginPage(page)
    ap_computers_page =ApComputersPage(page)
    login_page.open()
    login_page.login(username, password)
    ap_computers_page.verify_user_logged_in()
    ap_computers_page.log_off()
    login_page.validate()

def test_empty_email_login(page):
    # Verifying that user can't login with empty email field
    login_page = LoginPage(page)
    credentials = test_credentials["empty_email"]
    login_page.open()
    login_page.login(credentials["email"], credentials["password"]) 
    login_page.check_required_field_error()

def test_empty_password_login(page):
    # Verifying that user can't login with empty password field
    login_page = LoginPage(page)
    credentials = test_credentials["empty_password"]
    login_page.open()
    login_page.login(credentials["email"], credentials["password"])  
    login_page.check_required_field_error()

def test_non_existing_user_login(page):
     # Verifying that not signed up user can't login 
    login_page = LoginPage(page)
    credentials = test_credentials["non_existing_user"]
    login_page.open()
    login_page.login(credentials["email"], credentials["password"]) 
    login_page.check_invalid_email_password_error

def test_invalid_password_login(page):
    # Verifying that user can't login with invalid password
    login_page = LoginPage(page)
    credentials = test_credentials["existing_user_invalid_password"]
    login_page.open()
    login_page.login(credentials["email"], credentials["password"])  
    login_page.check_invalid_email_password_error() 

def test_valid_email_with_spaces_login(page):
    # Verifying that user should login with head and tail spaces added to username (assuming as designed).
    login_page = LoginPage(page)
    ap_computers_page =ApComputersPage(page)
    credentials = test_credentials["valid_email_with_spaces"]
    login_page.open()
    login_page.login(credentials["email"], credentials["password"])  
    ap_computers_page.verify_user_logged_in()
      
def test_valid_password_with_spaces_login(page):
    # Verifying that user can't login with head and tail spaces added to password
    login_page = LoginPage(page)
    credentials = test_credentials["valid_password_with_spaces"]
    login_page.open()
    login_page.login(credentials["email"], credentials["password"])
    login_page.check_invalid_email_password_error()        

      


