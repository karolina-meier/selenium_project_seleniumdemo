from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

def test_create_account_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("anna_nowak@gmail.com")
    driver.find_element(By.ID, "reg_password").send_keys("Passworld1234!")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    msg = "An account is already registered with your email address. Please log in."
    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text


def test_create_account_passed():
    email = "anna_nowak" + str(random.randint(0,10000)) + "@gmail.com"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("Passworld1234!")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


