import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from utils.driver_factory import get_driver
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def driver(request):
    remote = os.getenv("RUN_REMOTE", "false").lower() == "true"

    build_name = "JS Alerts Scenarios"
    test_name = request.node.name

    driver = get_driver(remote=remote, build_name=build_name, test_name=test_name)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit()


def test_simple_alert(driver):
    try:
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = Alert(driver)
        assert alert.text == "I am a JS Alert"
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert result == "You successfully clicked an alert"
        driver.execute_script("lambda-status=passed")
    except Exception:
        driver.execute_script("lambda-status=failed")
        raise


def test_confirm_alert_ok(driver):
    try:
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = Alert(driver)
        assert alert.text == "I am a JS Confirm"
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert result == "You clicked: Ok"
        driver.execute_script("lambda-status=passed")
    except Exception:
        driver.execute_script("lambda-status=failed")
        raise


def test_confirm_alert_cancel(driver):
    try:
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = Alert(driver)
        alert.dismiss()

        result = driver.find_element(By.ID, "result").text
        assert result == "You clicked: Cancel"
        driver.execute_script("lambda-status=passed")
    except Exception:
        driver.execute_script("lambda-status=failed")
        raise


def test_prompt_alert_input(driver):
    try:
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = Alert(driver)
        assert alert.text == "I am a JS prompt"
        alert.send_keys("Kapil")
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert result == "You entered: Kapil"
        driver.execute_script("lambda-status=passed")
    except Exception:
        driver.execute_script("lambda-status=failed")
        raise


def test_prompt_alert_dismiss(driver):
    try:
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = Alert(driver)
        alert.dismiss()

        result = driver.find_element(By.ID, "result").text
        assert result == "You entered: null"
        driver.execute_script("lambda-status=passed")
    except Exception:
        driver.execute_script("lambda-status=failed")
        raise
