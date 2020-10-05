import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    # @pytest.mark.parametrize('link', [
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    #                                   ])

    @pytest.fixture(scope="function", autouse=True, BasePage, LoginPage)
    def setup(self):
        page1 = LoginPage()
        page2 = BasePage()
        page1.register_new_user()
        page2.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, link):
        page = ProductPage(browser, link)
        page.open()
        page.guest_can_add_product_to_basket()
        page.solve_quiz_and_get_code()

    def test_user_cant_see_success_message(self):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                               "?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_product_should_be_added(browser, link):
    page = ProductPage(browser, link)
    page.open()
    pr_n = page.product_name_taking()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    alert_text = page.product_should_be_added()
    assert pr_n == alert_text


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_basket_should_be_increased(browser, link):
    page = ProductPage(browser, link)
    page.open()
    pr_p: str = page.product_price_taking()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    bk_p: str = page.basket_should_be_increased()
    if page.cart_and_product_comparison(pr_p, bk_p):
        print("Цена " + pr_p + " равна " + bk_p)
    else:
        print("Цены не равны!")


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_no_products_in_the_basket()
    basket_page.should_be_text_that_basket_is_empty()
