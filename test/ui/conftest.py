import time
import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver() -> Generator[WebDriver, None, None]:
    """
    Один браузер на всю UI-сессию.
    При первом запуске даёт время на ручное
    прохождение капчи / антибот-проверки.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # ОДИН РАЗ — ожидание ручного прохождения капчи
    print(
        "\n[INFO] Если появилась капча / антибот — "
        "пройди её сейчас. Ожидание 50 секунд...\n"
    )
    time.sleep(50)

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def pause_between_ui_tests() -> Generator[None, None, None]:
    """
    Пауза между UI-тестами (4 секунды)
    """
    yield
    time.sleep(4)
