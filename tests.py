
import uuid
import time
from selenium.webdriver.common.by import By
from locators import MainPageLocators, AuthPageLocators, UserInfoLocators, AdCreationLocators

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

def generate_email():
    return f"{uuid.uuid4()}@test.com"

def test_valid_registration(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).click()
    driver.find_element(*AuthPageLocators.NO_ACCOUNT_BUTTON).click()

    email = generate_email()
    driver.find_element(*AuthPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*AuthPageLocators.PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.REPEAT_PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(*UserInfoLocators.USER_NAME).is_displayed()

def test_registration_invalid_email(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).click()
    driver.find_element(*AuthPageLocators.NO_ACCOUNT_BUTTON).click()

    driver.find_element(*AuthPageLocators.EMAIL_FIELD).send_keys("invalid-email")
    driver.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(*AuthPageLocators.ERROR_MESSAGE).is_displayed()

def test_registration_existing_user(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).click()
    driver.find_element(*AuthPageLocators.NO_ACCOUNT_BUTTON).click()

    driver.find_element(*AuthPageLocators.EMAIL_FIELD).send_keys("test@test.com")
    driver.find_element(*AuthPageLocators.PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.REPEAT_PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(*AuthPageLocators.ERROR_MESSAGE).is_displayed()

def test_login(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).click()
    driver.find_element(*AuthPageLocators.EMAIL_FIELD).send_keys("test@test.com")
    driver.find_element(*AuthPageLocators.PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(*UserInfoLocators.USER_NAME).is_displayed()

def test_logout(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).click()
    driver.find_element(*AuthPageLocators.EMAIL_FIELD).send_keys("test@test.com")
    driver.find_element(*AuthPageLocators.PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    driver.find_element(*UserInfoLocators.LOGOUT_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).is_displayed()

def test_create_ad_unauthorized(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.POST_AD_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(*MainPageLocators.MODAL_TITLE).text == "Чтобы разместить объявление, авторизуйтесь"

def test_create_ad_authorized(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_REG_BUTTON).click()
    driver.find_element(*AuthPageLocators.EMAIL_FIELD).send_keys("test@test.com")
    driver.find_element(*AuthPageLocators.PASSWORD_FIELD).send_keys("ValidPass123")
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    driver.find_element(*MainPageLocators.POST_AD_BUTTON).click()
    time.sleep(1)
    driver.find_element(*AdCreationLocators.TITLE_FIELD).send_keys("Test Product")
    driver.find_element(*AdCreationLocators.DESCRIPTION_FIELD).send_keys("Test Description")
    driver.find_element(*AdCreationLocators.PRICE_FIELD).send_keys("1000")
    driver.find_element(*AdCreationLocators.CATEGORY_DROPDOWN).click()
    driver.find_element(By.XPATH, "//option[2]").click()
    driver.find_element(*AdCreationLocators.CITY_DROPDOWN).click()
    driver.find_element(By.XPATH, "//option[2]").click()
    driver.find_element(*AdCreationLocators.CONDITION_RADIO_NEW).click()
    driver.find_element(*AdCreationLocators.PUBLISH_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(*AdCreationLocators.MY_ADS_BLOCK).is_displayed()
    assert driver.find_element(*AdCreationLocators.CREATED_AD_TITLE).is_displayed()

