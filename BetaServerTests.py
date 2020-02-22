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
from seleniumrequests import Chrome
from seleniumrequests.request import RequestMixin

class CheckElementsCorrect(unittest.TestCase):

    base_url = "https://beta.flowworks.com"

    user_name = "alanli"

    user_password = "DC9kt10&2A8#"

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:/Users/allan/Desktop/FWUITest/Flowworks/Drivers/chromedriver.exe')

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
    
    def test_FLWS_Search_TC_001_User_Login_In(self):

        self.driver.get(self.base_url)

        username_input = self.driver.find_element_by_id("txtUsername")

        username_input.clear()

        username_input.send_keys(self.user_name)

        password_input = self.driver.find_element_by_name("Password")

        password_input.clear()

        password_input.send_keys(self.user_password)

        loginButton2 = self.driver.find_element_by_id("btnSubmitLogin")

        loginButton2.click()

        agreed = self.driver.find_element_by_id("Agreed")

        agreed.click()

        accept = self.driver.find_element_by_id("continue")

        accept.click()

        self.assertIn("Network Map", self.driver.title)

    def test_FLWS_Search_TC_002_Get_Graphing_Tool(self):

        self.driver.get(self.base_url)

        username_input = self.driver.find_element_by_id("txtUsername")

        username_input.clear()

        username_input.send_keys(self.user_name)

        password_input = self.driver.find_element_by_name("Password")

        password_input.clear()

        password_input.send_keys(self.user_password)

        loginButton2 = self.driver.find_element_by_id("btnSubmitLogin")

        loginButton2.click()

        agreed = self.driver.find_element_by_id("Agreed")

        agreed.click()

        accept = self.driver.find_element_by_id("continue")

        accept.click()

        initiate_toggle = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/a)")

        initiate_toggle.click()

        graphing_tool = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[1]/a)")

        graphing_tool.click()

        self.assertIn("Graphing", self.driver.title)
    
    def test_FLWS_Search_TC_003_Generate_A_Graph(self):

        self.driver.get(self.base_url)

        username_input = self.driver.find_element_by_id("txtUsername")

        username_input.clear()

        username_input.send_keys(self.user_name)

        password_input = self.driver.find_element_by_name("Password")

        password_input.clear()

        password_input.send_keys(self.user_password)

        loginButton2 = self.driver.find_element_by_id("btnSubmitLogin")

        loginButton2.click()

        agreed = self.driver.find_element_by_id("Agreed")

        agreed.click()

        accept = self.driver.find_element_by_id("continue")

        accept.click()

        initiate_toggle = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/a)")

        initiate_toggle.click()

        graphing_tool = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[1]/a)")

        graphing_tool.click()

        dataLogger = self.driver.find_element_by_id("590_anchor")

        dataLogger.click()

        dataLogger_sub_1 = self.driver.find_element_by_id("590|197_anchor")

        dataLogger_sub_1.click()

        from_date = self.driver.find_element_by_id("txtFrom")

        from_date.clear()

        from_date.send_keys("2016-01-01 00:00")

        to_date = self.driver.find_element_by_id("txtTo")

        to_date.clear()

        to_date.send_keys("2017-01-01 00:00")

        plot_data = self.driver.find_element_by_xpath("(//*[@id='btnPlot'])")

        plot_data.click()

        GRAPH_CANVAS_LOCATOR = (By.ID, "graph-canvas")

        graph_canvas = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(GRAPH_CANVAS_LOCATOR))

        self.assertTrue(graph_canvas.is_displayed())
    
    def test_FLWS_Search_TC_004_Make_Sure_Graph_Elements_Correct(self):

        self.driver.get(self.base_url)

        username_input = self.driver.find_element_by_id("txtUsername")

        username_input.clear()

        username_input.send_keys(self.user_name)

        password_input = self.driver.find_element_by_name("Password")

        password_input.clear()

        password_input.send_keys(self.user_password)

        loginButton2 = self.driver.find_element_by_id("btnSubmitLogin")

        loginButton2.click()

        agreed = self.driver.find_element_by_id("Agreed")

        agreed.click()

        accept = self.driver.find_element_by_id("continue")

        accept.click()

        initiate_toggle = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/a)")

        initiate_toggle.click()

        graphing_tool = self.driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[1]/a)")

        graphing_tool.click()

        dataLogger = self.driver.find_element_by_id("590_anchor")

        dataLogger.click()

        dataLogger_sub_1 = self.driver.find_element_by_id("590|197_anchor")

        dataLogger_sub_1.click()

        from_date = self.driver.find_element_by_id("txtFrom")

        from_date.clear()

        from_date.send_keys("2016-01-01 00:00")

        to_date = self.driver.find_element_by_id("txtTo")

        to_date.clear()

        to_date.send_keys("2017-01-01 00:00")

        plot_data = self.driver.find_element_by_xpath("(//*[@id='btnPlot'])")

        plot_data.click()

        GRAPH_CANVAS_LOCATOR = (By.ID, "graph-canvas")

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(GRAPH_CANVAS_LOCATOR))

        response = self.driver.request('GET', 'http://beta.flowworks.com/network/graph-new#timeseries/sites/590,197/period/CST/daterange/2016-01-01%2000%3A00|2017-01-01%2000%3A00')
# rather than generating requests, it will be better to detect the requests and check the status at the same time.


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/allan/Desktop/FWUITest/Results'))