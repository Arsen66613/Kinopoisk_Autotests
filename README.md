# kinopoisk_autotests


## Дипломный проект по автоматизации UI и API тестирования
Автоматизируются UI- и API-тесты финального проекта по ручному тестированию:
https://ars-66613.yonote.ru/doc/finalnyj-proekt-po-ruchnomu-testirovaniyu-gOgY3RnE4t


### Стек:
- pytest
- selenium
- requests
- allure


### Установка зависимостей
pip install -r requirements.txt


### Структура проекта
- ./api — API-клиенты Kinopoisk
- ./configuration — конфигурация проекта
- ./page — Page Object'ы UI
- ./test
    - conftest.py — общие фикстуры
    - ./api — API-тесты
    - ./ui conftest.py — UI-фикстуры test_ui.py — UI-тесты
- conftest.py — UI-фикстуры
- test_ui.py — UI-тесты
- ./testdata — тестовые данные
- pytest.ini
- test_config.ini
- README.md


### Реализованные тесты
UI:

- Авторизация пользователя
- Фильтрация фильмов:

с высоким рейтингом

по стране производства

по жанру (Аниме)

по городу (Абакан)


API:
- Поиск фильмов
- Проверка структуры и статусов ответов

### Особенности UI-авторизации (капча)
При выполнении UI-тестов может потребоваться ручной ввод капчи.
Причина — защитные механизмы Kinopoisk / Yandex ID от автоматизации.
Полная автоматизация прохождения капчи невозможна.

В проекте:
используются явные ожидания (WebDriverWait)

sleep не применяется

тест корректно ожидает действий пользователя

### Почему используется несколько conftest.py
В проекте используются два файла conftest.py:

test/conftest.py — общие фикстуры

test/ui/conftest.py — UI-специфичные фикстуры

Такое разделение:

предотвращает влияние UI-фикстур на API-тесты

ограничивает область видимости фикстур pytest

упрощает поддержку и масштабирование проекта


### Запуск тестов
UI-тесты: pytest -m ui

API-тесты: pytest -m api

Все тесты: pytest


### Allure-отчёт
pytest --alluredir=allure-results

allure serve allure-results


### Переменная окружения KINOPOISK_TOKEN
Документация для API-тестов https://api.poiskkino.dev/documentation#/

Для запуска API-тестов требуется токен Kinopoisk API, который вы можете получить в боте @poiskkinodev_bot.

Токен не хранится в репозитории и должен быть задан
через переменную окружения KINOPOISK_TOKEN.

Windows (PowerShell) -> $env:KINOPOISK_TOKEN="ваш_api_токен"

Windows (cmd) -> set KINOPOISK_TOKEN=ваш_api_токен

Linux / macOS -> export KINOPOISK_TOKEN=ваш_api_токен


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)