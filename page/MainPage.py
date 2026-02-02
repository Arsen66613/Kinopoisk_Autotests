import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Page Object страницы 'Фильмы в кино'
    """

    # ===== ЯКОРЬ СТРАНИЦЫ =====

    MOVIE_LIST = (
        By.XPATH,
        "//div[contains(@class, 'styles_root')]"
    )

    # ===== ССЫЛКИ-ФИЛЬТРЫ =====

    HIGH_RATING = (
        By.XPATH,
        "//a[contains(@href, 'high_rated')]"
    )

    RUSSIAN_MOVIES = (
        By.XPATH,
        "//a[contains(@href, 'b=russian')]"
    )

    FOREIGN_MOVIES = (
        By.XPATH,
        "//a[contains(@href, 'b=foreign')]"
    )

    # ===== СЕЛЕКТЫ =====

    GENRE_SELECT = (
        By.XPATH,
        "//span[text()='Все жанры' or text()='Аниме']"
        "/ancestor::div[contains(@class, 'selectButton')]"
    )

    CITY_SELECT = (
        By.XPATH,
        "//span[contains(text(), 'Москва') or contains(text(), 'Абакан')]"
        "/ancestor::div[contains(@class, 'selectButton')]"
    )

    CHECKBOX_OPTION = (
        By.XPATH,
        "//label[.//span[text()='{value}']]"
    )

    SELECTED_GENRE_TEXT = (
        By.XPATH,
        "//span[contains(@class, 'buttonCaption')][text()='Аниме']"
    )

    SELECTED_CITY_TEXT = (
        By.XPATH,
        "//span[contains(@class, 'buttonCaption')][text()='Абакан']"
    )

    # ===== КОНСТРУКТОР =====

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ===== БАЗОВЫЕ МЕТОДЫ =====

    @allure.step("Открыть страницу фильмов в кино")
    def open(self, url: str) -> None:
        self.driver.get(url)
        self.wait_page_loaded()

    @allure.step("Дождаться загрузки списка фильмов")
    def wait_page_loaded(self) -> None:
        self.wait.until(
            EC.presence_of_element_located(self.MOVIE_LIST)
        )

    # ===== ФИЛЬТРЫ =====

    @allure.step("Фильтрация: с высоким рейтингом")
    def filter_by_rating(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.HIGH_RATING)
        ).click()
        self.wait_page_loaded()

    @allure.step("Фильтрация: российские фильмы")
    def filter_russian_movies(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.RUSSIAN_MOVIES)
        ).click()
        self.wait_page_loaded()

    @allure.step("Фильтрация по жанру: {genre}")
    def filter_by_genre(self, genre: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.GENRE_SELECT)
        ).click()

        option = (
            self.CHECKBOX_OPTION[0],
            self.CHECKBOX_OPTION[1].format(value=genre)
        )

        self.wait.until(
            EC.element_to_be_clickable(option)
        ).click()

        self.wait_page_loaded()

    @allure.step("Фильтрация по городу: {city}")
    def filter_by_city(self, city: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.CITY_SELECT)
        ).click()

        option = (
            self.CHECKBOX_OPTION[0],
            self.CHECKBOX_OPTION[1].format(value=city)
        )

        self.wait.until(
            EC.element_to_be_clickable(option)
        ).click()

        self.wait_page_loaded()

    # ===== ГЕТТЕРЫ =====

    @allure.step("Получить выбранный жанр")
    def get_selected_genre(self) -> str:
        element = self.wait.until(
            EC.presence_of_element_located(
                self.SELECTED_GENRE_TEXT
            )
        )
        return element.text

    @allure.step("Получить выбранный город")
    def get_selected_city(self) -> str:
        element = self.wait.until(
            EC.presence_of_element_located(
                self.SELECTED_CITY_TEXT
            )
        )
        return element.text
