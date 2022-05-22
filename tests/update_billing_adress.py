import random
import allure
import pytest
from pages.billing_adress_page import BillingAddressPage
from pages.myaccount_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpgradeBillingAddress:

    @allure.title("Test - update billing address successfully")
    @allure.description("Automation testing using Selenium with page object pattern")
    def test_update_billing_address(self):
        email = "anna_nowak" + str(random.randint(0, 10000)) + "@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "Passworld1234!")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("Anna", "Nowak")
        billing_address_page.set_company_name("Tester")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Nowa 1", "00-001", "Warsaw")
        billing_address_page.set_phone_number("500-001-002")
        billing_address_page.save_address()

        msg = "Address changed successfully."
        assert msg in billing_address_page.get_upgrade_msg()
