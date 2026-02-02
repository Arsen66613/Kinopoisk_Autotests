import json
from typing import Dict, Any


class DataProvider:
    @staticmethod
    def load() -> Dict[str, Any]:
        """
        Загрузка тестовых данных из json-файла

        :return: словарь с тестовыми данными
        """
        with open(
            "test_data.json",
            encoding="utf-8"
        ) as file:
            return json.load(file)
