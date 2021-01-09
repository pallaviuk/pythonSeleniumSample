import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


# @pytest.mark.usefixtures("setup") #Created BaseClass in Utilities so that dont have to imclude this in all py files
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all card details")
        products = checkoutPage.getProductTitles()

        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getProductFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmPage = checkoutPage.checkoutItems()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")

        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info("successText")

        # assert "Success! Thank you!" in successText
        assert "Success! Thank you kjfaeshgkvjahskj ghj!" in successText

        self.driver.get_screenshot_as_file("screen.png")