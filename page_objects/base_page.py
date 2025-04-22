from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
         action = ActionChains(self.driver)
         WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
         element = self.driver.find_element(*locator)
         action.click(on_element=element).perform()

    @allure.step('Кликнуть на элемент закрытия в конце теста')
    def click_on_element_finish(self, locator):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Перетащить элемент')
    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(
            self.driver, 5
        ).until_not(expected_conditions.text_to_be_present_in_element(locator, value))
