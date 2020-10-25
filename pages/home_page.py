from appium.webdriver.common.touch_action import TouchAction

from pages.base_page import BasePage


from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    equals_selector = (MobileBy.ACCESSIBILITY_ID, "equals")
    plus_selector = (MobileBy.ACCESSIBILITY_ID, "plus")
    minus_selector = (MobileBy.ACCESSIBILITY_ID, "minus")
    multiply_selector = (MobileBy.ACCESSIBILITY_ID, "multiply")
    divide_selector = (MobileBy.ACCESSIBILITY_ID, "divide")
    result_selector = (MobileBy.ID, "result_final")
    result_preview_selector = (MobileBy.ID, "result_preview")
    arrow_panel_selector = (MobileBy.ID, "arrow")
    logarithm_selector = (MobileBy.ACCESSIBILITY_ID, "logarithm")
    more_options_selector = (MobileBy.ACCESSIBILITY_ID, "More options")
    history_selector = (MobileBy.ID, "//*[contains(., 'History'")
    cos_selector = (MobileBy.ACCESSIBILITY_ID, 'cosine')
    power_selector = (MobileBy.ACCESSIBILITY_ID, 'factorial')
    tan_selector = (MobileBy.ACCESSIBILITY_ID, 'tangent')

    def add_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.plus_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def sub_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.minus_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def div_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.divide_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def mul_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.multiply_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def calculate_log(self):
        self.open_expert_panel()
        self.driver.find_element(*self.logarithm_selector).click()
        self.close_expert_panel()
        self.driver.find_element(*self.digit_locator(1)).click()
        self.driver.find_element(*self.digit_locator(0)).click()
        self.driver.find_element(*self.equals_selector).click()

    def get_result(self):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.result_selector)).text
        return result

    def get_result_preview(self):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.result_preview_selector)).text
        return result


    def digit_locator(self, value):
        selector = (MobileBy.ID, f"digit_{value}")
        return selector

    def open_expert_panel(self):
        TouchAction(self.driver).tap(None, 1000, 1500).perform()

    def close_expert_panel(self):
        self.driver.find_element(*self.arrow_panel_selector).click()

    def wait_until_panel_is_hidden(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.arrow_panel_selector))

    def navigate_to_history(self):
        self.driver.find_element(*self.more_options_selector).click()
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.history_selector))

    def calculate_cos(self):
        self.open_expert_panel()
        self.driver.find_element(*self.cos_selector).click()
        self.close_expert_panel()
        self.driver.find_element(*self.digit_locator(1)).click()
        self.driver.find_element(*self.digit_locator(0)).click()
        self.driver.find_element(*self.equals_selector).click()

    def calculate_factorial(self):
        self.driver.find_element(*self.digit_locator(6)).click()
        self.open_expert_panel()
        self.driver.find_element(*self.power_selector).click()
        self.close_expert_panel()
        self.driver.find_element(*self.equals_selector).click()

    def calculate_tan(self):
        self.open_expert_panel()
        self.driver.find_element(*self.tan_selector).click()
        self.close_expert_panel()
        self.driver.find_element(*self.digit_locator(1)).click()
        self.driver.find_element(*self.digit_locator(2)).click()
        self.driver.find_element(*self.equals_selector).click()
