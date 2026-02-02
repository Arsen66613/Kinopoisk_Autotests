import pytest
import allure
from typing import Dict, Any
from api.KinopoiskApi import KinopoiskApi


@pytest.mark.api
@allure.epic("API тесты Kinopoisk")
class TestKinopoiskApi:

    @pytest.fixture(scope="class")
    def api(self) -> KinopoiskApi:
        """
        Инициализация API клиента
        """
        return KinopoiskApi()

    @allure.title("Поиск фильмов без фильтров")
    @allure.story("Поиск фильмов")
    def test_search_movies_without_filters(
        self,
        api: KinopoiskApi
    ) -> None:
        params: Dict[str, Any] = {
            "page": 1,
            "limit": 10
        }

        response = api.search_movies(params)

        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

        with allure.step("Проверка наличия фильмов в ответе"):
            assert len(response.json()["docs"]) > 0

    @allure.title("Поиск фильмов с фильтром по рейтингу")
    @allure.story("Фильтрация фильмов")
    def test_search_movies_by_rating(
        self,
        api: KinopoiskApi
    ) -> None:
        params: Dict[str, Any] = {
            "rating.kp": "7-10",
            "limit": 10
        }

        response = api.search_movies(params)

        assert response.status_code == 200
        assert len(response.json()["docs"]) > 0

    @allure.title("Поиск фильмов по стране производства")
    @allure.story("Фильтрация фильмов")
    def test_search_movies_by_country(
        self,
        api: KinopoiskApi
    ) -> None:
        params: Dict[str, Any] = {
            "countries.name": "США",
            "limit": 10
        }

        response = api.search_movies(params)

        assert response.status_code == 200
        assert len(response.json()["docs"]) > 0

    @allure.title("Поиск фильмов по жанру")
    @allure.story("Фильтрация фильмов")
    def test_search_movies_by_genre(
        self,
        api: KinopoiskApi
    ) -> None:
        params: Dict[str, Any] = {
            "genres.name": "драма",
            "limit": 10
        }

        response = api.search_movies(params)

        assert response.status_code == 200
        assert len(response.json()["docs"]) > 0

    @allure.title("Поиск фильмов по году выпуска")
    @allure.story("Фильтрация фильмов")
    def test_search_movies_by_year(
        self,
        api: KinopoiskApi
    ) -> None:
        params: Dict[str, Any] = {
            "year": 2024,
            "limit": 10
        }

        response = api.search_movies(params)

        assert response.status_code == 200
        assert len(response.json()["docs"]) > 0
