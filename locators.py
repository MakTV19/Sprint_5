
from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_REG_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'modal')]//h2")

class AuthPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    REPEAT_PASSWORD_FIELD = (By.NAME, "confirmPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Ошибка')]")

class UserInfoLocators:
    USER_AVATAR = (By.XPATH, "//img[@alt='User Avatar']")
    USER_NAME = (By.XPATH, "//span[text()='User']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

class AdCreationLocators:
    TITLE_FIELD = (By.NAME, "title")
    DESCRIPTION_FIELD = (By.NAME, "description")
    PRICE_FIELD = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    CONDITION_RADIO_NEW = (By.XPATH, "//input[@value='new']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    MY_ADS_BLOCK = (By.XPATH, "//h2[text()='Мои объявления']")
    CREATED_AD_TITLE = (By.XPATH, "//h3[text()='Test Product']")
