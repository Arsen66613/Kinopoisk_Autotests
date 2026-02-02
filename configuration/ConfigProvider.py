import os
from configparser import ConfigParser


class ConfigProvider:
    _parser: ConfigParser | None = None

    @classmethod
    def _get_parser(cls) -> ConfigParser:
        if cls._parser is None:
            parser = ConfigParser()
            parser.read(
                "test_config.ini",
                encoding="utf-8"
            )
            cls._parser = parser
        return cls._parser

    @classmethod
    def get(cls, section: str, key: str) -> str:
        """
        Получить значение из test_config.ini
        или из переменной окружения

        :param section: секция ini-файла
        :param key: ключ в секции
        :return: значение параметра
        """
        parser = cls._get_parser()
        value = parser.get(section, key)

        if value.startswith("${") and value.endswith("}"):
            env_key = value[2:-1]
            env_value = os.getenv(env_key)

            if env_value is None:
                raise RuntimeError(
                    f"Переменная окружения "
                    f"{env_key} не установлена"
                )

            return env_value

        return value
