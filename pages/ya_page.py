from selenium.webdriver.common.by import By

from pages.base_page import BasePage
class LocatorsYaPage:
    locator_ya_search = (By.XPATH, ".//div[@class='dzen-search-arrow-common__border']/div[@class='dzen-search-arrow-common__placeholder']")

class YaPage(BasePage):

    def get_ya_search_text(self):
        ya_search = self.find_element(LocatorsYaPage.locator_ya_search).text
        return ya_search
