import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.musinsa.com/snap/1237570978707323432')
time.sleep(3)

texts = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div[3]/div/div/div/div[1]/div/div[5]/div')

print(texts)