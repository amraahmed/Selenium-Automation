from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.get("http://automated.pythonanywhere.com")
    
    return driver


def get_only_temp(text:str):
    output = float(text.split(": ")[1])
    return output



def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[2]")
    return get_only_temp(element.text)


print("Scrapped world's Average temp is ",main())