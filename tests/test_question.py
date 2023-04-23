from pages.main_page import MainPage, LocatorsMainPage
import allure

answers = [
    'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
]

@allure.story('Проверка вопросов-ответов')
class TestQuestion:

    @allure.title('Проверка вопроса о цене')
    def test_question_price(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_price)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_price) == answers[0]

    @allure.title('Проверка вопроса о нескольких самокатах')
    def test_question_few_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_few_scooter)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_few_scooter) == answers[1]

    @allure.title('Проверка вопроса о сроках аренды')
    def test_question_rental_period(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_rental_period)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_rental_period) == answers[2]

    @allure.title('Проверка вопроса о заказе на сегодня')
    def test_question_today_order(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_today_order)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_today_order) == answers[3]

    @allure.title('Проверка вопроса о изменении срока')
    def test_question_change_period(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_change_period)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_change_period) == answers[4]

    @allure.title('Проверка вопроса о зарядке')
    def test_question_charge(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_charge)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_charge) == answers[5]

    @allure.title('Проверка вопроса об отмене')
    def test_question_cancel(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_cancel)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_cancel) == answers[6]

    @allure.title('Проверка вопроса о заказке за МКАД')
    def test_question_county(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(LocatorsMainPage.locator_question_county)
        assert main_page.get_answer(LocatorsMainPage.locator_answer_county) == answers[7]