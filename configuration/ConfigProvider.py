from configparser import ConfigParser


class ConfigProvider:
    _parser: ConfigParser | None = None

    @classmethod
    def _get_parser(cls) -> ConfigParser:
        if cls._parser is None:
            parser = ConfigParser()
            parser.read("test_config.ini", encoding="utf-8")
            cls._parser = parser
        return cls._parser

    @classmethod
    def get(cls, section: str, key: str) -> str:
        """
        Получить значение из test_config.ini

        :param section: секция ini-файла
        :param key: ключ в секции
        :return: значение параметра
        """
        parser = cls._get_parser()
        return parser.get(section, key)
