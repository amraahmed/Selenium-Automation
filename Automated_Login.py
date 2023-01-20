from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Setting options to make browsing easier
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument('start-maxmized')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    
    return driver


def main():
    driver = get_driver()
    driver.find_element(By.ID,value='id_username').send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID,value='id_password').send_keys("automatedautomated"+Keys.RETURN)
    time.sleep(2)

print(main())