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

    @allure.step('Нажимаем «Заказать» в внизу страницы')
    def click_on_button_order_middle(self):
        button_order_middle = self.find_element(LocatorsMainPage.locator_button_order_middle)
        self.scroll(button_order_middle)
        button_order_middle.click()

    def get_value_for_check_main_page(self):
        value_for_check_main_page = self.find_element(LocatorsMainPage.locator_check_main_page).text
        return value_for_check_main_page

    @allure.step('Нажимаем на вопрос о цене')
    def click_on_question_price(self):
        question_price_click = self.find_element(LocatorsMainPage.locator_question_price)
        self.scroll(question_price_click)
        question_price_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_price(self):
        answer_question_price = self.find_element(LocatorsMainPage.locator_answer_price).text
        return answer_question_price

    @allure.step('Нажимаем на вопрос о нескольких самокатах')
    def click_on_question_few_scooter(self):
        question_few_scooter_click = self.find_element(LocatorsMainPage.locator_question_few_scooter)
        self.scroll(question_few_scooter_click)
        question_few_scooter_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_few_scooter(self):
        answer_question_few_scooter = self.find_element(LocatorsMainPage.locator_answer_few_scooter).text
        return answer_question_few_scooter

    @allure.step('Нажимаем на вопрос о сроках аренды')
    def click_on_question_rental_period(self):
        question_rental_period_click = self.find_element(LocatorsMainPage.locator_question_rental_period)
        self.scroll(question_rental_period_click)
        question_rental_period_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_rental_period(self):
        answer_question_rental_period = self.find_element(LocatorsMainPage.locator_answer_rental_period).text
        return answer_question_rental_period


    @allure.step('Нажимаем на вопрос о заказе на сегодня')
    def click_on_question_today_order(self):
        question_today_order_click = self.find_element(LocatorsMainPage.locator_question_today_order)
        self.scroll(question_today_order_click)
        question_today_order_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_today_order(self):
        answer_question_today_order = self.find_element(LocatorsMainPage.locator_answer_today_order).text
        return answer_question_today_order

    @allure.step('Нажимаем на вопрос о смене срока аренды')
    def click_on_question_change_period(self):
        question_change_period_click = self.find_element(LocatorsMainPage.locator_question_change_period)
        self.scroll(question_change_period_click)
        question_change_period_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_change_period(self):
        answer_question_change_period = self.find_element(LocatorsMainPage.locator_answer_change_period).text
        return answer_question_change_period

    @allure.step('Нажимаем на вопрос о зарядке')
    def click_on_question_charge(self):
        question_charge_click = self.find_element(LocatorsMainPage.locator_question_charge)
        self.scroll(question_charge_click)
        question_charge_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_charge(self):
        answer_question_charge = self.find_element(LocatorsMainPage.locator_answer_charge).text
        return answer_question_charge

    @allure.step('Нажимаем на вопрос об отмене')
    def click_on_question_cancel(self):
        question_cancel_click = self.find_element(LocatorsMainPage.locator_question_cancel)
        self.scroll(question_cancel_click)
        question_cancel_click.click()

    @allure.step('Проверяем текст ответа')
    def get_answer_question_cancel(self):
        answer_question_cancel = self.find_element(LocatorsMainPage.locator_answer_cancel).text
        return answer_question_cancel

    @allure.step('Нажимаем на вопрос о заказе за МКАДом')
    def click_on_question_county(self):
        question_county_click = self.find_element(LocatorsMainPage.locator_question_county)
        self.scroll(question_county_click)
        question_county_click.click()


    @allure.step('Проверяем текст ответа')
    def get_answer_question_county(self):
        answer_question_county = self.find_element(LocatorsMainPage.locator_answer_county).text
        return answer_question_county

    @allure.step('Нажимаем на логотип Яндекс')
    def click_on_ya_logo(self):
        button_ya_logo = self.find_element(LocatorsMainPage.locator_yandex_logo)
        button_ya_logo.click()