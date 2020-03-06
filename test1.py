import time
import HtmlTestRunner
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/Users/allan/Desktop/python-tcode/FWUITest/FlowworksBeta/Drivers/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

base_url = "http://beta.flowworks.com"
username = "alanli"
password = "DC9kt10&2A8#"

driver.get(base_url)
username_input = driver.find_element_by_id("txtUsername")
username_input.clear()
username_input.send_keys(username)
password_input = driver.find_element_by_name("Password")
password_input.clear()
password_input.send_keys(password)
loginButton = driver.find_element_by_id("btnSubmitLogin")
loginButton.click()

agreed = driver.find_element_by_id("Agreed")
agreed.click()
accept = driver.find_element_by_id("continue")
accept.click()

graph = driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/a)")
graph.click()
graphing_tool = driver.find_element_by_xpath("(/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[1]/a)")
graphing_tool.click()

allSideNodes = driver.find_elements_by_css_selector("#site-tree li[rel=site]")
print(allSideNodes[0].get_attribute("id"))