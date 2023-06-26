from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from bs4 import BeautifulSoup


path = "./chromedriver.exe"
driver = webdriver.Chrome(service=Service(path))

url1 = "https://visa.vfsglobal.com/ind/en/pol/login"
def scrapData(url, email, password):
    driver.get(url)
    time.sleep(8)
    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(email)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/app-root/div/app-login/section/div/div/mat-card/form/button').click()
    time.sleep(8)
email = "vfspoland5@explodemail.com"
password = "Test123@"

scrapData(url1, email, password)
driver.quit()