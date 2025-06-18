from selenium.webdriver.common.by import By

class RegistrationLocators:
    LOGIN_BTN = (By.XPATH, "//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")
    USERNAME_TEXT = (By.CSS_SELECTOR, "h3.profileText.name")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Войти']")

class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Войти']")

class CreatePostLocators:
    POST_BTN = (By.XPATH, "//button[text()='Разместить объявление']")
    FORM_TITLE = (By.XPATH, "//h1[contains(text(), 'Новое объявление')]")
    NAME_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")

    OPEN_DROP_DOWN_CITY = (By.XPATH, ".//div[contains(@class, 'dropDownMenu_input__itKtw') and contains(@style, '760px')]/button")
    CITY_OPTIONS = (By.XPATH, ".//div[contains(@class, 'dropDownMenu_dropMenu__sBxhz') and contains(@style, '760px')]/*[@class = 'dropDownMenu_options__CmHmm']")
    CITY_OPTION_MSK = (By.XPATH, ".//*[@class='undefined dropDownMenu_textColor__Nyo8k' and text() = 'Москва']")

    CONDITION_NEW_RADIO = (By.XPATH, "//input[@type='radio' and @value='Новый']")
    PUBLISH_BTN = (By.XPATH, "//button[text()='Опубликовать']")
    MY_ADS_HEADER = (By.XPATH, "//h2[text()='Мои объявления']")
    AVATAR_BTN = (By.CLASS_NAME, "avatar__container")
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")
    MODAL_AUTH_HEADER = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление')]")