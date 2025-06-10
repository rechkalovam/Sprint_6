from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_FORM_TITLE_1 = By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Для кого самокат']"
    NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    LAST_NAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_DROPDOWN = By.XPATH, "//input[@class='select-search__input']"
    CHOOSE_METRO_STATION_IN_DROPDOWN = By.XPATH, "//button[contains(@class,'select-search__option')]/div[contains(@class,'Order_Text') and text()='{}']"
    PHONE_NUMBER_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    CONTINUE_BUTTON = By.XPATH, "//button[text()='Далее']"
    ORDER_FORM_TITLE_2 = By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Про аренду']"
    DELIVERY_DATE_DATEPICKER = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CHOOSE_DELIVERY_DATE_IN_DATEPICKER = By.XPATH, "//div[contains(@class, 'react-datepicker__day') and contains(@aria-label, '{}')]"
    PERIOD_OF_RENT_DROPDOWN = By.XPATH, "//div[@class='Dropdown-control']/div[text()='* Срок аренды']"
    CHOOSE_PERIOD_OF_RENT_DROPDOWN = By.XPATH, "//div[@class='Dropdown-option' and text()='{}']"
    CHOOSE_COLOR_CHECKBOX =  By.XPATH, "//label[contains(@class, 'Checkbox_Label') and text()='{}']/input"
    COMMENT_INPUT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"
    CONFIRMATION_ORDER_WINDOW_TITLE = By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Хотите оформить заказ?']"
    CONFIRMATION_ORDER_WIDOW_YES_BUTTON = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Да']"
    ORDER_INFORMATION_WINDOW_TITLE = By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']"