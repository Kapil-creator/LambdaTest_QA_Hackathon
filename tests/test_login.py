import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture
def driver(request):
    remote = os.getenv("RUN_REMOTE", "false").lower() == "true"

    build_name = "Login Scenarios"
    test_name = request.node.name  # Dynamically picks function name

    driver = get_driver(remote=remote, build_name=build_name, test_name=test_name)
    yield driver
    driver.quit()


def test_valid_login(driver):
    try:
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        driver.get("https://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        success_message = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in success_message

        driver.execute_script("lambda-status=passed")
    except Exception as e:
        driver.execute_script("lambda-status=failed")
        raise e


def test_invalid_login(driver):
    try:
        invalid_username = os.getenv("INVALID_USERNAME")
        invalid_password = os.getenv("INVALID_PASSWORD")

        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys(invalid_username)
        driver.find_element(By.ID, "password").send_keys(invalid_password)
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        error_message = driver.find_element(By.ID, "flash").text
        assert "Your username is invalid!" in error_message

        driver.execute_script("lambda-status=passed")
    except Exception as e:
        driver.execute_script("lambda-status=failed")
        raise e
