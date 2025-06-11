from selenium.webdriver.common.by import By

class MainPageLocators:

    COOKIE_CONFIRM_BUTTON = By.XPATH, "//button[@id='rcc-confirm-button']"
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWER_TEXT_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']/p"
    LAST_QUESTION_TO_SCROLL = By.XPATH, "//div[@id='accordion__heading-7']"
    HEADER_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    MAIN_PAGE_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"