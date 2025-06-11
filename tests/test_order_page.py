import pytest
import sys
import allure
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from locators.main_page_locators import MainPageLocators
from urls import URL_MAIN_PAGE
from data import ORDER_DATA_1
from data import ORDER_DATA_2
from data import SUCCESS_ORDER_TEXT


class TestOrderPage:

    @allure.title('Тесты на проверку создания заказа')
    @allure.description('Проверяем полный цикл создания заказа на 2 наборах тестовых данных')
    @pytest.mark.parametrize(
        'locator, order_data', 
        [
            (MainPageLocators.HEADER_ORDER_BUTTON, ORDER_DATA_1),
            (MainPageLocators.MAIN_PAGE_ORDER_BUTTON, ORDER_DATA_2)
        ]
    )
    def test_create_order(self, main_page, order_page, locator, order_data):
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.click_to_cookie_notification()
        main_page.click_to_element(locator)
        order_page.create_order(order_data)
        assert SUCCESS_ORDER_TEXT in order_page.check_order(), 'Модальное окно "Заказ оформлен" не отображается'