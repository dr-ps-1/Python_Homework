import pytest
from selenium import webdriver
from lesson_7_class_calculator import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    page = CalculatorPage(driver)
    page.set_delay("45")
    page.calculate()
    results = page.get_result()

    assert results == "15", f"Ожидался результат 15, получено {results}"
