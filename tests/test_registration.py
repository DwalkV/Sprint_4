from dataclasses import dataclass
from pages.main_page import MainPage, LocatorsMainPage
from pages.order_page import OrderPage, LocatorOrderPage
import allure

@dataclass
class Registration():
    name: str
    surname: str
    address: str
    phone: str

registration_data_1 = Registration('Дарья', 'Волк', 'На Луну', '+79112221111')
registration_data_2 = Registration('Крокодил', 'Гена', 'В лес', '+79102120000')

@allure.story('Проверка регистрации')
class TestRegistration:

    @allure.title('Проверка регистрации через кнопку в шапке')
    def test_registration_from_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_header()
        order_page = OrderPage(driver)
        order_page.registration(registration_data_1.name, registration_data_1.surname, registration_data_1.address, registration_data_1.phone)
        order_page.set_metro_cher()
        order_page.click_button_next()
        order_page.set_period_two_and_date_22()
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.get_order_status()

    @allure.title('Проверка регистрации через кнопку внизу страницы')
    def test_registration_from_middle_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_middle()
        order_page = OrderPage(driver)
        order_page.registration(registration_data_2.name, registration_data_2.surname, registration_data_2.address, registration_data_2.phone)
        order_page.set_metro_bulv()
        order_page.click_button_next()
        order_page.set_period_three_and_date_25()
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.get_order_status()

