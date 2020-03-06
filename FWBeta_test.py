import unittest
import time
import HtmlTestRunner
import urllib3
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckElementsCorrect(unittest.TestCase):

    base_url = "http://beta.flowworks.com"
    username = "alanli"
    password = "DC9kt10&2A8#"

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:/Users/allan/Desktop/python-tcode/FWUITest/FlowworksBeta/Drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test(self):
        
        self.driver.get(self.base_url)
        username_input = self.driver.find_element_by_id("txtUsername")
        username_input.clear()
        username_input.send_keys(self.username)
        password_input = self.driver.find_element_by_name("Password")
        password_input.clear()
        password_input.send_keys(self.password)
        loginButton = self.driver.find_element_by_id("btnSubmitLogin")
        loginButton.click()
        agreed = self.driver.find_element_by_id("Agreed")
        agreed.click()
        accept = self.driver.find_element_by_id("continue")
        accept.click()
        self.assertIn("Network Map", self.driver.title)
        sites = self.driver.find_elements_by_class_name("jstree-anchor")
        GOOGLE_MAP_LOCATOR = (By.CLASS_NAME, "gm-style")
        google_map = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(GOOGLE_MAP_LOCATOR))
        for site in sites:
            site.click()
            self.assertTrue(google_map.is_displayed())
        graph = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/a)")
        graph.click()
        graphing_tool = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[1]/a)")
        graphing_tool.click()
        self.assertIn("Graphing", self.driver.title)
        date_from = self.driver.find_element_by_id("txtFrom")
        date_from.clear()
        date_from.send_keys("2006-01-01 00:00")
        date_to = self.driver.find_element_by_id("txtTo")
        date_to.clear()
        date_to.send_keys("2019-12-31 23:59")
        allSideNodes = self.driver.find_elements_by_css_selector("#site-tree li[rel=site]")
        plot_data = self.driver.find_element_by_xpath("(/html/body/section/div/aside/div/div[2]/div[5]/button[1])")     
        allSideNodes_ids = []
        for i in range(0, len(allSideNodes)):
            allSideNodes_ids.append(allSideNodes[i].get_attribute("id"))
        for id in allSideNodes_ids:
            self.driver.execute_script("$('#site-tree').jstree('check_node',{})".format(str(id)))
            WebDriverWait(self.driver, 2)
            plot_data.click()
            GRAPH_LOCATOR = (By.XPATH, "(/html/body/section/div/main/div[2]/div/div[2]/div/div/img)")
            graph = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(GRAPH_LOCATOR))
            self.assertTrue(graph.is_displayed())
            self.driver.execute_script("$('#site-tree').jstree('uncheck_node',{})".format(str(id)))
        
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/allan/Desktop/python-tcode/FWUITest/Results'))