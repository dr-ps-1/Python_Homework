from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("  http://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

time.sleep(1)

driver.quit()
