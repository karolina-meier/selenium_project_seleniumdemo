from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random


def test_update_billing_adress():
    email = "anna_nowak" + str(random.randint(0,10000)) + "@gmail.com"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("Passworld1234!")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Anna")
    driver.find_element(By.ID, "billing_last_name").send_keys("Nowak")
    driver.find_element(By.ID, "billing_company").send_keys("Tester")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Nowa 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-001")
    driver.find_element(By.ID, "billing_city").send_keys("Warsaw")
    driver.find_element(By.ID, "billing_phone").send_keys("500-001-002")
    driver.find_element(By.NAME, "save_address").click()

    assert "Address changed successfully" in driver.find_element(By.XPATH, "//div[@class = 'woocommerce-message']").text

