import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions as EC, select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageobject import homepage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  #fileHandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifytext(self,text):
        element = WebDriverWait(self.driver, 7).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoption(self):
        sel = Select(homepage.clickcheckbox())
        sel.select_by_visible_text("Male")

    #def selectOptionBytext(self,locator,text):
        #sel = select(locator)
        #sel.select_by_visible_text(text)
