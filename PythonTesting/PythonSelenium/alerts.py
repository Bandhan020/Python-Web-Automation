import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#invoking chrome driver
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Rahul")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()
time.sleep(2)
assert "Rahul" in alertText
#alert.dismiss()

