import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, sys, inspect
# fetch path to the directory in which current file is, from the root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/file to be imported
sys.path.insert(0, parentdir+'/Resources')
sys.path.insert(0, parentdir+'/Resources/PO')


from Locators import Locators
from TestData import TestData
import Page
from Page import LoginPage, AcknowledgementPage, NetworkMapPage, GeneratingGraphPage

class Test_FWB_Search_Base(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options = chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit() 

class Test_FWB_Search(Test_FWB_Search_Base):
    def setUp(self):
        super().setUp()
    
    def test_checking_web_elements(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_into_page()
        self.acknowledgementPage = AcknowledgementPage(self.loginPage.driver)
        self.acknowledgementPage.acknowledgement()
        self.networkMapPage = NetworkMapPage(self.acknowledgementPage.driver)
        self.networkMapPage.site_access()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/allan/Desktop/FWUITest/Results'))    
       