from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import RegistrationLocators as Loc

class TestRegistration:

    def test_valid_user_registration(self):
        fake = Faker()
        new_email = fake.email()
        password = fake.password()

        driver = webdriver.Chrome()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*Loc.LOGIN_BTN).click()
        driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        driver.find_element(*Loc.EMAIL_INPUT).send_keys(new_email)
        driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        user_info = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Loc.USERNAME_TEXT))

        assert user_info.is_displayed()

        driver.quit()

    def test_registration_invalid_email(self):
        driver = webdriver.Chrome()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*Loc.LOGIN_BTN).click()
        driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        driver.find_element(*Loc.EMAIL_INPUT).send_keys("***")
        driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Loc.ERROR_HINT))

        assert "Ошибка" in error.text
        driver.quit()

    def test_registration_existing_user(self):
        driver = webdriver.Chrome()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        fake = Faker()
        email = fake.email()
        password = fake.password()

        driver = webdriver.Chrome()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*Loc.LOGIN_BTN).click()
        driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Loc.USERNAME_TEXT))
        driver.quit()

        driver = webdriver.Chrome()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*Loc.LOGIN_BTN).click()
        driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Loc.ERROR_HINT))

        assert "Ошибка" in error.text
        driver.quit()
