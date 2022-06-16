import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.checkoutpage import CheckOutPage
from pageobject.homepage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixture("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        #homepage.ShopItems().click()
        checkoutpage = homepage.ShopItems()
        log.info("getting all cards info")
        #checkoutpage = CheckOutPage(self.driver)
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getcardFooter()[i].click()


        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifytext("India")
        #wait = WebDriverWait(self.driver, 15)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']/label").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        successtext = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successtext

        self.driver.get_screenshot_as_file("screen.png")





