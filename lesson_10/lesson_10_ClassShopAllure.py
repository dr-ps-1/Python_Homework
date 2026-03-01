from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:
    """
    Page Object для работы со страницами интернет-магазина SauceDemo.
    """

    def __init__(self, driver):
        """
        Конструктор класса ShopPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Авторизация под стандартным пользователем")
    def login_as_standard_user(self):
        """
        Выполняет вход в систему под учетной записью standart_user.
        """
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_required_items(self):
        """
        Добавляет в корзину три товара:
        Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
         ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    @allure.step("Оформление заказа")
    def complete_checkout(self):
        """
        Выполняет процесс оформления заказа:
        переход в корзину, заполнение данных, продолжение.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()

        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("0123")
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы")
    def get_total_price(self):
        """
        Ожидает появления итоговой суммы на странице и возвращает ее.

        :return: str - текст с итоговой суммой (например, 'Total: $58.29')
        """
        total_element = self.wait.until(
            EC.presence_of_element_located
            ((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
