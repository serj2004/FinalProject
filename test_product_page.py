from .pages.product_page import ProductPage
from .pages.base_page import BasePage


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.solve_quiz_and_get_code()


# def test_product_name_taking():
#     pass
#
#
# def test_product_price_taking():
#     pass


def test_product_should_be_added(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    bk_p = page.product_name_taking()
    page.product_should_be_added(bk_p)


def test_basket_should_be_increased(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    pr_p = page.product_price_taking()
    page.basket_should_be_increased(pr_p)
