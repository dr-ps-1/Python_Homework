from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

WebDriverWait(driver, 20).until(
    lambda driver: len(
        driver.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4
)

image_container = driver.find_element(By.ID, "image-container")
third_image = image_container.find_elements(By.TAG_NAME, "img")[2]
src_attribute = third_image.get_attribute("src")


print(f"{src_attribute}")

driver.quit()
