import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AuthPage:
    """
    Page Object страницы авторизации Kinopoisk / Yandex ID
    """

    # ===== ЛОКАТОРЫ =====

    LOGIN_INPUT = (
        By.XPATH,
        (
            "//input[@data-testid='text-field-input' "
            "and @aria-label='Логин или email']"
        )
    )

    LOGIN_NEXT_BUTTON = (
        By.XPATH,
        (
            "//button[@data-testid='add-user-next' "
            "or @data-testid='split-add-user-next-login']"
        )
    )

    LOGIN_WITH_PASSWORD_BUTTON = (
        By.XPATH,
        "//button[@data-testid='password-btn']"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        (
            "//input[@data-testid='text-field-input' "
            "and @aria-label='Пароль']"
        )
    )

    PASSWORD_NEXT_BUTTON = (
        By.XPATH,
        "//button[@data-testid='password-next']"
    )

    USER_AVATAR = (
        By.XPATH,
        (
            "//button[contains(@class, 'user-pic')] | "
            "//img[contains(@src, 'avatar')]"
        )
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button//span[text()='Войти']"
    )

    # ===== КОНСТРУКТОР =====

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ===== МЕТОДЫ =====

    @allure.step("Открыть страницу авторизации: {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Ввести логин (email)")
    def enter_login(self, login: str) -> None:
        login_input = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_INPUT)
        )
        login_input.clear()
        login_input.send_keys(login)

    @allure.step("Нажать кнопку Далее после ввода логина")
    def click_login_next(self) -> None:
        next_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_NEXT_BUTTON)
        )
        next_button.click()

    @allure.step("Нажать «Войти с паролем»")
    def click_login_with_password(self) -> None:
        password_button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_WITH_PASSWORD_BUTTON
            )
        )
        password_button.click()

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        password_input = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

    @allure.step("Нажать кнопку Далее после ввода пароля")
    def click_password_next(self) -> None:
        next_button = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_NEXT_BUTTON)
        )
        next_button.click()

    @allure.step(
        "Ожидать ввод капчи или завершение авторизации "
        "(до 60 секунд)"
    )
    def wait_for_captcha_or_auth(self) -> None:
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    self.USER_AVATAR
                )
            )
        except TimeoutException:
            pass

    @allure.step("Проверить, что пользователь авторизован")
    def assert_user_authorized(self) -> None:
        self.wait_for_captcha_or_auth()

        self.wait.until(
            EC.presence_of_element_located(self.USER_AVATAR)
        )

        login_buttons = self.driver.find_elements(
            *self.LOGIN_BUTTON
        )

        assert (
            len(login_buttons) == 0
        ), "Пользователь не авторизован — кнопка 'Войти' присутствует"
