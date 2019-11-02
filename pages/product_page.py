from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BTN), "Missing add to basket button"

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_basket_total, "No product price in the message"

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def success_message_disappearance_check(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "success message did not disappear"