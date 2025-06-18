from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import RegistrationLocators as RLoc, CreatePostLocators as CLoc

def test_create_post_unauthorized():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*CLoc.POST_BTN).click()

    modal_title = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(CLoc.MODAL_AUTH_HEADER))

    assert "Чтобы разместить объявление, авторизуйтесь" in modal_title.text

    driver.quit()

def test_create_post_authorized():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    fake = Faker()
    email = fake.email()
    password = fake.password()

    driver.find_element(*RLoc.LOGIN_BTN).click()
    driver.find_element(*RLoc.NO_ACCOUNT_BTN).click()
    driver.find_element(*RLoc.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RLoc.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RLoc.CONFIRM_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RLoc.CREATE_ACCOUNT_BTN).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RLoc.USERNAME_TEXT))

    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*RLoc.LOGIN_BTN).click()
    driver.find_element(*RLoc.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RLoc.PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(RLoc.USERNAME_TEXT))

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CLoc.POST_BTN)).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(CLoc.FORM_TITLE))
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CLoc.NAME_INPUT)).send_keys("Новый товар")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CLoc.DESCRIPTION_INPUT)).send_keys(
        "Новинка самого нового поколения")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(CLoc.PRICE_INPUT)).send_keys("500")


# Работа с дропдауном города
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CLoc.OPEN_DROP_DOWN_CITY))
    driver.find_element(*CLoc.OPEN_DROP_DOWN_CITY).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(CLoc.CITY_OPTIONS))
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CLoc.CITY_OPTION_MSK)).click()

    driver.find_element(*CLoc.CONDITION_NEW_RADIO).click()

    # Публикуем объявление
    publish_btn = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(CLoc.PUBLISH_BTN))
    driver.execute_script("arguments[0].scrollIntoView(true);", publish_btn)
    driver.execute_script("arguments[0].click();", publish_btn)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(CLoc.MY_ADS_HEADER))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CLoc.AVATAR_BTN)).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(CLoc.PROFILE_HEADER))

    assert "Новый товар" in driver.page_source
    driver.quit()