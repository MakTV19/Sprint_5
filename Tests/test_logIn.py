from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import RegistrationLocators as Loc

def test_valid_login():
    fake = Faker()
    email = fake.email()
    password = fake.password()

    # Регистрация нового пользователя
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*Loc.LOGIN_BTN).click()
    driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
    driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(Loc.USERNAME_TEXT))

    driver.quit()

    # Повторный вход
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*Loc.LOGIN_BTN).click()
    driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Loc.SUBMIT_BTN).click()

    user_info = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(Loc.USERNAME_TEXT))

    assert user_info.is_displayed()
    driver.quit()
