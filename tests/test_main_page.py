import pytest
import sys
import allure
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data import ANSWERS_DATA
from urls import URL_MAIN_PAGE


class TestMainPage:

    @allure.title('Тесты на проверку ответов на вопросы на главной странице')
    @allure.description('Проверяем, что текст каждого ответа на вопрос совпадает с ожидаемым')
    @pytest.mark.parametrize(
        'num', [0, 1, 2, 3, 4, 5, 6, 7]
    )
    def test_check_answer_text(self, main_page, num):
        main_page.go_to_url(URL_MAIN_PAGE)
        assert main_page.click_question_and_get_answer(num) == ANSWERS_DATA[num], 'Ответ/ы не совпал/и с ожидаемым/и'