import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Клик на модалку cookie')
    def click_to_cookie_notification(self):
        self.click_to_element(MainPageLocators.COOKIE_CONFIRM_BUTTON)
    
    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        formatted_question = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_TO_SCROLL)
        self.click_to_element(formatted_question)

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, num):
        formatted_answer = self.format_locators(MainPageLocators.ANSWER_TEXT_LOCATOR, num)
        return self.get_text_from_element(formatted_answer)
    
    @allure.step('Клик на вопрос и поулчение ответа')
    def click_question_and_get_answer(self, num):
        self.click_to_cookie_notification()
        self.click_to_question(num)
        return self.get_answer_text(num)
    