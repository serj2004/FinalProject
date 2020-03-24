from .locators import ProductPageLocators


class ProductPage:

    """Метод добавления в корзину"""
    def guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(ProductPageLocators.ADD_BUTTON)
        add_button.click()