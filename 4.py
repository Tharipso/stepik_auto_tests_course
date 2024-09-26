from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = browser.find_element(By.ID, "price")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), text_="100"))


browser.find_element(By.ID, "book").click()

x = int(browser.find_element(By.ID, "input_value").text)
print(x)

y = str(math.log(abs(12*math.sin(int(x)))))
textarea = browser.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
submit_button.click()



print(browser.switch_to.alert.text.split()[-1])
browser.quit()
