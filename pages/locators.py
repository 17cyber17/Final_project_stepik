from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK =(By.CSS_SELECTOR,".btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name = registration-email]")
    PASSWORD_INPUT1 = (By.CSS_SELECTOR, "[name = registration-password1]") 
    PASSWORD_INPUT2 = (By.CSS_SELECTOR, "[name = registration-password2]")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name = registration_submit]")

class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasketPageLocators():
    PRODUCT_SECTION = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")