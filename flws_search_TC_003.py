import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LogIn(unittest.TestCase):

    base_url = "https://www.flowworks.com"

    user_name = "alanli"

    user_password = "DC9kt10&2A8#"

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path="C:/Users/allan/Desktop/FWUITest/driver/chromedriver.exe")

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
    
    def test_user_login(self):
        
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

        self.assertIn("Graphing", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()