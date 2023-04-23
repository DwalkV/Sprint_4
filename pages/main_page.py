from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class LocatorsMainPage:
    locator_button_order_header = (By.XPATH, ".//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]")
    locator_button_order_middle = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    locator_check_main_page = (By.XPATH, ".//div[contains(@class,'Home_Header__iJKdX')]")
    locator_yandex_logo = (By.XPATH, ".//img[@alt='Yandex'] ")

    locator_question_price = (By.XPATH, ".//*[@id='accordion__heading-0']")
    locator_answer_price = (By.XPATH, ".//*[@id='accordion__panel-0']")

    locator_question_few_scooter = (By.XPATH, ".//*[@id='accordion__heading-1']")
    locator_answer_few_scooter = (By.XPATH, ".//*[@id='accordion__panel-1']")

    locator_question_rental_period = (By.XPATH, ".//*[@id='accordion__heading-2']")
    locator_answer_rental_period = (By.XPATH, ".//*[@id='accordion__panel-2']")

    locator_question_today_order = (By.XPATH, ".//*[@id='accordion__heading-3']")
    locator_answer_today_order = (By.XPATH, ".//*[@id='accordion__panel-3']")

    locator_question_change_period = (By.XPATH, ".//*[@id='accordion__heading-4']")
    locator_answer_change_period = (By.XPATH, ".//*[@id='accordion__panel-4']")

    locator_question_charge = (By.XPATH, ".//*[@id='accordion__heading-5']")
    locator_answer_charge = (By.XPATH, ".//*[@id='accordion__panel-5']")

    locator_question_cancel = (By.XPATH, ".//*[@id='accordion__heading-6']")
    locator_answer_cancel = (By.XPATH, ".//*[@id='accordion__panel-6']")

    locator_question_county = (By.XPATH, ".//*[@id='accordion__heading-7']")
    locator_answer_county = (By.XPATH, ".//*[@id='accordion__panel-7']")

class MainPage(BasePage):

    @allure.step('Нажимаем «Заказать» в шапке профиля')
    def click_on_button_order_header(self):
        button_order_header = self.find_element(LocatorsMainPage.locator_button_order_header)
        button_order_header.click()

    @allure.step('Нажимаем «Заказать» внизу страницы')
    def click_on_button_order_middle(self):
        button_order_middle = self.find_element(LocatorsMainPage.locator_button_order_middle)
        self.scroll(button_order_middle)
        button_order_middle.click()

    def get_value_for_check_main_page(self):
        value_for_check_main_page = self.find_element(LocatorsMainPage.locator_check_main_page).text
        return value_for_check_main_page

    @allure.step('Нажимаем на вопрос')
    def click_on_question(self, locator):
        question_click = self.find_element(locator)
        self.scroll(question_click)
        question_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer(self, locator):
        answer_question = self.find_element(locator).text
        return answer_question

    @allure.step('Нажимаем на логотип Яндекс')
    def click_on_ya_logo(self):
        button_ya_logo = self.find_element(LocatorsMainPage.locator_yandex_logo)
        button_ya_logo.click()