from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login_as_standard_user(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def add_required_items(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
         ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def complete_checkout(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()

        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("0123")
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.presence_of_element_located
            ((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
