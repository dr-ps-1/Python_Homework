import pytest
from selenium import webdriver
from lesson_7_class_shop import ShopPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_saucedemo_checkout(driver):
    page = ShopPage(driver)

    page.login_as_standard_user()
    page.add_required_items()
    page.complete_checkout()

    total = page.get_total_price()

    assert "58.29" in total, f"Ожидалась сумма $58.29, получено {total}"
