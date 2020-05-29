from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):

        """Метод добавления в корзину"""

        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_should_be_added(self, product_name_taking):

        """Метод проверки добавления в корзину"""

        self.guest_can_add_product_to_basket()
        text = self.browser.find_element(*ProductPageLocators.ADD_ALERT).text
        pr_n = product_name_taking()
        assert pr_n in text

    def basket_should_be_increased(self, product_price_taking):

        """Метод проверки равности стоимости товара и стоимости корзины"""

        self.guest_can_add_product_to_basket()
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        bk_p = basket_price
        pr_p = product_price_taking()
        assert (bk_p == pr_p), 'Стоимость товара и корзины отличаются!'

    def product_name_taking(self):

        """Метод возвращающий наименование товара на странице товара"""

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def product_price_taking(self):

        """Метод возвращающий цену товара на странице товара"""

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

