from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver


    cardTitle = (By.XPATH,"//div[@class='card h-100']")
    cardFooter= (By.XPATH,"div/h4/a")
               #= (By.XPATH,"div[2]/button")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
    def getcardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)
    #def getcardFooter(self):
        #return self.driver.find_element(*CheckOutPage.cardFooter)
    #def checkoutpage(self):
