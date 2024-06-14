from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = 'C:\\Users\\aakas\\AppData\\Roaming\\Python\\Python39\\site-packages\\chromedriver_binary\\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Leetcode.com" + Keys.ENTER)

time.sleep(10)
driver.quit()
