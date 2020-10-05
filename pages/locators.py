from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_VIEWING_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    BASKET_PRODUCT_ITEM = (By.XPATH, "//div[@class='basket-items']//div[@class='row']")
    EMPTY_BASKET_TEXT = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_FIELD = (By.XPATH, "//input[@id='id_registration-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    REGISTER_NOTIFICATION = (By.XPATH, "//div[contains(text(),'Thanks for registering!')]")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")
    ADD_ALERT = (By.XPATH, "//strong")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]")
