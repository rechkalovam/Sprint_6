import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Создание заказа 1 часть')
    def create_order_part_1(self, data):
        self.find_element_with_wait(OrderPageLocators.ORDER_FORM_TITLE_1)
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, data["name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT, data["last_name"])
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.click_to_element(OrderPageLocators.METRO_STATION_DROPDOWN)
        metro_station_locator = self.format_locators(OrderPageLocators.CHOOSE_METRO_STATION_IN_DROPDOWN, data["metro_station"])
        self.click_to_element(metro_station_locator)
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, data["phone_number"])
        self.click_to_element(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step('Создание заказа 2 часть')
    def create_order_part_2(self, data):
        self.find_element_with_wait(OrderPageLocators.ORDER_FORM_TITLE_2)
        self.click_to_element(OrderPageLocators.DELIVERY_DATE_DATEPICKER)
        delivery_date_locator = self.format_locators(OrderPageLocators.CHOOSE_DELIVERY_DATE_IN_DATEPICKER, data["delivery_date_and_time"])
        self.click_to_element(delivery_date_locator)
        self.click_to_element(OrderPageLocators.PERIOD_OF_RENT_DROPDOWN)
        period_date_locator = self.format_locators(OrderPageLocators.CHOOSE_PERIOD_OF_RENT_DROPDOWN, data["period_of_rent"])
        self.click_to_element(period_date_locator)
        choose_color_locator = self.format_locators(OrderPageLocators.CHOOSE_COLOR_CHECKBOX, data["color"])
        self.click_to_element(choose_color_locator)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, data["comment"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждение заказа')
    def confirmation_order(self):
        self.find_element_with_wait(OrderPageLocators.CONFIRMATION_ORDER_WINDOW_TITLE)
        self.click_to_element(OrderPageLocators.CONFIRMATION_ORDER_WIDOW_YES_BUTTON)

    @allure.step('Создание и подтверждение заказа')
    def create_order(self, data):
        self.create_order_part_1(data)
        self.create_order_part_2(data)
        self.confirmation_order()

    @allure.step('Проверка создания заказа')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_INFORMATION_WINDOW_TITLE)