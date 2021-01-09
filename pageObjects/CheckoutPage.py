from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getProductFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkoutItems(self):
         self.driver.find_element(*CheckoutPage.checkout).click()
         confirmPage = ConfirmPage(self.driver)
         return confirmPage