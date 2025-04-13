from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
import os

def get_driver(remote: bool = False, build_name: str = "Default Build", test_name: str = "Unnamed Test") -> WebDriver:
    if remote:
        username = os.getenv("LT_USERNAME")
        access_key = os.getenv("LT_ACCESS_KEY")
        url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

        lt_options = {
            "platformName": "Windows 11",
            "project": "QA Hackathon",
            "build": build_name,
            "name": test_name,
            "selenium_version": "4.0.0",
        }

        options = webdriver.ChromeOptions()
        options.browser_version = "latest"
        options.set_capability('LT:Options', lt_options)

        return webdriver.Remote(command_executor=url, options=options)
    else:
        options = Options()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)



