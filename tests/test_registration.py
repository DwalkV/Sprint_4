from pages.main_page import MainPage, LocatorsMainPage
from pages.order_page import OrderPage, LocatorOrderPage
import allure

registration_data = [
    'Дарья', 'Волк', 'На Луну', '+79112221111',
'Крокодил', 'Гена', 'В лес', '+79102120000'
]
@allure.story('Проверка регистрации')
class TestRegistration:

    @allure.title('Проверка регистрации через кнопку в шапке')
    def test_registration_from_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_header()
        order_page = OrderPage(driver)
        order_page.registration(registration_data[0],registration_data[1],registration_data[2],registration_data[3])
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
        order_page.registration(registration_data[4],registration_data[5],registration_data[6],registration_data[7])
        order_page.set_metro_bulv()
        order_page.click_button_next()
        order_page.set_period_three_and_date_25()
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.get_order_status()

