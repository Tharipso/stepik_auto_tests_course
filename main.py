import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
time.sleep(1)

browser.get("https://suninjuly.github.io/execute_script.html")

x = int(browser.find_element(By.ID, "input_value").text)
print(x)

y = str(math.log(abs(12*math.sin(int(x)))))
print(y)


textarea = browser.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)

people_radio = browser.find_element(By.ID, "peopleRule")

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)


option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

print(browser.switch_to.alert.text.split()[-1])
time.sleep(20)

browser.quit()

