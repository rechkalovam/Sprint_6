import allure
from pages.base_page import BasePage
from locators.transition_page_locators import TransitionPageLocators


class TransitionPage(BasePage):

    @allure.step('Клик на лого Яндекса')
    def click_to_yandex_logo(self):
        self.click_to_element(TransitionPageLocators.LOGO_YANDEX)
    
    @allure.step('Проверка перехода на Яндекс.Дзен')
    def check_transition_to_dzen(self):
        self.switch_to_last_tab()
        return self.find_element_with_wait(TransitionPageLocators.DZEN_HEADER)

    @allure.step('Клик на лого Яндекса и проверка перехода на Яндекс.Дзен')
    def click_to_yandex_logo_and_check_transition(self):
        self.click_to_yandex_logo()
        return self.check_transition_to_dzen()
    
    @allure.step('Клик на лого Яндекс.Самокат')
    def click_to_scooter_logo(self):
        self.click_to_element(TransitionPageLocators.SCOOTER_LOGO)
    
    @allure.step('Проверка перехода на главную Яндекс.Самокат')
    def check_transition_to_main_page(self):
        return self.get_text_from_element(TransitionPageLocators.MAIN_PAGE_SCOOTER_TEXT)
    
    @allure.step('Клик на лого Яндекс.Самокат и проверка перехода на главную Яндекс.Самокат')
    def click_to_scooter_logo_and_check_transition(self):
        self.click_to_scooter_logo()
        return self.check_transition_to_main_page()

