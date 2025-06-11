import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.transition_page import TransitionPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    yield driver 
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return page

@pytest.fixture
def transition_page(driver):
    page = TransitionPage(driver)
    return page