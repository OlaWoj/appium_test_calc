import os
from appium import webdriver
from pages.home_page import HomePage
from pages.history_page import HistoryPage

app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = app_path

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
home_page = HomePage(driver)
history_page = HistoryPage(driver)

def test_tan():
    home_page.wait_until_panel_is_hidden()
    home_page.calculate_tan()
    result = home_page.get_result()
    assert result == "0.2125565616"

def test_factorial():
    home_page.calculate_factorial()
    result = home_page.get_result()
    assert result == "720"

def test_cos():
    home_page.wait_until_panel_is_hidden()
    home_page.calculate_cos()
    result = home_page.get_result()
    assert result == "0.9848077530"

# def test_history():
#     home_page.add_digits(1, 2)
#     home_page.navigate_to_history()
#     result = history_page.get_history_result()
#     assert result == "3"
#
# def test_log():
#     home_page.wait_until_panel_is_hidden()
#     home_page.calculate_log()
#     result = home_page.get_result()
#     assert result == "1"
#
#
# def test_add():
#     home_page.add_digits(1, 2)
#     result = home_page.get_result()
#     assert result == "3"
#
#
# def test_sub():
#     home_page.sub_digits(1, 2)
#     result = home_page.get_result()
#     assert result == "−1"
#
#
# def test_mul():
#     home_page.mul_digits(1, 2)
#     result = home_page.get_result()
#     assert result == "2"
#
#
# def test_div():
#     home_page.div_digits(1, 2)
#     result = home_page.get_result()
#     assert result == "0.5"
#
#
# def test_zero_div():
#     home_page.div_digits(1, 0)
#     result = home_page.get_result_preview()
#     assert result == "Can't divide by 0"
#
#
# def test_multiple_operations():
#     home_page.add_digits(1, 2)
#     result = home_page.get_result()
#     home_page.mul_digits(result, 3)
#     result2 = home_page.get_result()
#     home_page.div_digits(result2, 2)
#     result3 = home_page.get_result()
#     assert result3 == "4.5"