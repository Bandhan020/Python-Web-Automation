import time
from selenium import webdriver

#invoking chrome driver
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)

#with using chrome driver
"""
import time

from selenium import selenium
from selenium.webdriver.chrome.service import Service

service obj= Service("path to chrome driver")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://google.com")

[note: for edge or firefox, you have to import related service and in same way related path for related driver]

"""