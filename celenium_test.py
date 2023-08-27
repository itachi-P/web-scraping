from selenium import webdriver

# ChromeDriverにパスが通っていれば不要
#import chromedriver_binary
import time

driver = webdriver.Chrome()
driver.get('https://dev.to')
time.sleep(3)

# Open Chrome browser -> Access Google.com -> Close after 3 seconds.
driver.close()