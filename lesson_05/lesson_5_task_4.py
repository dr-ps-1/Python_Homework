from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get(" http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
time.sleep(3)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
time.sleep(3)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type ='submit']")
login_button.click()
time.sleep(3)

success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print(success_message.text)


time.sleep(1)

driver.quit()
