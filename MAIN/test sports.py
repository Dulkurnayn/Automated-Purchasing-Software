from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time
#

try:
    item = "air max 95 men"
    #index =fra

    chrome_options = webdriver.ChromeOptions()
    
    browser = webdriver.Chrome(options=chrome_options)

    browser.get('https://www.sportsdirect.com/')

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
    browser.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()
    time.sleep(3)
    search_box=browser.find_element(By.ID, 'txtSearch')

    search_box.send_keys(item)
    time.sleep(2)  # Replace "shoe" with the actual shoe name you're looking for
    search_box.submit()
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR, 'li:nth-child(1) .rtimg').click()
    time.sleep(4)
    browser.find_element(By.LINK_TEXT, '8 (42.5)').click()
    time.sleep(7)
    browser.find_element(By.CSS_SELECTOR, '#ProductStandardAddToBag .addToBagInner').click()
    
    #id="aAddToBag"
    #self.update_status(0, "basket")
    time.sleep(4)
    browser.find_element(By.ID, 'aCheckout').click()
    #current_thread = threading.current_thread()
    #print(f"My function is running on thread: {current_thread.name}")
    #self.purchase_app_instance = PurchaseApp
    #self.user_info_frame
    #self.update_status(0, "checkout")
    

    time.sleep(3)
    #print(user_details[First_Name])
    browser.find_element(By.CSS_SELECTOR, '#Login_EmailAddress').send_keys('mustafashakil6@gmail.com')
    time.sleep(3)
        # browser.find_element(By.CSS_SELECTOR, css='#Login_EmailAddress').send_keys('mustafashakil6@gmail.com')
    #email_entry.submit()
    browser.find_element(By.CSS_SELECTOR, '.formCompleteCTA > button').click()
    time.sleep(2)
    WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.LINK_TEXT,'No thanks, continue without signing in')))
    browser.find_element(By.LINK_TEXT,'No thanks, continue without signing in').click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, '.singleLine span').click()
    time.sleep(2)
    
    browser.find_element(By.CSS_SELECTOR, '.formCompleteCTA > button').click()
    time.sleep(2)
    browser.find_element(By.ID,'firstName').click()
    browser.find_element(By.ID,'firstName').send_keys('name')
    time.sleep(3)
    browser.find_element(By.ID,'lastName').click()
    browser.find_element(By.ID,'lastName').send_keys('sename')
    time.sleep(3)
    browser.find_element(By.ID,'contactNumber').send_keys('38338')

    time.sleep(3)
    
    browser.find_element(By.ID,'line1').click()
    browser.find_element(By.ID, 'line1').send_keys('17 Rosebery Street liverpool' )
    time.sleep(100)
except Exception as e:
    print(f"Error testing proxy {proxy_url}: {str(e)}")

def suggest_new_items(suggests):
    chrome_options = webdriver.ChromeOptions()
    
    browser = webdriver.Chrome(options=chrome_options)

    browser.get('s')

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
    browser.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()
    time.sleep(3)
    print("")
   
