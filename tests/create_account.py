import random
import pytest

from pages.myaccount_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("anna_nowak@gmail.com", "Passworld1234!")

        msg = "An account is already registered with your email address. Please log in."
        assert msg in my_account_page.get_error_msg()

    def test_create_account_passed(self):
        email = "anna_nowak" + str(random.randint(0, 10000)) + "@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "Passworld1234!")

        assert my_account_page.is_logout_link_displayed()
