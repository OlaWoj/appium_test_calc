from pages.base_page import BasePage


from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HistoryPage(BasePage):

    history_result_selector = (MobileBy.ID, "history_result")

    def get_history_result(self):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.history_result_selector)).text
        return result