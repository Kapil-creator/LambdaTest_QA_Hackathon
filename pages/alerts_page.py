from selenium.webdriver.common.by import By

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/javascript_alerts"

    def open(self):
        self.driver.get(self.url)

    def trigger_alert(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    def trigger_confirm(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    def trigger_prompt(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    def get_result_text(self):
        return self.driver.find_element(By.ID, "result").text