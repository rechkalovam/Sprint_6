from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()
    
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    def format_locators(self, not_formatted_locator, num):
        method, locator = not_formatted_locator
        locator = locator.format(num)
        return (method, locator)
    
    def switch_to_last_tab(self):
        self.wait.until(expected_conditions.number_of_windows_to_be(2))
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        