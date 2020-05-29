from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):

        """Метод выполняющий добавление в корзину"""

        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_should_be_added(self):

        """Метод возвращающий текст сообщения о добавлении товара в корзину"""

        alert_text = self.browser.find_element(*ProductPageLocators.ADD_ALERT)
        return alert_text.text

    def basket_should_be_increased(self):

        """Метод возвращающий стоимость корзины"""

        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        return basket_price.text

    def product_name_taking(self):

        """Метод возвращающий наименование товара на странице товара"""

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def product_price_taking(self):

        """Метод возвращающий цену товара на странице товара"""

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

