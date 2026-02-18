import pytest
from selenium import webdriver
from lesson_10_ClassShopAllure import ShopPage
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера Firefox.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Тестирование оформления заказа в интернет-магазине")
@allure.description(
    "Тест проверяет полный сценарий покупки трех товаров"
    "и проверяет итоговую сумму"
    )
@allure.feature("Интернет-магазин")
@allure.severity("allure.severity_level.BLOCKER")
def test_saucedemo_checkout(driver):
    """
    тест проверяет оформление заказа в интернет-магазине SauceDemo.
    """
    page = ShopPage(driver)

    with allure.step("Авторизация в системе"):
        page.login_as_standard_user()

    with allure.step("Добавление товаров в корзину"):
        page.add_required_items()

    with allure.step("Оформление заказа"):
        page.complete_checkout()

    with allure.step("Получение итоговой суммы"):
        total = page.get_total_price()

    with allure.step("проверка, что итоговая сумма содержит $58.29"):
        assert "58.29" in total, f"Ожидалась сумма $58.29, получено {total}"
