import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_on_personal_account_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.button_personal_account)
        self.click_on_element(MainPageLocators.button_personal_account)

    @allure.step('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.wait_visibility_of_element(MainPageLocators.button_order_feed_in_header)
        self.click_on_element(MainPageLocators.button_order_feed_in_header)

    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.header_of_page_constructor)
        self.click_on_element(MainPageLocators.header_of_page_constructor)

    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        return self.get_text_on_element(MainPageLocators.constructor_title)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        self.click_on_element(MainPageLocators.button_login_in_main)

    @allure.step('Кликнуть по кнопке "Войти" в окне Вход')
    def click_on_button_enter(self):
        self.click_on_element(MainPageLocators.button_enter)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_visibility_of_element(MainPageLocators.obj_modal_window)
        return self.check_displaying_of_element(MainPageLocators.obj_modal_window)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.burger_ingredient)
        self.click_on_element(MainPageLocators.burger_ingredient)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        self.wait_visibility_of_element(MainPageLocators.header_of_modal_details)
        return self.check_displaying_of_element(MainPageLocators.header_of_modal_details)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(MainPageLocators.header_of_modal_details)
        if not self.check_displaying_of_element(MainPageLocators.header_of_modal_details):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        self.wait_visibility_of_element(MainPageLocators.button_close_modal)
        self.click_on_element(MainPageLocators.button_close_modal)

    @allure.step('Добавить ингредиенты')
    def drag_and_drop_ingredient_to_order(self):
        self.click_on_element(MainPageLocators.burger_ingredient)
        self.move_element(MainPageLocators.burger_ingredient, MainPageLocators.place_for_ingredients)

    @allure.step('Добавить ингредиент (соус)')
    def drag_and_drop_ingredient_to_order_sauce(self):
        self.move_element(MainPageLocators.burger_ingredient_sauce, MainPageLocators.place_for_ingredients)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainPageLocators.count_of_ingredient)

    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def click_on_button_make_order(self):
        self.click_on_element(MainPageLocators.button_make_order)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.find_element_with_wait(MainPageLocators.number_of_order_in_modal_confirmation)
        self.wait_for_element_to_change_text(MainPageLocators.number_of_order_in_modal_confirmation, '9999')
        return self.get_text_on_element(MainPageLocators.number_of_order_in_modal_confirmation)

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def close_modal_window_success_order(self):
        self.wait_for_element_to_change_text(MainPageLocators.number_of_order_in_modal_confirmation, '9999')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element(MainPageLocators.obj_modal_window))
        self.click_on_element_finish(MainPageLocators.button_close_confirmation)
