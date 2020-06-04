
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):

    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()


def test_product_should_be_added(browser):

    page = ProductPage(browser, link)
    page.open()
    pr_n = page.product_name_taking()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    alert_text = page.product_should_be_added()
    assert pr_n in alert_text


def test_basket_should_be_increased(browser):

    page = ProductPage(browser, link)
    page.open()
    pr_p = page.product_price_taking()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    bk_p = page.basket_should_be_increased()
    print("Это цена корзины: " + str(bk_p))
    print("Это цена товара: " + str(pr_p))
    assert (bk_p == pr_p), 'Стоимость товара и корзины отличаются!'


