from selenium.webdriver import Keys

from locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        #my_account page elements
        self.username_input = locators.MyAccountPage.username_input
        self.password_input = locators.MyAccountPage.password_input
        self.reg_email_input = locators.MyAccountPage.reg_email_input
        self.reg_password_input = locators.MyAccountPage.reg_password_input
        self.logout_link = locators.MyAccountPage.logout_link
        self.myaccount_link = locators.MyAccountPage.myaccount_link
        self.error_msg = locators.MyAccountPage.error_msg

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/")
        self.driver.find_element(self.myaccount_link).click()

    def log_in(self, username, password):
        self.driver.find_element(self.username_input).send_keys(username)
        self.driver.find_element(self.password_input).send_keys(password)
        self.driver.find_element(self.password_input).send_keys(Keys.ENTER)

    def create_account(self, reg_email, reg_password):
        self.driver.find_element(self.reg_email_input).send_keys(reg_email)
        self.driver.find_element(self.reg_password_input).send_keys(reg_password)
        self.driver.find_element(self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(self.error_msg).text




