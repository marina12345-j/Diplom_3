from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Кнопка "Восстановить пароль" на экране входа
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Поле ввода email на странице ввода "Восстановление пароля"
    input_email = (By.XPATH, '//*[@class="input pr-6 pl-6 input_type_text input_size_default"]/*[@class="text input__textfield text_type_main-default"]')

    # Кнопка "Восстановить" на странице ввода "Восстановление пароля"
    button_recover = (By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')

    # Поле ввода пароля
    input_password = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')

    input_password_after = (By.XPATH,
                   '//*[@class="input pr-6 pl-6 input_type_password input_size_default"]/*[@class="text input__textfield text_type_main-default"]')

    # Иконка, скрывающая пароль
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Пароль со статусом видимости
    value_password_is_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_type_text input_size_default input_status_active")]')

    # Пароль скрыт
    value_password_is_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_type_password")]')