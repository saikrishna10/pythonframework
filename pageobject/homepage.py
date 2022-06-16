from selenium.webdriver.common.by import By

from pageobject.checkoutpage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME,("email"))
    id   = (By.ID,("exampleCheck1"))
    check = (By.ID,("exampleFormControlSelect1"))



    def ShopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage


    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getid(self):
        return self.driver.find_element(*HomePage.id)

    def clickcheckbox(self):
        return self.driver.find_element(*HomePage.check)