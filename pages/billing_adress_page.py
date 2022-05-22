from selenium.webdriver.support.select import Select
from locators.locators import BillingAdressLocators


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        # Billing Address Page elements
        self.address_link = BillingAdressLocators.address_link
        self.edit_link = BillingAdressLocators.edit_link
        self.first_name_input = BillingAdressLocators.first_name_input
        self.last_name_input = BillingAdressLocators.last_name_input
        self.company_input = BillingAdressLocators.company_input
        self.country_select = BillingAdressLocators.country_select
        self.address_1_input = BillingAdressLocators.address_1_input
        self.postcode_input = BillingAdressLocators.postcode_input
        self.city_input = BillingAdressLocators.city_input
        self.phone_input = BillingAdressLocators.phone_input
        self.save_address_btn = BillingAdressLocators.save_address_btn
        self.message_div = BillingAdressLocators.message_div

    def open_edit_billing_address(self):
        self.driver.find_element(*self.address_link).click()
        self.driver.find_element(*self.edit_link).click()

    def set_personal_data(self, firstname, lastname):
        self.driver.find_element(*self.first_name_input).send_keys(firstname)
        self.driver.find_element(*self.last_name_input).send_keys(lastname)

    def set_company_name(self, company_name):
        self.driver.find_element(*self.company_input).send_keys(company_name)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.address_1_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def save_address(self):
        self.driver.find_element(*self.save_address_btn).click()

    def get_upgrade_msg(self):
        return self.driver.find_element(*self.message_div).text
