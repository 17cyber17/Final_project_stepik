from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login not contained in current browser url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FROM), "No login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "No register form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT1)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT2)
        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()