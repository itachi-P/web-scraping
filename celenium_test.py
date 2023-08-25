from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
time.sleep(3)

# Open Chrome browser -> Access Google.com -> Close after 3 seconds.
driver.close()