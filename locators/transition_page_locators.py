from selenium.webdriver.common.by import By

class TransitionPageLocators:

    LOGO_YANDEX = By.XPATH, "//a[contains(@class,'Header_LogoYandex')]"
    SCOOTER_LOGO = By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"
    DZEN_HEADER = By.XPATH, "//header[@id='dzen-header']"
    MAIN_PAGE_SCOOTER_TEXT = By.XPATH, "//div[contains(@class,'Home_Header')]"
