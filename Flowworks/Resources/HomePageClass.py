from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import BasePageClass
import locators
import testdata

driver = webdriver.Chrome('C:/Users/allan/Desktop/FWUITest/driver/chromedriver.exe')

class HomePage(BasePage):
    """Home page of Flowworks"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self)