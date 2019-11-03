from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def Check_that_the_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_SECTION), "There is a product in the basket"

    def should_be_basket_empty_block(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), \
        "A block with the text that the basket is empty is missing"

    def Check_if_there_is_a_text_saying_that_basket_is_empty(self):
       text_basket_empty =  self.browser.find_element(*BasketPageLocators.TEXT_BASKET_EMPTY).text
       assert text_basket_empty == "Your basket is empty. Continue shopping", "The text that the basket is empty does not match"