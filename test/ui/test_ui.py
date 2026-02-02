import json
import pytest
import allure

from selenium.webdriver.remote.webdriver import WebDriver

from configuration.ConfigProvider import ConfigProvider
from page.AuthPage import AuthPage
from page.MainPage import MainPage


@allure.epic("UI")
@pytest.mark.ui
class TestKinopoiskUI:
    """
    UI-тесты Kinopoisk: авторизация и фильтрация фильмов
    """

    @allure.title("Авторизация на сайте")
    @allure.story("UI Авторизация")
    def test_ui_auth(self, driver: WebDriver) -> None:
        auth_url: str = ConfigProvider.get(
            "ui",
            "auth_url"
        )

        with open("test_data.json", encoding="utf-8") as file:
            data = json.load(file)

        auth_page = AuthPage(driver)

        auth_page.open(auth_url)
        auth_page.enter_login(data["login"])
        auth_page.click_login_next()
        auth_page.click_login_with_password()
        auth_page.enter_password(data["password"])
        auth_page.click_password_next()
        auth_page.assert_user_authorized()

    @allure.title("Фильтрация фильмов с высоким рейтингом")
    @allure.story("UI Фильтры")
    def test_ui_filter_by_rating(self, driver: WebDriver) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_by_rating()

        assert "high_rated" in driver.current_url

    @allure.title("Фильтрация фильмов по стране: российские")
    @allure.story("UI Фильтры")
    def test_ui_filter_by_country(self, driver: WebDriver) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_russian_movies()

        assert "b=russian" in driver.current_url

    @allure.title("Фильтрация фильмов по жанру: Аниме")
    @allure.story("UI Фильтры")
    def test_ui_filter_by_genre(self, driver: WebDriver) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_by_genre("Аниме")

        assert page.get_selected_genre() == "Аниме"

    @allure.title("Фильтрация фильмов по городу: Абакан")
    @allure.story("UI Фильтры")
    def test_ui_filter_by_city(self, driver: WebDriver) -> None:
        page = MainPage(driver)

        page.open(
            ConfigProvider.get(
                "ui",
                "movies_url"
            )
        )
        page.filter_by_city("Абакан")

        assert page.get_selected_city() == "Абакан"
