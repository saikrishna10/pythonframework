import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestsData.HomePageData import HomePageData
from pageobject.homepage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):




    def test_formsubmission(self,getData):
        #driver = webdriver.Chrome("C:\webdriverpy\chromedriver_win32 (1)\chromedriver.exe")
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #driver.maximize_window()
        homepage = HomePage(self.driver)
        homepage.getname().send_keys("firstname")
        #self.driver.find_element_by_css_selector("[name='name']").send_keys("sai")
        homepage.getemail().send_keys("lastname")
        #self.driver.find_element_by_name("email").send_keys("krishna")
        homepage.getid().click()
        #self.driver.find_element_by_id("exampleCheck1").click()
        sel = Select(homepage.clickcheckbox())
        sel = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        #self.selectOptionBytext(homepage.getgender(),"male")
        #sel.select_by_visible_text("Male")
        self.driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/input").click()
        alertText = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        assert ("success" in alertText)
        self.driver.refresh()



    #@pytest.fixture(params=[("sai","krishna","male"),("komi","kondra","female")])
    #def getData(self,request):
        #return request.param

    #@pytest.fixture(params=HomePageData.test_HomePage_data)
    #def getData(self, request):
        #return request.param

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param