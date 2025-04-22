from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной
    button_login_in_main = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # Кнопка "Войти" в окне Вход
    button_enter = (By.XPATH, './/button[text() = "Войти"]')

    # Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')

    # Кнопка "Конструктор" в шапке сайта
    header_of_page_constructor = (By.XPATH, '//p[text() = "Конструктор"]')

    # Заголовок раздела "Соберите бургер "
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Кнопка "Лента заказов"
    button_order_feed_in_header = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    # Заголовок окна "Детали ингредиента"
    header_of_modal_details = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    button_close_modal = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')

    # Картинка ингредиента в общем списке
    burger_ingredient = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')#//*[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]

    # Картинка добавляемого ингредиента в общем списке
    burger_ingredient_sauce = (By.XPATH, './/*[@alt="Соус Spicy-X"]')

    # Куда перетаскиваются ингредиенты
    place_for_ingredients = (By.XPATH, '//*[@class="constructor-element constructor-element_pos_top"]')

    # Кнопка "Оформить заказ"
    button_make_order = (By.XPATH, './/button[text()="Оформить заказ"]')

    # Количество экземпляров ингредиента в заказе (счетчик)
    count_of_ingredient = (By.XPATH, './/div[@class="Modal_priceBox__2U6_9"]')

    # Номер созданного заказа в окне подтверждения
    number_of_order_in_modal_confirmation = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')

    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    button_close_confirmation = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 div.Modal_modal__container__Wo2l_ button.Modal_modal__close_modified__3V5XS")

    obj_modal_window = (By.CLASS_NAME, "Modal_modal__loading__3534A")
