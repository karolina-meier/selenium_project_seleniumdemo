from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_log_in_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("anna_nowak@gmail.com")
    #using javascript - scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "password"))
    driver.find_element(By.ID, "password").send_keys("Passworld1234!")
    driver.find_element(By.NAME, "login").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

def test_log_in_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("anna_nowak@gmail.com")
    driver.find_element(By.ID, "password").send_keys("PassListt1234!")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    assert "ERROR: Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
    



