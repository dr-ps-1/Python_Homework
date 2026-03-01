import pytest
from selenium import webdriver
from lesson_10_ClassCalcAllure import CalculatorPage
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора: 7 + 8 = 15")
@allure.description(
    "Тест проверяет корректность работы калькулятора c задержкой 45 секунд."
    )
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет вычисление 7 + 8 с установленной задержкой.
    """
    page = CalculatorPage(driver)

    with allure.step("Установка задержки 45 секунд"):
        page.set_delay("45")

    with allure.step("Выполнение вычисления 7 + 8"):
        page.calculate()

    with allure.step("Получение результата"):
        results = page.get_result()

    with allure.step("Проверка, что результат равен 15"):
        assert results == "15", f"Ожидался результат 15, получено {results}"
