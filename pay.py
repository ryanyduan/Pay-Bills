from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common import keys
import pyautogui
import argparse

#==================================================================
# Set up webdriver and command line parser
#==================================================================
parser = argparse.ArgumentParser()
parser.add_argument("amount",type=int)
args = parser.parse_args()
amt = args.amount
driver = webdriver.Chrome()
wait = ui.WebDriverWait(driver,10)

#==================================================================
# Username and Passwords in a dictionary
#==================================================================

passwords = {"CIBC": ["USERNAME", "PASSWORD"]}

#==================================================================
# Log into credit card account and scrape how much money is owed
#==================================================================

#driver.get("https://www1.bmo.com/")

# wait.until(lambda driver: driver.find_element_by_name("FBC_Number"))
# wait.until(lambda driver: driver.find_element_by_name("FBC_Password"))

# BMO_USER = driver.find_element_by_name("FBC_Number")
# BMO_PASS = driver.find_element_by_name("FBC_Password")

# pyautogui.moveTo(320,550,duration=0.25)
# pyautogui.click(300,300)
# BMO_USER.send_keys(passwords['BMO'][0])
# BMO_PASS.send_keys(passwords['BMO'][1])

# pyautogui.moveTo(470,570,duration=0.1)
# pyautogui.click(470,570)
# pyautogui.click(470,570)

#==================================================================
# Log into bank account and pay credit owed
#==================================================================

driver.get("https://www.cibconline.cibc.com/ebm-resources/public/banking/cibc/client/web/index.html#/signon")
wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='row card-entry']//*[@name='cardNumber']"))
wait.until(lambda driver: driver.find_element_by_xpath("//*[@type='password']"))

CIBC_USER = driver.find_element_by_xpath("//div[@class='row card-entry']//*[@name='cardNumber']")
CIBC_PASS = driver.find_element_by_xpath("//*[@type='password']") 

CIBC_USER.send_keys(passwords['CIBC'][0])
CIBC_PASS.send_keys(passwords['CIBC'][1])

pyautogui.moveTo(300,567, duration=0.1)	
pyautogui.click(300,567)
pyautogui.click(300,567)

wait.until(lambda driver: driver.find_elements_by_link_text('Pay Bills'))

pyautogui.moveTo(180,680,duration=0.1)
pyautogui.click(180,680)

wait.until(lambda driver: driver.find_elements_by_class_name('ui-checkmark'))
pyautogui.moveTo(338,763, duration=0.25)
pyautogui.click(338,763)

AMOUNT = driver.find_element_by_name("amount")
AMOUNT.send_keys(amt)
