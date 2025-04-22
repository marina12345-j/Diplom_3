import pytest
from selenium import webdriver
from data import IngredientData
from helpers import *
import requests
from urls import Urls
import allure


@pytest.fixture(params=['chrome', 'firefox'], ids=['chrome', 'firefox']) #
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.get(Urls.base_url)
    yield browser
    browser.quit()

@pytest.fixture
def generate_user_credentials():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_username()
    return email, password, name

@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными кредами и удаляет его из базы после теста')
def new_user_creature_and_delete():  # create_new_user_and_delete
    payload_cred = {
        'email': generate_random_email(),
        'password': generate_random_password(),
        'name': generate_random_username()
    }
    response = requests.post(Urls.user_register, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Urls.user_delete, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ для его аккаунта')
def create_user_and_order_and_delete(new_user_creature_and_delete):
    access_token = new_user_creature_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [IngredientData.burger_2]}
    response_body = requests.post(Urls.order_create, data=payload, headers=headers)

    yield access_token, response_body

    requests.delete(Urls.user_delete, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура передает в драйвер токены созданного пользователя')
def set_user_tokens(driver, new_user_creature_and_delete):
    driver.get(Urls.base_url)
    user_data = new_user_creature_and_delete[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')



