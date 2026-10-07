import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture(scope="function")
def browser_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

class TestSauceDemo:
    
    def test_valid_login(self, browser_setup):
        page = browser_setup
        page.goto(BASE_URL)
        
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        assert products_page.is_loaded(), "Products page should load after login"

    def test_invalid_login(self, browser_setup):
        page = browser_setup
        page.goto(BASE_URL)
        
        login_page = LoginPage(page)
        login_page.login("invalid_user", "wrong_password")
        
        error_msg = login_page.get_error_message()
        assert "Username and password do not match" in error_msg

    def test_add_to_cart(self, browser_setup):
        page = browser_setup
        page.goto(BASE_URL)
        
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_backpack_to_cart()
        
        assert products_page.get_cart_count() == "1", "Cart should show 1 item"