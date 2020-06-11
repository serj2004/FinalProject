from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):

        """Метод добавления в корзину"""

        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_should_be_added(self):

        """Метод возвращающий текст сообщения о добавлении товара в корзину """

        text = self.browser.find_elements(*ProductPageLocators.ADD_ALERT)[-3]
        return text.text

    def basket_should_be_increased(self):

        """Метод возвращающий цену корзины"""

        basket_price = self.browser.find_elements(*ProductPageLocators.BASKET_PRICE)[-1]
        return basket_price.text

    def product_name_taking(self):

        """Метод возвращающий наименование товара на странице товара"""

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def product_price_taking(self):

        """Метод возвращающий цену товара на странице товара"""

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def cart_and_product_comparison(self, pr_p: str, bk_p: str) -> bool:

        """Метод проверяющий равенство цены товара и цены корзины"""

        return pr_p == bk_p

    def should_not_be_success_message(self):

        """Метод проверяющий отсутствие сообщения о добавлении товара в корзину"""

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        """Метод проверяющий исчезновение сообщения о добавлении товара в корзину"""

        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


