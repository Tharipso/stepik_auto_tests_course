from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/redirect_accept.html")
browser.find_element(By.CSS_SELECTOR, ".btn").click()

browser.switch_to.window(browser.window_handles[1])

x = int(browser.find_element(By.ID, "input_value").text)
print(x)

y = str(math.log(abs(12*math.sin(int(x)))))
textarea = browser.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
submit_button.click()




print(browser.switch_to.alert.text.split()[-1])
browser.quit()
