import time
from typing import Dict, Any

import allure
import requests

from configuration.ConfigProvider import ConfigProvider


class KinopoiskApi:
    def __init__(self) -> None:
        self.base_url: str = ConfigProvider.get(
            "api",
            "base_url"
        )
        self.token: str = ConfigProvider.get(
            "api",
            "token"
        )
        self.timeout: int = int(
            ConfigProvider.get(
                "api",
                "timeout"
            )
        )

    def _headers(self, with_token: bool = True) -> Dict[str, str]:
        """
        Формирование заголовков запроса

        :param with_token: использовать ли токен
        :return: словарь заголовков
        """
        if with_token:
            return {
                "X-API-KEY": self.token
            }

        return {}

    @allure.step("Поиск фильмов с параметрами: {params}")
    def search_movies(
        self,
        params: Dict[str, Any],
        with_token: bool = True
    ) -> requests.Response:
        """
        Поиск фильмов через API Kinopoisk

        :param params: параметры запроса
        :param with_token: использовать ли токен
        :return: Response
        """
        for attempt in range(3):
            try:
                return requests.get(
                    url=f"{self.base_url}/v1.4/movie",
                    headers=self._headers(with_token),
                    params=params,
                    timeout=self.timeout
                )
            except requests.exceptions.ReadTimeout:
                if attempt == 2:
                    raise
                time.sleep(1)
