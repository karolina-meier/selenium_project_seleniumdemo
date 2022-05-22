import pytest
from pages.myaccount_page import MyAccountPage

@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_accout_page = MyAccountPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.log_in("anna_nowak@gmail.com", "Passworld1234!")

        assert my_accout_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_accout_page = MyAccountPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.log_in("anna_nowak@gmail.com", "PassListt1234!")

        assert "ERROR: Incorrect username or password." in my_accout_page.get_error_msg()
    



