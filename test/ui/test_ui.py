import pytest
import allure

from selenium.webdriver.remote.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider
from page.MainPage import MainPage


@allure.epic("UI")
@pytest.mark.ui
class TestKinopoiskUI:
    """
    UI-тесты фильтрации фильмов Kinopoisk
    """

    @allure.title(
        "Фильтрация фильмов по рейтингу"
    )
    @allure.story("UI Фильтры")
    def test_filter_by_rating(
        self,
        driver: WebDriver
    ) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_by_rating()

        with allure.step(
            "Проверка фильтра рейтинга в URL"
        ):
            assert "high_rated" in driver.current_url

    @allure.title(
        "Фильтрация фильмов по стране: российские"
    )
    @allure.story("UI Фильтры")
    def test_filter_russian_movies(
        self,
        driver: WebDriver
    ) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_russian_movies()

        with allure.step(
            "Проверка фильтра страны"
        ):
            assert "b=russian" in driver.current_url

    @allure.title(
        "Фильтрация фильмов по стране: зарубежные"
    )
    @allure.story("UI Фильтры")
    def test_filter_foreign_movies(
        self,
        driver: WebDriver
    ) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_foreign_movies()

        with allure.step(
            "Проверка фильтра страны"
        ):
            assert "b=foreign" in driver.current_url

    @allure.title(
        "Фильтрация фильмов по жанру: Аниме"
    )
    @allure.story("UI Фильтры")
    def test_filter_by_genre_anime(
        self,
        driver: WebDriver
    ) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_by_genre("Аниме")

        with allure.step(
            "Проверка выбранного жанра"
        ):
            assert page.get_selected_genre() == "Аниме"

    @allure.title(
        "Фильтрация фильмов по городу: Абакан"
    )
    @allure.story("UI Фильтры")
    def test_filter_by_city_abakan(
        self,
        driver: WebDriver
    ) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_by_city("Абакан")

        with allure.step(
            "Проверка выбранного города"
        ):
            assert page.get_selected_city() == "Абакан"
