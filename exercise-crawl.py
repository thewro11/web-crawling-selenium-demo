from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import config

# create browser options
options = Options()
options.binary_location = config.BROWSER_BINARY_LOCATION

# create Chrome services
s = Service(config.BROWSER_DRIVER)

# create Chrome webdriver
chrome = webdriver.Chrome(service=s, options=options)

# implicitly wait until chome finds the element or timeout by the time limit you specified (in seconds)
chrome.implicitly_wait(5)

# specify browser
url = "https://www.google.com/"
chrome.get(url)

searchBarElement = chrome.find_element(By.ID, "APjFqb")
searchBarElement.send_keys("National Central University")
searchBarElement.send_keys(Keys.ENTER)

results = chrome.find_elements(By.CLASS_NAME, "MjjYud")

for result in results:
    print(result.text, end="\n------------------------\n\n")

# close browser
chrome.close()
