from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):
        """Метод добавления в корзину"""
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_should_be_added(self):
        """Метод проверки добавления в корзину"""
        text = self.browser.find_element(*ProductPageLocators.ADD_ALERT).text
        assert "The shellcoder's handbook был добавлен в вашу корзину." in text

    def basket_should_increased(self):
        """Метод проверки равности стоимости товара и стоимости корзины"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price in basket_price, 'Стоимость товара и корзины отличаются!'

