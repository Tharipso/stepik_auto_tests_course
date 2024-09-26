from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("qwe")
browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("qwe")
browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("qwe")




current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')
print(file_path)

browser.find_element(By.CSS_SELECTOR, "[name='file']").send_keys(file_path)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()



print(browser.switch_to.alert.text.split()[-1])
browser.quit()

