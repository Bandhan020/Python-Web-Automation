import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#invoking chrome driver
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#LinkText can also be used as locator
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("raihansultan05@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
"""
xpath in respect of parent and child
//tagname/child[no.]/type -> //form/div[1]/input
for css, same format, just in space of '/' there will be ' '(space), and child should be written as nth-child(child no.) followed by a ':'
for instance "form div:nth-child(2) input"

If you don't have anything for locator, then you can use text to make xpath

"""
