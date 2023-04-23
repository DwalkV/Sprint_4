from pages.main_page import MainPage
import allure
from pages.order_page import OrderPage,  registration_data_1, registration_data_2


@allure.story('Проверка регистрации')
class TestRegistration:

    @allure.title('Проверка регистрации через кнопку в шапке')
    def test_registration_from_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_header()
        order_page = OrderPage(driver)
        order_page.registration(registration_data_1)
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
        order_page.registration(registration_data_2)
        order_page.set_metro_bulv()
        order_page.click_button_next()
        order_page.set_period_three_and_date_25()
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.get_order_status()

