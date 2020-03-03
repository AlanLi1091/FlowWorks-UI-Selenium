import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

from Locators import Locators
from TestData import TestData

class BasePage():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    #This function is called every time a new object of the base class is created
    def __init__(self, driver):
        self.driver = driver
    
    #This function performs click on web element whose locator is passed to it
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    
    #This function asserts comparison of a web element's text with passed in text
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    #This function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    #this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    #web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    
    #this function checks if the web element whose locator has been passed to it, is visible or not and returns
    #true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    #this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

class HomePage(BasePage):
    """Home Page of FlowWorks"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    def login(self):
        self.click(Locators.LOGIN_BUTTON1)
    
class LoginPage(BasePage):
    """Login Page of Flowworks"""
    def __init__(self, driver):
        super().__init__(driver)
    
    def login_into_page(self):
        self.enter_text(Locators.INPUT_USERNAME_BOX, TestData.USERNAME)
        self.enter_text(Locators.INPUT_PASSWORD_BOX, TestData.PASSWORD)
        self.click(Locators.LOGIN_BUTTON2)

class AcknowledgementPage(BasePage):
    """Acknowledgement Page after Login Page"""
    def __init__(self, driver):
        super().__init__(driver)

    def acknowledgement(self):
        self.click(Locators.AGREED_BOX)
        self.click(Locators.CONTINUE_BUTTON)

class NetworkMapPage(BasePage):
    """This is the network map page after the acknowledgement page"""
    def __init__ (self, driver):
        super().__init__(driver)
    
    def graphing_tool_access(self):
        self.click(Locators.GRAPH_TOGGLE)
        self.click(Locators.GRAPHING_TOOL)
    
    def network_map_access(self):
        self.click(Locators.DC_MAP)

class GeneratingGraphPage(BasePage):
    """This class allows the automated testing machine to generate the graph"""
    def __init__(self, driver):
        super().__init__(driver)

    def generating_graph(self):
        self.click(Locators.DC_CA)
        self.click(Locators.DC_CAT)
        self.click(Locators.DC_CAWS)
        self.click(Locators.PLOT_BTN)

    def return_to_network_map(self):
        self.click(Locators.MONITOR_TOGGLE)
        self.click(Locators.NETWORK_MAP)