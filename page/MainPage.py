import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Page Object страницы "Фильмы в кино"
    """

    MOVIE_LIST = (
        By.XPATH,
        "//div[contains(@class, 'styles_root')]"
    )

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

    GENRE_SELECT = (
        By.XPATH,
        "//summary[.='Жанры']"
        "/following-sibling::div"
        "//span[contains(@class, 'buttonCaption')]"
    )

    CITY_SELECT = (
        By.XPATH,
        "//summary[.='Города']"
        "/following-sibling::div"
        "//span[contains(@class, 'buttonCaption')]"
    )

    CHECKBOX_OPTION = (
        By.XPATH,
        "//label[.//span[text()='{value}']]"
    )

    SELECTED_GENRE_TEXT = (
        By.XPATH,
        "//summary[.='Жанры']"
        "/following-sibling::div"
        "//span[contains(@class, 'buttonCaption')]"
    )

    SELECTED_CITY_TEXT = (
        By.XPATH,
        "//summary[.='Города']"
        "/following-sibling::div"
        "//span[contains(@class, 'buttonCaption')]"
    )

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Открыть страницу фильмов в кино")
    def open(self, url: str) -> None:
        self.driver.get(url)
        self.wait.until(
            EC.presence_of_element_located(
                self.MOVIE_LIST
            )
        )

    @allure.step("Фильтрация: фильмы с высоким рейтингом")
    def filter_by_rating(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(
                self.HIGH_RATING
            )
        ).click()

    @allure.step("Фильтрация: российские фильмы")
    def filter_russian_movies(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(
                self.RUSSIAN_MOVIES
            )
        ).click()

    @allure.step("Фильтрация: зарубежные фильмы")
    def filter_foreign_movies(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(
                self.FOREIGN_MOVIES
            )
        ).click()

    @allure.step("Фильтрация по жанру: {genre}")
    def filter_by_genre(self, genre: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable(
                self.GENRE_SELECT
            )
        ).click()

        option = (
            self.CHECKBOX_OPTION[0],
            self.CHECKBOX_OPTION[1].format(
                value=genre
            )
        )

        self.wait.until(
            EC.element_to_be_clickable(
                option
            )
        ).click()

    @allure.step("Фильтрация по городу: {city}")
    def filter_by_city(self, city: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable(
                self.CITY_SELECT
            )
        ).click()

        option = (
            self.CHECKBOX_OPTION[0],
            self.CHECKBOX_OPTION[1].format(
                value=city
            )
        )

        self.wait.until(
            EC.element_to_be_clickable(
                option
            )
        ).click()

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
