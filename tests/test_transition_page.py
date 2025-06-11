import pytest
import sys
import allure
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from urls import URL_MAIN_PAGE
from data import MAIN_PAGE_TEXT


class TestTransitionPage:

    @allure.title('Тест на проверку перехода по лого Яндекс')
    @allure.description('Проверяем, что при клике на лого Яндекса происходит переход на главную Яндекс.Дзен')
    def test_click_to_yandex_logo_transition_to_dzen(self, transition_page):
        transition_page.go_to_url(URL_MAIN_PAGE)
        assert transition_page.click_to_yandex_logo_and_check_transition().is_displayed(), 'Ошибка перехода на главную Яндекс.Дзен'

    @allure.title('Тест на проверку перехода по лого Яндекс.Самокат')
    @allure.description('Проверяем, что при клике на лого Самоката происходит переход на главную Яндекс.Самокат')
    def test_click_to_scooter_logo_transition_to_main_page(self, transition_page):
        transition_page.go_to_url(URL_MAIN_PAGE)
        assert MAIN_PAGE_TEXT in transition_page.click_to_scooter_logo_and_check_transition(), 'Ошибка перехода на главную Яндекс.Самокат'