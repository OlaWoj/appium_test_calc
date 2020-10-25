from appium import webdriver


class BasePage:

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver