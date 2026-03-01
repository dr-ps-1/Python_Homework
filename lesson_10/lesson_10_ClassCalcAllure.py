from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CalculatorPage:
    """
    Page Object для страницы калькулятора с задержкой.
    """

    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Установка задержки {delay_value} секунд")
    def set_delay(self, delay_value):
        """
        Устанавливает значение задержки перед вычислениями.

        :param delay_value: str - время задержки в секундах.
        """
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay_value)

    @allure.step("Выполнение вычисления 7 + 8")
    def calculate(self):
        """Нажимает кнопки 7, +, 8, = для выполнения сложения."""
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Ожидание результата и получение значения")
    def get_result(self):
        """
        Ожидает появления результата 15 на экране и возвращает его.

        :return: str - текст результата на экране калькулятора.
        """
        self.wait.until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".screen").
            text == "15"
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
