import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#invoking chrome driver
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


"""
XPATH syntax:
//tagname[@attribute='value'] -> "//input[@type='submit']"

CSS
tagname[attribute='value']
if you have id, then #id also comes as CSS selector
if you have classname, then .classname also considered as valid CSS selector

"""

time.sleep(2)