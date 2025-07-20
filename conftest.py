import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import os

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Captura de pantalla automática si el test falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{screenshots_dir}/FAILED_{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
