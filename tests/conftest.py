import os
from os import getcwd

import pytest
from selenium import webdriver
driver = None #For screenshot

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
#py.test --browser_name chrome - The above code is a set up to run cmd with browser option

@pytest.fixture(scope="class")
def setup(request):
    global driver #For screenshot - new object will not be created
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\selenium\geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#      Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             _capture_Screenshot(file_name)
#             if file_name:
#                 fpath = getcwd()
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '\
#                           'onclick="window.open(this.src)" align="right"/></div>' % (fpath, file_name)
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                fpath = os.getcwd() #When reports were moved to different folder - Reports . This was added to fix the broken screenshot issue
                html = '<div><img src="file:%s/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % (fpath, file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

#py.test --browser_name chrome --html=$WORKSPACE\reports\report.html -v --junitxml="result.xml"
#py.test --browser_name chrome --html=$WORKSPACE\reports\report.html