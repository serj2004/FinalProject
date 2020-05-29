from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):

        """Метод добавления в корзину"""

        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_should_be_added(self, product_name_taking):

        """Метод возвращающий текст сообщения о добавлении товара в корзину """

        text = self.browser.find_element(*ProductPageLocators.ADD_ALERT).text
        return text

    def basket_should_be_increased(self, product_price_taking):

        """Метод возвращающий цену корзины"""

        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return basket_price

    def product_name_taking(self):

        """Метод возвращающий наименование товара на странице товара"""

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def product_price_taking(self):

        """Метод возвращающий цену товара на странице товара"""

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

