import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# YANDEX_LOGIN = os.getenv("YANDEX_LOGIN")
# YANDEX_PASSWORD = os.getenv("YANDEX_PASSWORD")
AUTH_URL = "https://passport.yandex.ru/auth/"

# Для аккаунта может быть включена 2FA, автопрохождение нестабильно

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1400,1000")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(
        service=service, options=options)
    
    yield browser
    browser.quit()


# @pytest.mark.skipif(
    # not YANDEX_LOGIN or not YANDEX_PASSWORD,
    # reason="Нет YANDEX_LOGIN и YANDEX_PASSWORD в переменных окружения",
# )

def test_yandex_auth_page_open(driver):
    driver.get(AUTH_URL)
    wait = WebDriverWait(driver, 40)

    login_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
    )
    # login_input.clear()
    # login_input.send_keys(YANDEX_LOGIN)

    # next_button = wait.until(
        # EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    # )
    # next_button.click()

    # password_input = wait.until(
       # EC.visibility_of_element_located((By.NAME, "passwd"))
    # )
    # password_input.clear()
    # password_input.send_keys(YANDEX_PASSWORD)

    # enter_button = wait.until(
      #  EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    # )
    # enter_button.click()

    # wait.until(lambda d: "passport.yandex.ru/auth" not in d.current_url)

    # assert "passport.yandex.ru/auth" not in driver.current_url

    assert login_input.is_displayed()