from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import RegistrationLocators as Loc, LogoutLocators as LogoutLoc

def test_user_logout():
        driver = webdriver.Chrome()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        fake = Faker()
        email = fake.email()
        password = fake.password()

        driver.find_element(*Loc.LOGIN_BTN).click()
        driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Loc.USERNAME_TEXT))

        driver.find_element(*LogoutLoc.LOGOUT_BTN).click()

        login_btn = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Loc.LOGIN_BTN))

        assert login_btn.is_displayed()
        driver.quit()