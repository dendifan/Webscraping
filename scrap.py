from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from bs4 import BeautifulSoup


path = "./chromedriver.exe"
driver = webdriver.Chrome(service=Service(path))

url1 = "https://www.pinksale.finance/launchpad/0x148c295B7EE3A854d0dCD37dD10B7994c920f55B?chain=ETH"
url2 = "https://www.pinksale.finance/launchpad/0x9f39D96d22da1e00bF1B6573fDDF9a12DAB7E3E7?chain=BSC"
def scrapData(url):
    driver.get(url)
    time.sleep(3)
    projectName = driver.find_element(By.XPATH, '//*[@id="root"]/section/section/main/div[2]/div[1]/div[1]/div[1]/div/article/div[2]/div[1]/div[1]/div/h1').text
    print("project name is: ", projectName)

scrapData(url1)
scrapData(url2)

driver.quit()