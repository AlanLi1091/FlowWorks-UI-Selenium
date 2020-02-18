# Generate a graph

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DisplayGraph(unittest.TestCase):

    base_url = "https://www.flowworks.com"

    user_name = "alanli"

    user_password = "DC9kt10&2A8#"

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:/Users/allan/Desktop/FWUITest/Flowworks/Drivers/chromedriver.exe')

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
    
    def test_get_graph(self):
        
        self.driver.get(self.base_url)

        loginButton = self.driver.find_element_by_id("menu-item-781")

        loginButton.click()

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

        dataLogger = self.driver.find_element_by_id("598_anchor")

        dataLogger.click()

        dataLogger_sub_1 = self.driver.find_element_by_id("598|185_anchor")

        dataLogger_sub_1.click()

        dataLogger_sub_2 = self.driver.find_element_by_id("598|184_anchor")
        
        dataLogger_sub_2.click()

        plot_data = self.driver.find_element_by_xpath("(/html/body/section/div/aside/div/div[2]/div[5]/button[1])")

        plot_data.click()

        graph_canvas = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.ID,"graph-canvas"))

        self.assertTrue(graph_canvas.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/allan/Desktop/FWUITest/Results'))