import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver() -> Generator[WebDriver, None, None]:
    """
    Один браузер на всю UI-сессию
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
