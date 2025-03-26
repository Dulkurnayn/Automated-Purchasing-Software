from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument(f'--proxy-server=http://147.161.237.88')
    #chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    #chrome_options.add_argument('--enable-logging')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://myexternalip.com/raw")
driver.implicitly_wait(250)
time.sleep(400)
#visual_search_input = driver.find_element(By.ID,"VisualSearchInput")

#visual_search_input.click()
#search_box.send_keys("FJ7098-301")  # Replace "shoe" with the actual shoe name you're looking for
#search_box.send_keys(Keys.RETURN)

# Wait for the search results page to load
#driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to appear

# You can now interact with the search results page, for example, click on a specific shoe
# For instance, let's click on the first search result
#first_search_result = driver.find_element_by_css_selector(".product-card:first-child a")
#first_search_result.click()

driver.quit()
#get mac address and bind liscence

with open('/sys/class/net/eth0/address') as f:
    mac = f.read()
    print (mac)
    print (random.randint)