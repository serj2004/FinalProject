from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_ALERT = (By.CLASS_NAME, "alertinner ")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    BASKET_PRICE = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/strong[1]")
