from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_ITEM)

    def should_be_text_that_basket_is_empty(self):
        empty_basket_info = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty." in empty_basket_info
