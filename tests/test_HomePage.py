import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Submission form test")
        # homepage.getName().send_keys(getData[0])
        homepage.getName().send_keys(getData["firstname"])
        # homepage.getEmail().send_keys(getData[1])
        homepage.getEmail().send_keys(getData["emailid"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessgae().text

        assert "success" in alertText
        self.driver.refresh()


    # @pytest.fixture(params=[("Pallavi","pallavi.kukkillaya@gmail.com", "Female"),("Niranjan","Niranjan.s@gmail.com", "Male")])
    @pytest.fixture(params=HomePageData.test_homePage_data)
    def getData(self, request):
        return request.param

#pytest --browser_name chrome --html=C:\Users\UKPallavi\PycharmProjects\PythonSeleniumFramework\reports\report.html