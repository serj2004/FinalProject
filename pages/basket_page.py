from base_page import BasePage
from locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_products_in_the_basket(self):
        product_quantity = self.browser.find_element(*BasketPageLocators.BASKET_PRODUCT_QUANTITY).text()
        assert product_quantity == 0

    def should_be_text_that_basket_is_empty(self):
        empty_basket_info = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text()
        return empty_basket_info
