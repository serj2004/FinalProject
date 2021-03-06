from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "login substring is not presented in login url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # регистрация пользователя
        f = faker.Faker()
        email = f.email()
        password = f.password()
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password[0:9])
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        # register_notification = self.browser.find_element(*LoginPageLocators.REGISTER_NOTIFICATION)
        # assert "Thanks for registering!" in register_notification
