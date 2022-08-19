from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time

gutterdogs_url = "https://opensea.io/zh-CN/collection/gutterdogs"
try_url = 'https://opensea.io/zh-CN/assets?search[collections][0]=rareapepeyachtclub&search[collections][1]=8liens&search[resultModel]=BUNDLES'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(try_url)
time.sleep(random.randint(4,7))
previous_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, documnet.body.scrollHeight);')
    time.sleep(random.randint(4,7))

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == previous_height:
        break
    previous_height = new_height

driver.find_elements(By)
find_elements(By.TAG_NAME, 'img')

file = open('data/Try.html','w')
file.write(driver.page_source)
file.close()

driver.close()
