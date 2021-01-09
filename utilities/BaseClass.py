import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionByText(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        # logger = logging.getLogger(__name__)
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)


        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # FileHandler object

        logger.setLevel(logging.INFO)
        return logger