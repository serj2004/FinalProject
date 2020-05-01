from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")
    ADD_ALERT = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/strong[1]")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/strong[1]")
    PRODUCT_NAME = (By.XPATH, "//h1")
