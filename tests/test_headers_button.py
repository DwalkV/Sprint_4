from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.ya_page import YaPage
import allure

@allure.story('Проверка логотипов в шапке')
class TestHeadersButton:

    @allure.title('Проверка логотипа «Самокат»')
    def test_headers_scooter_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_header()
        order_page.click_on_scooter_logo()
        assert "Самокат" in main_page.get_value_for_check_main_page()

    @allure.title('Проверка логотипа «Яндекс»')
    def test_headers_ya_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_ya_logo()
        ya_page = YaPage(driver)
        driver.switch_to.window(driver.window_handles[1])
        assert ya_page.get_ya_search_text() == "Поиск Яндекса"
