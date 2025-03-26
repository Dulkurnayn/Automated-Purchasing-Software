from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = webdriver.ChromeOptions()
email = "air max 95 men"
password = "#"
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.sportsdirect.com/')
#time.sleep(40)
#browser.find_element(
#   By.CSS_SELECTOR, 'onetrust-accept-btn-handler').click()
# browser.find_element(By.ID,"id=HeaderSearch_search_query").send_keys(email)
WebDriverWait(browser, 10).until(
EC.visibility_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
browser.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()
time.sleep(7)
search_box=browser.find_element(By.ID, 'txtSearch')

search_box.send_keys(email)
time.sleep(2)  # Replace "shoe" with the actual shoe name you're looking for
search_box.submit()
time.sleep(4)
browser.find_element(By.CSS_SELECTOR, 'li:nth-child(1) .rtimg').click()
time.sleep(4)
browser.find_element(By.LINK_TEXT, '8 (42.5)').click()
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, '#ProductStandardAddToBag .addToBagInner').click()
#id="aAddToBag"
time.sleep(4)
browser.find_element(By.ID, 'aCheckout').click()


time.sleep(499)