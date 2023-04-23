from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Открываем сайт «Самокат»')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')

    def scroll(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)


